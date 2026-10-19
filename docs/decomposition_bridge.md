# Decomposition Bridge

Companion to the manuscript, proof appendix, verification notes, and theorem index.

## Purpose

The Decomposition Bridge connects the Finite Number Framework's magnitude space, logarithmic relations, C(S) classification, inversion symmetry, and balance criteria through a common mathematical structure. Its purpose is to provide a consistent interface between:

- positive magnitudes and their logarithmic coordinates,
- relative positions and boundary-independent relations,
- the three-class partition defined by C(S),
- inversion symmetry and reciprocal pairing,
- balance criteria evaluated by explicit framework gates.

The bridge distinguishes identities that follow from ordinary analysis from additional axioms or interpretive assumptions that belong specifically to the framework.

## 1. Mathematical setup

Let S be a set equipped with a positive magnitude function

m : S → (0, ∞).

Define the logarithmic coordinate of each element x ∈ S by

u(x) = ln(m(x)).

For any positive reference boundary B, define the relative position

P_B(x) = ln(m(x)/B).

Equivalently,

P_B(x) = u(x) - ln(B).

Let the two positive boundaries satisfy

0 < B1 < B2 < ∞.

Their logarithmic coordinates are

b1 = ln(B1),
b2 = ln(B2),

so that b1 < b2.

All logarithmic operations in this specification assume finite, strictly positive magnitudes and boundaries.

## 2. Bridge architecture

The bridge consists of five conceptual layers.

### Layer 1: Magnitude space

The input consists of elements x ∈ S and their magnitudes m(x).

### Layer 2: Logarithmic coordinates

Each magnitude is mapped to the real line by u(x) = ln(m(x)). Multiplication becomes addition:

ln(ab) = ln(a) + ln(b).

Reciprocals reverse the sign:

ln(1/a) = -ln(a).

### Layer 3: Relational decomposition

The relative position with respect to a boundary is

P_B(x) = u(x) - ln(B).

The relation between two elements is

R(x, y) = u(x) - u(y) = ln(m(x)/m(y)).

The reference boundary cancels. This yields the boundary-independent relation

R(x, y) = P_B(x) - P_B(y).

### Layer 4: Classification

The classification function C(S) partitions the set into three classes by the two boundaries. The induced decomposition is:

- inside B1 when P_{B1}(x) < 0,
- between B1 and B2 when P_{B1}(x) ≥ 0 and P_{B2}(x) ≤ 0,
- outside B2 when P_{B2}(x) > 0.

### Layer 5: Gate evaluation

The framework evaluates relational invariance, inversion behavior, classification integrity, and explicitly defined balance criteria. Passing one gate does not automatically establish the validity of another gate.

## 3. Decomposition theorem

Define the three subsets

S_in = {x ∈ S : u(x) < b1},
S_mid = {x ∈ S : b1 ≤ u(x) ≤ b2},
S_out = {x ∈ S : u(x) > b2}.

Then

S = S_in ⊔ S_mid ⊔ S_out,

where ⊔ denotes disjoint union.

Proof.
For every x ∈ S, the real number u(x) satisfies exactly one of the following mutually exclusive and collectively exhaustive conditions:

- u(x) < b1,
- b1 ≤ u(x) ≤ b2,
- u(x) > b2.

Therefore x lies in exactly one of the three classes, and the union of the classes is S.
QED.

The induced classification is

C(S) = (S_in, S_mid, S_out).

The decomposition is explicit and preserves element identity. The class labels alone do not preserve exact magnitudes or logarithmic coordinates.

## 4. Relational invariance

For any x, y ∈ S and any positive boundary B,

P_B(x) - P_B(y) = ln(m(x)/m(y)) = R(x, y).

Hence the relation between two elements is boundary-independent.

If the coordinate system is translated by a constant c, then u'(x) = u(x) + c. If the boundaries shift correspondingly to b1' = b1 + c and b2' = b2 + c, then the inequalities defining the classes are unchanged. Thus the classification depends on relative positions, not the absolute choice of coordinate frame.

## 5. Inversion bridge

Suppose an inversion operation ι : S → S satisfies

m(ι(x)) = 1 / m(x).

