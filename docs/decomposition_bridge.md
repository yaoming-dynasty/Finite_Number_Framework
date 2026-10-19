Decomposition Bridge — Finite Number Framework

Companion to README.md, C_of_S.md, All_Things.md, and the Gate Specifications.

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa

1. Purpose

The Decomposition Bridge connects the Finite Number Framework's magnitude space, logarithmic relations, C(S) classification, inversion symmetry, and balance gates through a common mathematical structure.

Its purpose is to provide a consistent interface between:

Positive magnitudes and their logarithmic coordinates.
Relative positions and boundary-independent relations.
The three-class partition defined by C(S).
Inversion symmetry and reciprocal pairing.
Balance criteria evaluated by the framework's gates.

The bridge distinguishes mathematical identities derived from classical mathematics from additional axioms that the framework may impose.

2. Mathematical Setup

Let 
𝑆
 be a set equipped with a magnitude function

𝑚
:
𝑆
→
(
0
,
∞
)
.

Define the logarithmic coordinate of each element by

𝑢
(
𝑥
)
=
ln
⁡
𝑚
(
𝑥
)
.

For any positive reference boundary 
𝐵
, define the relative position

𝑃
𝐵
(
𝑥
)
=
ln
⁡
𝑚
(
𝑥
)
𝐵
.

Equivalently, in logarithmic boundary coordinates,

𝑃
𝐵
(
𝑥
)
=
𝑢
(
𝑥
)
−
ln
⁡
𝐵
.

Let the two positive magnitude boundaries satisfy

0
<
𝐵
1
<
𝐵
2
<
∞
.

Their logarithmic coordinates are

𝑏
1
=
ln
⁡
𝐵
1
,
𝑏
2
=
ln
⁡
𝐵
2
,

so that 
𝑏
1
<
𝑏
2
.

All logarithmic operations in this specification assume finite, strictly positive magnitudes and boundaries.

3. Bridge Architecture

The bridge consists of five conceptual layers.

Layer 1 — Magnitude Space

The input consists of elements 
𝑥
∈
𝑆
 and their positive magnitudes 
𝑚
(
𝑥
)
.

Layer 2 — Logarithmic Coordinates

Each magnitude is mapped to the real line:

𝑢
(
𝑥
)
=
ln
⁡
𝑚
(
𝑥
)
.

Multiplication of magnitudes becomes addition of logarithmic coordinates:

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

Reciprocal magnitudes reverse the sign of the coordinate:

ln
⁡
(
1
/
𝑎
)
=
−
ln
⁡
𝑎
.
Layer 3 — Relational Decomposition

The relative position with respect to a boundary is

𝑃
𝐵
(
𝑥
)
=
𝑢
(
𝑥
)
−
ln
⁡
𝐵
.

The relation between two elements is

𝑅
(
𝑥
,
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
=
ln
⁡
𝑚
(
𝑥
)
𝑚
(
𝑦
)
.

The reference boundary cancels from this expression.

Layer 4 — Classification

The C(S) function partitions the original set into three classes according to the two logarithmic boundaries.

Layer 5 — Gate Evaluation

The framework evaluates relational invariance, inversion properties, classification integrity, and explicitly defined balance conditions.

Each gate evaluates a distinct property. Passing one gate does not automatically establish the properties tested by another.

4. Decomposition Theorem

Define the three subsets

𝑆
i
n
=
{
𝑥
∈
𝑆
:
𝑢
(
𝑥
)
<
𝑏
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
∈
𝑆
:
𝑏
1
≤
𝑢
(
𝑥
)
≤
𝑏
2
}
,

and

𝑆
o
u
t
=
{
𝑥
∈
𝑆
:
𝑢
(
𝑥
)
>
𝑏
2
}
.

Then

𝑆
=
𝑆
i
n
  
∪
˙
  
𝑆
m
i
d
  
∪
˙
  
𝑆
o
u
t

where 
∪
˙
 denotes disjoint union.

Proof

For every 
𝑥
∈
𝑆
, the real number 
𝑢
(
𝑥
)
 satisfies exactly one of the following conditions:

𝑢
(
𝑥
)
<
𝑏
1
.
𝑏
1
≤
𝑢
(
𝑥
)
≤
𝑏
2
.
𝑢
(
𝑥
)
>
𝑏
2
.

These conditions are mutually exclusive and collectively exhaustive. Therefore, the three preimages are pairwise disjoint and their union is 
𝑆
. Any of the classes may be empty. 
□

The classification function is consequently

𝐶
(
𝑆
)
=
(
𝑆
i
n
,
𝑆
m
i
d
,
𝑆
o
u
t
)
.

The decomposition preserves element identity when the original elements are retained. The class labels alone do not preserve exact magnitudes or logarithmic coordinates.

5. Relational Invariance

For any 
𝑥
,
𝑦
∈
𝑆
 and any positive reference boundary 
𝐵
,

𝑃
𝐵
(
𝑥
)
−
𝑃
𝐵
(
𝑦
)
	
=
ln
⁡
𝑚
(
𝑥
)
𝐵
−
ln
⁡
𝑚
(
𝑦
)
𝐵


	
=
ln
⁡
𝑚
(
𝑥
)
𝑚
(
𝑦
)


	
=
𝑅
(
𝑥
,
𝑦
)
.

Therefore,

𝑃
𝐵
(
𝑥
)
−
𝑃
𝐵
(
𝑦
)
=
𝑅
(
𝑥
,
𝑦
)

and the relation is independent of the chosen reference boundary.

Frame Translation

Suppose a change of frame adds a constant 
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

If the boundaries transform correspondingly,

𝑏
1
′
=
𝑏
1
+
𝑐
,
𝑏
2
′
=
𝑏
2
+
𝑐
,

then every classification remains unchanged.

Indeed,

𝑢
′
(
𝑥
)
<
𝑏
1
′
  
⟺
  
𝑢
(
𝑥
)
<
𝑏
1
,

with equivalent results for the middle and outer classes.

The boundary width is invariant:

𝑏
2
′
−
𝑏
1
′
=
𝑏
2
−
𝑏
1
.

Thus the classification depends on the positions of the elements relative to the boundaries, not on the choice of translated coordinate frame.

6. Inversion Bridge

Suppose an inversion operation 
𝜄
:
𝑆
→
𝑆
 satisfies

𝑚
(
𝜄
(
𝑥
)
)
=
1
𝑚
(
𝑥
)
.

Then

𝑢
(
𝜄
(
𝑥
)
)
=
−
𝑢
(
𝑥
)
.

For inversion to exchange the inner and outer classes, the logarithmic boundaries must be symmetric:

𝑏
1
=
−
𝑏
2
.

In magnitude coordinates, this is equivalent to

𝐵
1
𝐵
2
=
1
.

Under these conditions:

If 
𝑥
∈
𝑆
i
n
, then 
𝜄
(
𝑥
)
∈
𝑆
o
u
t
.
If 
𝑥
∈
𝑆
o
u
t
, then 
𝜄
(
𝑥
)
∈
𝑆
i
n
.
If 
𝑥
∈
𝑆
m
i
d
, then 
𝜄
(
𝑥
)
∈
𝑆
m
i
d
.

If inversion is a bijection on 
𝑆
, it establishes a bijection between the inner and outer classes. Consequently,

∣
𝑆
i
n
∣
=
∣
𝑆
o
u
t
∣
.

This equality holds for finite or infinite cardinalities, provided the inversion operation and symmetric boundaries satisfy the conditions above.

7. Balance Conditions

The term balance must be associated with an explicitly defined mathematical criterion. The following conditions are distinct.

7.1 Logarithmic Conservation

For a finite collection 
𝑆
, define the logarithmic sum

𝐿
(
𝑆
)
=
∑
𝑥
∈
𝑆
𝑢
(
𝑥
)
.

If 
𝑆
 is inversion-closed, inversion is a bijection, and each element is counted once, then

𝐿
(
𝑆
)
=
0.

To see this, the elements can be grouped into reciprocal pairs. Each pair contributes

𝑢
(
𝑥
)
+
𝑢
(
𝜄
(
𝑥
)
)
=
0.

Any fixed point of inversion has 
𝑚
(
𝑥
)
=
1
, so its logarithmic coordinate is also zero.

For infinite collections, a summation convention and appropriate convergence conditions are required before the sum can be asserted to equal zero.

7.2 Class-Cardinality Symmetry

Under inversion closure and symmetric boundaries,

∣
𝑆
i
n
∣
=
∣
𝑆
o
u
t
∣
.

This is a cardinality result, not a statement about the sum of logarithmic coordinates.

For infinite sets, equality of cardinalities does not by itself establish convergence or cancellation of a sum.

7.3 Weighted Balance

If the framework uses a weight function 
𝑤
:
𝑆
→
𝑅
, it may define a weighted balance criterion such as

𝐿
𝑤
(
𝑆
)
=
∑
𝑥
∈
𝑆
𝑤
(
𝑥
)
𝑢
(
𝑥
)
.

The weights, summation convention, and required convergence properties must be specified. Inversion symmetry alone does not guarantee weighted cancellation unless the weights and summation rule are compatible with inversion.

7.4 Balance Gate

The balance gate should report which criterion it evaluates:

Logarithmic conservation.
Inner/outer cardinality symmetry.
Weighted balance.
Another explicitly defined framework axiom.

These criteria must not be treated as equivalent without a separate proof.

8. Gate Interface

The following interfaces describe the intended responsibilities of the framework's gates.

Component	Input	Responsibility
C(S)	Magnitudes and two boundaries	Construct a disjoint, exhaustive three-class partition.
R(x, y)	Two elements with positive magnitudes	Compute the logarithmic ratio.
Inversion gate	An inversion operation and its domain	Verify reciprocal mapping and sign reversal.
Partition gate	The resulting classes	Verify disjointness and coverage.
Balance gate	A collection and an explicit balance criterion	Evaluate the selected balance property.

A successful partition check establishes classification integrity only. It does not independently establish inversion closure, global conservation, or topological closure.

9. Reference Implementation

The following Python implementation provides the core decomposition and relational operations.

from math import isfinite, log


def validate_positive(value, name):
    if not isfinite(value) or value <= 0:
        raise ValueError(
            f"{name} must be finite and strictly positive"
        )


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

    return {
        "inside": inside,
        "middle": middle,
        "outside": outside,
    }


The implementation retains the original elements in their classes, assigns both boundary values to the middle class, and uses logarithmic comparisons.

For a finite input collection, the partition can be checked by verifying that every input element appears in exactly one output class. If S is a mathematical set, the implementation should preserve its set semantics when duplicate inputs are possible.

10. Example

Let

𝑆
=
{
1
4
,
1
2
,
1
,
2
,
4
}
,
𝐵
1
=
1
2
,
𝐵
2
=
2
,

with 
𝑚
(
𝑥
)
=
𝑥
.

The logarithmic boundaries are

𝑏
1
=
−
ln
⁡
2
,
𝑏
2
=
ln
⁡
2.

The decomposition is

𝑆
i
n
=
{
1
4
}
,
𝑆
m
i
d
=
{
1
2
,
1
,
2
}
,
𝑆
o
u
t
=
{
4
}
.

The reciprocal operation exchanges 
1
/
4
 with 
4
, and 
1
/
2
 with 
2
. The element 
1
 is a fixed point of inversion.

The logarithmic sum is

𝐿
(
𝑆
)
	
=
−
ln
⁡
4
−
ln
⁡
2
+
0
+
ln
⁡
2
+
ln
⁡
4


	
=
0.

This example satisfies the partition theorem, inversion symmetry, class-cardinality symmetry, and finite logarithmic conservation.

11. Scope and Limitations

The Decomposition Bridge establishes a classical mathematical structure for classifying positive magnitudes and evaluating their logarithmic relations.

It does not, by itself, establish:

That zero and infinity are a single point in a circular topology.
That every conceivable totality can be represented as a set of positive magnitudes.
That every infinite collection admits a well-defined sum.
That class-cardinality symmetry implies logarithmic conservation.
That the framework's additional axioms follow from the partition theorem.

Any extension involving topological closure, infinite aggregation, or universal totality requires its own definitions and proofs.

12. Summary

The Decomposition Bridge unifies four mathematical operations:

Coordinate mapping: Convert positive magnitudes into logarithmic positions.
Relational comparison: Evaluate ratios independently of a common reference boundary.
Classification: Partition the domain using the C(S) boundaries.
Balance evaluation: Test separately specified conservation and symmetry conditions.

The partition theorem, relational invariance, and conditional inversion results follow from classical mathematics under the stated assumptions. Stronger claims about totality and global conservation remain dependent on additional framework axioms.

Document: docs/decomposition_bridge.md

Framework: Finite Number Framework

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa
