
import math
from dataclasses import dataclass

import numpy as np
import pytest

from fnf import ReasoningAdapter


@dataclass
class DemoState:
    """Minimal state compatible with ReasoningAdapter."""

    coordinates: np.ndarray
    bonds: list[tuple[int, int]]

    def clone(self):
        return DemoState(
            coordinates=self.coordinates.copy(),
            bonds=list(self.bonds),
        )


@pytest.fixture
def adapter():
    return ReasoningAdapter(
        boundary1=1.0,
        boundary2=2.0,
        tolerance=1e-10,
    )


@pytest.fixture
def chain_state():
    coordinates = np.array(
        [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [3.0, 0.0, 0.0],
        ]
    )
    return DemoState(
        coordinates=coordinates,
        bonds=[(0, 1), (1, 2)],
    )


# ------------------------------------------------------------
# Logarithmic mathematics
# ------------------------------------------------------------

def test_logarithmic_coordinate(adapter):
    assert adapter.q(math.e) == pytest.approx(1.0)


def test_inversion_law(adapter):
    x = 7.5
    assert adapter.q(1 / x) == pytest.approx(-adapter.q(x))


def test_relative_position(adapter):
    assert adapter.relative_position(4.0, 2.0) == pytest.approx(
        math.log(2.0)
    )


def test_relation_is_boundary_independent(adapter):
    x, y = 8.0, 2.0

    assert adapter.relation(x, y) == pytest.approx(math.log(4.0))

    for boundary in (0.5, 1.0, 3.0, 10.0):
        difference = (
            adapter.relative_position(x, boundary)
            - adapter.relative_position(y, boundary)
        )
        assert difference == pytest.approx(adapter.relation(x, y))


@pytest.mark.parametrize("value", [0.0, -1.0, float("inf"), float("nan")])
def test_log_rejects_invalid_magnitudes(adapter, value):
    with pytest.raises(ValueError):
        adapter.q(value)


def test_invalid_boundaries_are_rejected():
    with pytest.raises(ValueError):
        ReasoningAdapter(boundary1=2.0, boundary2=1.0)


# ------------------------------------------------------------
# Many & Few classification
# ------------------------------------------------------------

@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0.5, "inside"),
        (1.0, "middle"),
        (1.5, "middle"),
        (2.0, "middle"),
        (3.0, "outside"),
    ],
)
def test_classification_boundaries(adapter, value, expected):
    result = adapter.classify(value)
    assert result.category == expected


def test_classify_many(adapter):
    result = adapter.classify_many([0.5, 1.0, 1.5, 2.0, 3.0])

    assert result == {
        "inside": [0.5],
        "middle": [1.0, 1.5, 2.0],
        "outside": [3.0],
    }


# ------------------------------------------------------------
# State validation and measurements
# ------------------------------------------------------------

def test_valid_state_passes_gate(adapter, chain_state):
    assert adapter.validate(chain_state)


def test_bond_lengths_are_measured(adapter, chain_state):
    measurements = adapter.measure(chain_state)

    assert measurements["bond:0-1"] == pytest.approx(1.0)
    assert measurements["bond:1-2"] == pytest.approx(2.0)


def test_log_measurements(adapter, chain_state):
    measurements = adapter.measure_log(chain_state)

    assert measurements["bond:0-1"] == pytest.approx(0.0)
    assert measurements["bond:1-2"] == pytest.approx(math.log(2.0))


def test_zero_length_bond_cannot_be_measured(adapter):
    state = DemoState(
        coordinates=np.array(
            [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        ),
        bonds=[(0, 1)],
    )

    # The graph can be structurally valid, but ln(0) is undefined.
    assert adapter.validate(state)

    with pytest.raises(ValueError, match="strictly positive"):
        adapter.measure(state)


def test_self_bond_is_rejected(adapter):
    state = DemoState(
        coordinates=np.zeros((2, 3)),
        bonds=[(0, 0)],
    )

    assert not adapter.validate(state)


def test_non_finite_coordinates_are_rejected(adapter):
    state = DemoState(
        coordinates=np.array(
            [[0.0, 0.0, 0.0], [float("nan"), 0.0, 0.0]]
        ),
        bonds=[(0, 1)],
    )

    assert not adapter.validate(state)


# ------------------------------------------------------------
# Transition integration
# ------------------------------------------------------------

def test_rigid_translation_preserves_measurements(adapter, chain_state):
    def translate(state):
        state.coordinates += np.array([5.0, -2.0, 3.0])
        return state

    result = adapter.apply_action(
        chain_state,
        translate,
        preserve_measurements=True,
    )

    assert result.valid
    assert result.state is not None
    assert np.allclose(
        result.state.coordinates,
        chain_state.coordinates + np.array([5.0, -2.0, 3.0]),
    )

    # The original state must not have been mutated.
    assert np.allclose(
        chain_state.coordinates,
        np.array([[0, 0, 0], [1, 0, 0], [3, 0, 0]]),
    )


def test_scaling_fails_measurement_preservation(adapter, chain_state):
    def scale(state):
        state.coordinates *= 2.0
        return state

    result = adapter.apply_action(
        chain_state,
        scale,
        preserve_measurements=True,
    )

    assert not result.valid
    assert any(
        "Preserved measurement changed" in error
        for error in result.errors
    )


def test_bond_cleavage_is_valid(adapter, chain_state):
    def cleave(state):
        state.bonds.remove((1, 2))
        return state

    result = adapter.apply_action(chain_state, cleave)

    assert result.valid
    assert result.state is not None
    assert (1, 2) not in result.state.bonds
    assert (0, 1) in result.state.bonds


def test_invariant_must_hold_before_and_after(adapter, chain_state):
    result = adapter.apply_action(
        chain_state,
        lambda state: state,
        invariants=[lambda state: (1, 2) not in state.bonds],
    )

    assert not result.valid
    assert any("Precondition invariant" in e for e in result.errors)


# ------------------------------------------------------------
# Search state keys
# ------------------------------------------------------------

def test_state_key_ignores_bond_endpoint_order(adapter):
    first = DemoState(
        coordinates=np.array([[0, 0, 0], [1, 0, 0]], dtype=float),
        bonds=[(0, 1)],
    )
    second = DemoState(
        coordinates=np.array([[0, 0, 0], [1, 0, 0]], dtype=float),
        bonds=[(1, 0)],
    )

    assert adapter.state_key(first) == adapter.state_key(second)