Then

u(ι(x)) = -u(x).

If the logarithmic boundaries are symmetric, so that b1 = -b2, equivalently B1 B2 = 1, then inversion exchanges the inner and outer classes. In that case:

- if x ∈ S_in then ι(x) ∈ S_out,
- if x ∈ S_out then ι(x) ∈ S_in,
- if x ∈ S_mid then ι(x) ∈ S_mid.

If inversion is bijective on S, then the inner and outer classes have equal cardinality in the finite case.

## 6. Balance conditions

The term balance should be associated with an explicitly defined criterion. The following are distinct.

### 6.1 Logarithmic conservation

For a finite inversion-closed collection S, define

L(S) = Σ_{x∈S} u(x).

If inversion pairs each x with 1/x and each pair contributes u(x) + u(1/x) = 0, then L(S) = 0.

### 6.2 Class-cardinality symmetry

Under inversion closure and symmetric boundaries,

|S_in| = |S_out|.

This is a statement about cardinality, not necessarily about the sum of logarithmic coordinates.

### 6.3 Weighted balance

If a weight function w : S → ℝ is introduced, then a weighted balance criterion may be defined by

L_w(S) = Σ_{x∈S} w(x) u(x).

Any such criterion must specify the weights, summation convention, and convergence assumptions.

The balance gate should therefore report which criterion it evaluates, and it must not be treated as equivalent to another criterion without additional proof.

## 7. Gate interface

The framework's gates are responsible for distinct checks:

- C(S): construct a disjoint and exhaustive three-class partition.
- R(x, y): compute the logarithmic ratio.
- Inversion gate: verify reciprocal mapping and sign reversal.
- Partition gate: verify disjointness and coverage.
- Balance gate: evaluate the selected balance criterion.

A successful partition check establishes classification integrity only; it does not by itself establish inversion closure, conservation, or topological closure.

## 8. Reference implementation

The following Python implementation provides the core decomposition and relational operations:

```python
from math import isfinite, log


def validate_positive(value, name):
    if not isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and strictly positive")


def relative_position(magnitude, boundary):
    validate_positive(magnitude, "magnitude")
    validate_positive(boundary, "boundary")
    return log(magnitude) - log(boundary)


def relation(magnitude_x, magnitude_y):
    validate_positive(magnitude_x, "magnitude_x")
    validate_positive(magnitude_y, "magnitude_y")
    return log(magnitude_x) - log(magnitude_y)


def decompose(S, magnitude, B1, B2):
    validate_positive(B1, "B1")
    validate_positive(B2, "B2")
    if B1 >= B2:
        raise ValueError("Boundaries must satisfy B1 < B2")

    b1 = log(B1)
    b2 = log(B2)

    inside = []
    middle = []
    outside = []

    for x in S:
        value = magnitude(x)
        validate_positive(value, f"magnitude({x!r})")
        position = log(value)

        if position < b1:
            inside.append(x)
        elif position <= b2:
            middle.append(x)
        else:
            outside.append(x)

    return {"inside": inside, "middle": middle, "outside": outside}
```

This implementation retains the original elements in their classes and uses logarithmic comparisons to perform the decomposition.

## 9. Example

Let

S = {1/4, 1/2, 1, 2, 4},
B1 = 1/2,
B2 = 2,

with m(x) = x. The logarithmic boundaries are

b1 = ln(1/2),
b2 = ln(2),

and the log-values are

ln(1/4), ln(1/2), ln(1), ln(2), ln(4).

Then the set decomposes into:

- inside B1: {1/4},
- middle: {1/2, 1, 2},
- outside B2: {4}.

This is consistent with the logarithmic ordering induced by the boundaries.

## 10. Summary

The decomposition bridge encodes the core structure of the framework:

- positive magnitudes map into logarithmic coordinates,
- boundaries define a signed position on the log-line,
- relative comparisons are invariant under boundary change,
- inversion acts by sign reversal,
- and the classification C(S) is a three-way partition induced by two boundaries.

This makes the framework formally coherent as a relational algebraic system, while keeping the interpretive and philosophical claims clearly separated from the verified identities.
