Transformation Bridge — Finite Number Framework

Companion to README.md, C_of_S.md, All_Things.md, decomposition_bridge.md, and composition_bridge.md.

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa

1. Purpose

The Transformation Bridge defines how changes to magnitudes, logarithmic coordinates, and boundaries are represented and evaluated within the Finite Number Framework.

Its purpose is to connect:

Transformations of positive magnitudes.
Induced transformations of logarithmic coordinates.
Changes of reference boundary and coordinate frame.
Preservation or alteration of relational invariants.
Changes in Many & Few classification.
Transformation verification through the framework's gates.

The bridge distinguishes a transformation of the underlying magnitudes from a change of coordinate frame. These operations may have different mathematical consequences.

2. Mathematical Setup

Let

Ω
=
𝑅
>
0

and define the canonical logarithmic coordinate

𝑞
(
𝑥
)
=
ln
⁡
𝑥
.

For a positive boundary 
𝐵
, define

𝑃
𝐵
(
𝑥
)
=
ln
⁡
(
𝑥
/
𝐵
)
.

The relation between two positive magnitudes is

𝑅
(
𝑥
,
𝑦
)
=
ln
⁡
(
𝑥
/
𝑦
)
.

A magnitude transformation is a function

𝑇
:
Ω
→
Ω
.

The transformation must return finite, strictly positive magnitudes for every input in its stated domain.

Its induced logarithmic transformation is

𝐹
𝑇
(
𝑢
)
=
ln
⁡
(
𝑇
(
𝑒
𝑢
)
)
.

Consequently,

𝑞
(
𝑇
(
𝑥
)
)
=
𝐹
𝑇
(
𝑞
(
𝑥
)
)
.

This formula expresses every valid magnitude transformation in logarithmic coordinates.

3. Transformation of Magnitudes
Definition 3.1. Magnitude transformation

A transformation 
𝑇
 maps each input magnitude 
𝑥
 to an output magnitude 
𝑇
(
𝑥
)
.

The transformed logarithmic coordinate is

𝑢
𝑇
(
𝑥
)
=
𝑞
(
𝑇
(
𝑥
)
)
.

The change in logarithmic position is

Δ
𝑇
(
𝑥
)
=
𝑞
(
𝑇
(
𝑥
)
)
−
𝑞
(
𝑥
)
.

Equivalently,

Δ
𝑇
(
𝑥
)
=
ln
⁡
𝑇
(
𝑥
)
𝑥
.

This quantity measures the change in logarithmic position produced by the transformation.

Proposition 3.2. Relation after transformation

For 
𝑥
,
𝑦
∈
Ω
,

𝑅
(
𝑇
(
𝑥
)
,
𝑇
(
𝑦
)
)
=
𝑞
(
𝑇
(
𝑥
)
)
−
𝑞
(
𝑇
(
𝑦
)
)
.

Therefore,

𝑅
(
𝑇
(
𝑥
)
,
𝑇
(
𝑦
)
)
=
𝐹
𝑇
(
𝑞
(
𝑥
)
)
−
𝐹
𝑇
(
𝑞
(
𝑦
)
)
.

A transformation preserves every pairwise logarithmic relation exactly when

𝐹
𝑇
(
𝑢
)
−
𝐹
𝑇
(
𝑣
)
=
𝑢
−
𝑣

for all 
𝑢
,
𝑣
∈
𝑅
.

Equivalently, there exists a constant 
𝑐
∈
𝑅
 such that

𝐹
𝑇
(
𝑢
)
=
𝑢
+
𝑐
.

In magnitude coordinates, this is precisely the class of positive scaling transformations

𝑇
(
𝑥
)
=
𝑘
𝑥
,
𝑘
>
0
.

For such transformations,

𝑅
(
𝑇
(
𝑥
)
,
𝑇
(
𝑦
)
)
=
𝑅
(
𝑥
,
𝑦
)
.

This characterizes the transformations that preserve all pairwise logarithmic relations.

4. Scaling Transformations

Let

𝑇
𝑘
(
𝑥
)
=
𝑘
𝑥
,
𝑘
>
0.

Then

𝑞
(
𝑇
𝑘
(
𝑥
)
)
=
ln
⁡
(
𝑘
𝑥
)
=
𝑞
(
𝑥
)
+
ln
⁡
𝑘
.

Thus scaling produces a translation in logarithmic coordinates.

The relative position under a fixed boundary becomes

𝑃
𝐵
(
𝑇
𝑘
(
𝑥
)
)
=
𝑃
𝐵
(
𝑥
)
+
ln
⁡
𝑘
.

For two transformed magnitudes,

𝑅
(
𝑇
𝑘
(
𝑥
)
,
𝑇
𝑘
(
𝑦
)
)
=
𝑅
(
𝑥
,
𝑦
)
.

Therefore, positive scaling:

Preserves the ordering of magnitudes.
Translates all logarithmic coordinates by the same constant.
Preserves pairwise logarithmic relations.
May change classification if the boundaries remain fixed.
Preserves classification if the boundaries are scaled by the same factor.

If 
𝐵
1
 and 
