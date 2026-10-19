from _future_ import annotations

from dataclasses import dataclass from math import isfinite, log from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple

import numpy as np

Bond = Tuple[int, int] StateLike = Any ActionFunction = Callable[[StateLike], StateLike] InvariantFunction = Callable[[StateLike], bool]

@dataclass(frozen=True) class GateResult: """Structured result from a framework validation gate."""

valid: bool
gate: str
message: str


@dataclass(frozen=True) class TransitionResult: """Result of applying and validating a state transition."""

valid: bool
state: Optional[StateLike]
errors: Tuple[str, ...]


@dataclass(frozen=True) class Classification: """Many & Few classification for one positive magnitude."""

value: float
position_b1: float
position_b2: float
category: str


class ReasoningAdapter: """ Bridge between the Finite Number Framework and a state-transition ReasoningEngine.

Expected state interface:
    state.coordinates: NumPy-compatible array with shape (n, 3)
    state.bonds: iterable of vertex-index pairs

FNF operations apply to explicitly selected positive magnitudes.
Cartesian coordinates and graph topology retain their native meaning.
"""

def __init__(
    self,
    boundary1: float = 1.0,
    boundary2: float = 2.0,
    *,
    tolerance: float = 1e-10,
    require_finite_coordinates: bool = True,
    allow_duplicate_bonds: bool = False,
) -> None:
    self._validate_positive(boundary1, "boundary1")
    self._validate_positive(boundary2, "boundary2")

    if boundary1 >= boundary2:
        raise ValueError("boundary1 must be less than boundary2")

    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and non-negative")

    self.boundary1 = float(boundary1)
    self.boundary2 = float(boundary2)
    self.tolerance = float(tolerance)
    self.require_finite_coordinates = require_finite_coordinates
    self.allow_duplicate_bonds = allow_duplicate_bonds

# ---------------------------------------------------------------
# 1. FNF logarithmic mathematics
# ---------------------------------------------------------------

@staticmethod
def _validate_positive(value: float, name: str = "magnitude") -> None:
    try:
        valid = isfinite(value) and value > 0
    except (TypeError, ValueError, OverflowError):
        valid = False

    if not valid:
        raise ValueError(
            f"{name} must be finite and strictly positive"
        )

@classmethod
def q(cls, value: float) -> float:
    """Canonical logarithmic coordinate q(x) = ln(x)."""
    cls._validate_positive(value)
    return log(value)

@classmethod
def relative_position(cls, value: float, boundary: float) -> float:
    """Boundary-relative position P_B(x) = ln(x / B)."""
    cls._validate_positive(value, "value")
    cls._validate_positive(boundary, "boundary")
    return log(value) - log(boundary)

@classmethod
def relation(cls, x: float, y: float) -> float:
    """Boundary-independent relation R(x, y) = ln(x / y)."""
    cls._validate_positive(x, "x")
    cls._validate_positive(y, "y")
    return log(x) - log(y)

@classmethod
def logarithmic_change(cls, before: float, after: float) -> float:
    """Logarithmic change ln(after / before)."""
    cls._validate_positive(before, "before")
    cls._validate_positive(after, "after")
    return log(after) - log(before)

# ---------------------------------------------------------------
# 2. Many & Few classification
# ---------------------------------------------------------------

def classify(self, value: float) -> Classification:
    """
    Classify a positive magnitude relative to two boundaries.

    inside:  value < boundary1
    middle:  boundary1 <= value <= boundary2
    outside: value > boundary2
    """
    self._validate_positive(value)

    a = self.relative_position(value, self.boundary1)
    b = self.relative_position(value, self.boundary2)

    if a < 0:
        category = "inside"
    elif b <= 0:
        category = "middle"
    else:
        category = "outside"

    return Classification(
        value=float(value),
        position_b1=a,
        position_b2=b,
        category=category,
    )