𝐵
2
 are transformed to 
𝑘
𝐵
1
 and 
𝑘
𝐵
2
, the classification relative to those boundaries is unchanged.

5. Power Transformations

For 
𝑝
≠
0
, define

𝑇
𝑝
(
𝑥
)
=
𝑥
𝑝
.

Then

𝑞
(
𝑇
𝑝
(
𝑥
)
)
=
𝑝
 
𝑞
(
𝑥
)
.

Consequently,

𝑅
(
𝑇
𝑝
(
𝑥
)
,
𝑇
𝑝
(
𝑦
)
)
=
𝑝
 
𝑅
(
𝑥
,
𝑦
)
.

The effects depend on the value of 
𝑝
:

If 
𝑝
=
1
, the transformation is the identity.
If 
𝑝
>
0
, the transformation preserves ordering.
If 
𝑝
<
0
, the transformation reverses ordering.
If 
∣
𝑝
∣
=
1
, the absolute size of every logarithmic relation is preserved.
If 
∣
𝑝
∣
≠
1
, logarithmic distances are scaled by 
∣
𝑝
∣
.

When 
𝑝
=
−
1
,

𝑇
−
1
(
𝑥
)
=
1
/
𝑥
,

which is the framework's inversion operation.

For power transformations, transformed boundaries should be evaluated using the same transformation as the magnitudes when the goal is to preserve the original classification.

6. Inversion Transformation

Define

𝑇
i
n
v
(
𝑥
)
=
1
/
𝑥
.

Then

𝑞
(
𝑇
i
n
v
(
𝑥
)
)
=
−
𝑞
(
𝑥
)
.

For a boundary 
𝐵
,

𝑃
𝐵
(
1
/
𝑥
)
=
−
𝑃
𝐵
(
𝑥
)
−
2
ln
⁡
𝐵
.

Thus inversion is sign reversal in the canonical coordinate 
𝑞
(
𝑥
)
, and also in 
𝑃
1
(
𝑥
)
 under the normalized boundary 
𝐵
=
1
.

For a general boundary, inversion does not simply negate the boundary-relative position.

Boundary transformation under inversion

If the original boundary is 
𝐵
, transform it to

𝐵
′
=
1
/
𝐵
.

Then

𝑃
𝐵
′
(
1
/
𝑥
)
=
ln
⁡
1
/
𝑥
1
/
𝐵
=
−
ln
⁡
𝑥
𝐵
=
−
𝑃
𝐵
(
𝑥
)
.

Therefore,

𝑃
1
/
𝐵
(
1
/
𝑥
)
=
−
𝑃
𝐵
(
𝑥
)
.

This is the correct inversion rule when the magnitude and boundary are both transformed.

7. Boundary and Frame Transformations

A coordinate-frame transformation adds a constant 
𝑐
 to every logarithmic coordinate:

𝑢
′
(
𝑥
)
=
𝑢
(
𝑥
)
+
𝑐
.

To preserve relative positions, the logarithmic boundary must also change:

𝑏
′
=
𝑏
+
𝑐
.

In magnitude coordinates, this corresponds to scaling magnitudes and boundaries by 
𝑘
=
𝑒
𝑐
.

The relative position remains unchanged:

𝑢
′
(
𝑥
)
−
𝑏
′
=
𝑢
(
𝑥
)
−
𝑏
.

For two elements,

𝑢
′
(
𝑥
)
−
𝑢
′
(
𝑦
)
=
𝑢
(
𝑥
)
−
𝑢
(
𝑦
)
.

Thus a consistent frame transformation preserves both boundary-relative positions and pairwise relations.

A frame change is a coordinate operation. A magnitude transformation, by contrast, may alter the actual relations among elements.

8. Transformation of Many & Few Classification

Let 
𝐵
1
<
𝐵
2
 and define the classes

𝑆
i
n
=
{
𝑥
:
𝑚
(
𝑥
)
<
𝐵
1
}
,
𝑆
m
i
d
=
{
𝑥
:
𝐵
1
≤
𝑚
(
𝑥
)
≤
𝐵
2
}
,
𝑆
o
u
t
=
{
𝑥
:
𝑚
(
𝑥
)
>
𝐵
2
}
.

For a transformation 
𝑇
, there are two distinct classification questions.

8.1 Fixed boundaries

If the magnitudes are transformed but the boundaries remain fixed, the new classification is computed using 
𝑚
𝑇
(
𝑥
)
=
𝑇
(
𝑚
(
𝑥
)
)
.

Elements may move between classes.

8.2 Co-transformed boundaries

If the boundaries are transformed as well, the new boundaries are

𝐵
1
′
=
𝑇
(
𝐵
1
)
,
𝐵
2
′
=
𝑇
(
𝐵
2
)
.

When 
𝑇
 is strictly increasing, the order of the boundaries is preserved, and classification is unchanged under the transformed magnitudes and boundaries.

When 
𝑇
 is strictly decreasing, the order of the boundaries reverses. The transformed boundaries must be reordered before applying the three-class definition.

For a positive scaling transformation, co-transforming the magnitudes and boundaries always preserves classification.