def classify_many(
    self, values: Iterable[float]
) -> Dict[str, List[float]]:
    """Partition positive magnitudes into three classification lists."""
    result = {
        "inside": [],
        "middle": [],
        "outside": [],
    }

    for value in values:
        classification = self.classify(value)
        result[classification.category].append(float(value))

    return result

# ---------------------------------------------------------------
# 3. State measurement
# ---------------------------------------------------------------

def measure(self, state: StateLike) -> Dict[str, float]:
    """
    Extract named positive measurements from a state.

    Returns bond lengths keyed by their canonical edge identifiers.
    Zero-length bonds cannot be represented logarithmically and
    therefore raise ValueError when measured.
    """
    self.validate_or_raise(state)

    coordinates = np.asarray(state.coordinates, dtype=float)
    measurements: Dict[str, float] = {}

    for a, b in self._canonical_bonds(state):
        length = float(np.linalg.norm(coordinates[a] - coordinates[b]))
        self._validate_positive(length, f"bond length ({a}, {b})")
        measurements[f"bond:{a}-{b}"] = length

    return measurements

def measure_log(self, state: StateLike) -> Dict[str, float]:
    """Return logarithmic coordinates for all measured bond lengths."""
    return {
        name: self.q(value)
        for name, value in self.measure(state).items()
    }

def measure_changes(
    self,
    before: StateLike,
    after: StateLike,
) -> Dict[str, float]:
    """
    Return logarithmic changes for bond identifiers present in both
    states. Removed and added bonds are intentionally not paired.
    """
    old = self.measure(before)
    new = self.measure(after)

    common = old.keys() & new.keys()

    return {
        name: self.logarithmic_change(old[name], new[name])
        for name in sorted(common)
    }

# ---------------------------------------------------------------
# 4. Structural validation gates
# ---------------------------------------------------------------

def validate(self, state: StateLike) -> bool:
    """Return whether the state passes the structural gate."""
    return not self.validate_state(state)

def validate_state(self, state: StateLike) -> List[GateResult]:
    """Return all detected structural validation failures."""
    errors: List[GateResult] = []

    if not hasattr(state, "coordinates"):
        return [
            GateResult(False, "structure", "Missing coordinates")
        ]

    if not hasattr(state, "bonds"):
        return [
            GateResult(False, "structure", "Missing bonds")
        ]

    try:
        coordinates = np.asarray(state.coordinates, dtype=float)
    except (TypeError, ValueError, OverflowError):
        return [
            GateResult(
                False, "coordinates", "Coordinates are not numeric"
            )
        ]

    if coordinates.ndim != 2 or coordinates.shape[1] != 3:
        errors.append(
            GateResult(
                False,
                "coordinates",
                "Coordinates must have shape (n, 3)",
            )
        )
        return errors

    if (
        self.require_finite_coordinates
        and not np.isfinite(coordinates).all()
    ):
        errors.append(
            GateResult(
                False,
                "coordinates",
                "Coordinates contain NaN or infinity",
            )
        )

    n = len(coordinates)
    seen: set[Bond] = set()

    try:
        raw_bonds = list(state.bonds)
    except TypeError:
        return errors + [
            GateResult(False, "bonds", "Bonds are not iterable")
        ]

    for raw_bond in raw_bonds:
        try:
            if len(raw_bond) != 2:
                raise ValueError("Bond must contain two indices")

            a, b = raw_bond

            # Reject non-integral values instead of silently truncating.
            if (
                isinstance(a, (bool, np.bool_))
                or isinstance(b, (bool, np.bool_))
                or not isinstance(a, (int, np.integer))
                or not isinstance(b, (int, np.integer))
            ):
                raise ValueError("Bond indices must be integers")

            a, b = int(a), int(b)

            if not (0 <= a < n and 0 <= b < n):
                errors.append(
                    GateResult(
                        False,
                        "bonds",
                        f"Out-of-range bond: ({a}, {b})",
                    )
                )
                continue

            if a == b:
                errors.append(
                    GateResult(
                        False,
                        "bonds",
                        f"Self-bond is not allowed: ({a}, {b})",
                    )
                )
                continue

            edge = (min(a, b), max(a, b))

            if (
                edge in seen
                and not self.allow_duplicate_bonds
            ):
                errors.append(
                    GateResult(
                        False,
                        "bonds",
                        f"Duplicate bond: {edge}",
                    )
                )
            seen.add(edge)

        except (TypeError, ValueError):
            errors.append(
                GateResult(
                    False, "bonds", f"Malformed bond: {raw_bond!r}"
                )
            )

    return errors

def validate_or_raise(self, state: StateLike) -> None:
    """Raise ValueError if structural validation fails."""
    failures = self.validate_state(state)

    if failures:
        details = "; ".join(
            f"{failure.gate}: {failure.message}"
            for failure in failures
        )
        raise ValueError(details)

# ---------------------------------------------------------------
# 5. Transition validation
# ---------------------------------------------------------------

def apply_action(
    self,
    state: StateLike,
    action: ActionFunction,
    *,
    invariants: Optional[List[InvariantFunction]] = None,
    preserve_measurements: bool = False,
) -> TransitionResult:
    """
    Apply an action to an isolated state and validate its output.

    Optional invariants must hold before and after the action.
    If preserve_measurements=True, every named measurement shared
    by both states must remain unchanged within the configured
    absolute tolerance.

    The action is expected to return a new state. This method
    clones the input when its clone() method is available.
    """
    try:
        self.validate_or_raise(state)

        before_measurements = (
            self.measure(state) if preserve_measurements else {}
        )

        checks = invariants or []

        for index, invariant in enumerate(checks):
            if not invariant(state):
                return TransitionResult(
                    False,
                    None,
                    (f"Precondition invariant {index} failed",),
                )

        source = (
            state.clone()
            if callable(getattr(state, "clone", None))
            else state
        )

        candidate = action(source)

        if candidate is None:
            return TransitionResult(
                False, None, ("Action returned no state",)
            )

        self.validate_or_raise(candidate)

        for index, invariant in enumerate(checks):
            if not invariant(candidate):
                return TransitionResult(
                    False,
                    None,
                    (f"Postcondition invariant {index} failed",),
                )

        if preserve_measurements:
            after_measurements = self.measure(candidate)

            for name in before_measurements.keys() & after_measurements.keys():
                old = before_measurements[name]
                new = after_measurements[name]

                if abs(old - new) > self.tolerance:
                    return TransitionResult(
                        False,
                        None,
                        (f"Preserved measurement changed: {name}",),
                    )

        return TransitionResult(True, candidate, ())

    except (ValueError, TypeError, IndexError, OverflowError) as exc:
        return TransitionResult(False, None, (str(exc),))

# ---------------------------------------------------------------
# 6. State key for search
# ---------------------------------------------------------------

def state_key(self, state: StateLike) -> tuple:
    """
    Build a deterministic exact-coordinate state key.

    This does not identify states that differ only by rigid motion.
    Such equivalence requires a separately defined canonicalizer.
    """
    self.validate_or_raise(state)

    coordinates = np.asarray(state.coordinates, dtype=float)

    # Normalize signed zero, since -0.0 and 0.0 are numerically equal.
    coordinates = coordinates.copy()
    coordinates[coordinates == 0.0] = 0.0

    coordinate_key = tuple(
        tuple(float(value) for value in row)
        for row in coordinates
    )

    bond_key = tuple(sorted(self._canonical_bonds(state)))

    return coordinate_key, bond_key

@staticmethod
def _canonical_bonds(state: StateLike) -> List[Bond]:
    """Canonicalize undirected edges without silently removing duplicates."""
    result = []

    for a, b in state.bonds:
        a, b = int(a), int(b)
        result.append((min(a, b), max(a, b)))

    return sorted(result)