For a strictly increasing power transformation 
𝑥
𝑝
 with 
𝑝
>
0
, co-transforming the boundaries also preserves classification.

For inversion, which reverses order, the transformed boundaries must be swapped and reordered. Under symmetric boundaries satisfying 
𝐵
1
𝐵
2
=
1
, inversion exchanges the inner and outer classes while retaining the middle class.

9. Composition of Transformations

Let 
𝑇
1
,
𝑇
2
:
Ω
→
Ω
 be valid transformations.

Their composition is

(
𝑇
2
∘
𝑇
1
)
(
𝑥
)
=
𝑇
2
(
𝑇
1
(
𝑥
)
)
.

In logarithmic coordinates,

𝐹
𝑇
2
∘
𝑇
1
=
𝐹
𝑇
2
∘
𝐹
𝑇
1
.

The order matters in general: the first transformation is applied before the second.

For positive scaling transformations,

𝑇
𝑎
(
𝑥
)
=
𝑎
𝑥
,
𝑇
𝑏
(
𝑥
)
=
𝑏
𝑥
,

their composition satisfies

𝑇
𝑏
(
𝑇
𝑎
(
𝑥
)
)
=
𝑎
𝑏
𝑥
.

The corresponding logarithmic translations add:

ln
⁡
(
𝑎
𝑏
)
=
ln
⁡
𝑎
+
ln
⁡
𝑏
.

The identity transformation leaves every magnitude unchanged. If a transformation is bijective, its inverse transformation reverses its action.

10. Transformation Gate

A transformation verification gate should check the following properties where applicable:

Domain validity: The transformation maps every allowed input to a finite positive magnitude.
Coordinate consistency: The induced logarithmic transformation agrees with 
𝑞
(
𝑇
(
𝑥
)
)
.
Relation preservation: Pairwise relations remain unchanged if preservation is claimed.
Boundary consistency: Boundaries are transformed according to the declared frame or magnitude operation.
Classification consistency: The resulting classes agree with the transformed magnitudes and boundaries.
Inversion consistency: Reciprocal transformations obey the appropriate sign and boundary rules.
Composition consistency: Sequential transformations agree with their composed function.

A transformation need not preserve every property. The gate should test the properties claimed for that transformation rather than reject all transformations that alter relations or classifications.

11. Reference Implementation
from math import isfinite, log


def validate_positive(x, name="magnitude"):
    if not isfinite(x) or x <= 0:
        raise ValueError(
            f"{name} must be finite and strictly positive"
        )


def q(x):
    validate_positive(x)
    return log(x)


def relative_position(x, B):
    validate_positive(x, "x")
    validate_positive(B, "B")
    return log(x) - log(B)


def transformed_position(x, transform):
    validate_positive(x, "x")

    result = transform(x)
    validate_positive(result, "transformed magnitude")

    return log(result)


def relation(x, y):
    validate_positive(x, "x")
    validate_positive(y, "y")

    return log(x) - log(y)


def verify_relation_preservation(
    values, transform, tolerance=1e-10
):
    for x in values:
        validate_positive(x, "input magnitude")

    transformed = []

    for x in values:
        result = transform(x)
        validate_positive(result, "transformed magnitude")
        transformed.append(result)

    for i, x in enumerate(values):
        for j, y in enumerate(values):
            original = relation(x, y)
            changed = relation(transformed[i], transformed[j])

            if abs(original - changed) > tolerance:
                return False

    return True


This implementation checks pairwise relation preservation for a finite collection. Passing the check establishes approximate preservation for the tested values, not a proof that a transformation preserves all relations over its entire mathematical domain.

12. Scope and Limitations

The Transformation Bridge establishes a common language for magnitude transformations and their induced logarithmic effects.

It does not independently establish:

That all transformations preserve pairwise relations.
That every transformation preserves Many & Few classification.
That zero and infinity form a single topological point.
That an arbitrary transformation is invertible.
That global conservation follows from transformation invariance.

Every transformation must be specified by its domain, codomain, and action. Any claimed invariant must be identified and proved under the relevant assumptions.

13. Summary

The Transformation Bridge connects transformations in magnitude space to their effects in logarithmic coordinates.

Its central identities are

𝑞
(
𝑇
(
𝑥
)
)
=
𝐹
𝑇
(
𝑞
(
𝑥
)
)
,
Δ
𝑇
(
𝑥
)
=
ln
⁡
𝑇
(
𝑥
)
𝑥
,
𝑅
(
𝑇
(
𝑥
)
,
𝑇
(
𝑦
)
)
=
𝐹
𝑇
(
𝑞
(
𝑥
)
)
−
𝐹
𝑇
(
𝑞
(
𝑦
)
)
,

and, for positive scaling,

𝑞
(
𝑘
𝑥
)
=
𝑞
(
𝑥
)
+
ln
⁡
𝑘
.

These identities distinguish transformations that preserve relations from those that change them, and distinguish consistent frame changes from changes to the underlying magnitudes.

Document: docs/transformation_bridge.md

Framework: Finite Number Framework

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa
