Composition Bridge — Finite Number Framework

Companion to README.md, C_of_S.md, All_Things.md, and decomposition_bridge.md.

Authors: Christopher Thomas Ronio, Jeremey James Grice-Rosa

1. Purpose

The Composition Bridge defines how positive magnitudes and their logarithmic relations combine into larger mathematical structures within the Finite Number Framework.

Its purpose is to connect:

Individual magnitudes and their compositions.
Multiplicative operations and additive logarithmic coordinates.
Pairwise relations and composed relations.
Element-level operations and set-level constructions.
Composition rules and the framework's decomposition and balance gates.

The bridge uses classical real arithmetic and logarithmic identities. It distinguishes identities that follow mathematically from additional conditions imposed by the framework.

2. Mathematical Setup

Let

Ω
=
𝑅
>
0

be the domain of finite positive magnitudes.

Define the canonical logarithmic coordinate

𝑞
:
Ω
→
𝑅
,
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
, define the relative position

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
=
𝑞
(
𝑥
)
−
𝑞
(
𝐵
)
.

For two positive magnitudes 
𝑥
,
𝑦
, define their logarithmic relation by

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
=
𝑞
(
𝑥
)
−
𝑞
(
𝑦
)
.

The Composition Bridge treats multiplication as the primary composition operation on positive magnitudes.

3. Composition of Magnitudes
Definition 3.1. Binary composition

For 
𝑥
,
𝑦
∈
Ω
, define

𝑥
∘
𝑦
:
=
𝑥
𝑦
.

Since 
𝑥
>
0
 and 
𝑦
>
0
, their product is also positive:

𝑥
∘
𝑦
∈
Ω
.
Proposition 3.2. Composition becomes addition

For all 
𝑥
,
𝑦
∈
Ω
,

𝑞
(
𝑥
𝑦
)
=
𝑞
(
𝑥
)
+
𝑞
(
𝑦
)
.

Proof.

By the logarithm product identity,

ln
⁡
(
𝑥
𝑦
)
=
ln
⁡
𝑥
+
ln
⁡
𝑦
.

Therefore,

𝑞
(
𝑥
∘
𝑦
)
=
𝑞
(
𝑥
)
+
𝑞
(
𝑦
)
.

□

This identity establishes the central composition rule: multiplication in magnitude space corresponds to addition in logarithmic coordinate space.

Proposition 3.3. Composition is associative

For all 
𝑥
,
𝑦
,
𝑧
∈
Ω
,

(
𝑥
𝑦
)
𝑧
=
𝑥
(
𝑦
𝑧
)
.

Consequently,

𝑞
(
(
𝑥
𝑦
)
𝑧
)
=
𝑞
(
𝑥
)
+
𝑞
(
𝑦
)
+
𝑞
(
𝑧
)
.

The logarithmic representation is independent of the grouping of a finite product.

Proposition 3.4. Identity and inverse

The identity magnitude is 
1
, since

𝑥
⋅
1
=
𝑥
.

Its logarithmic coordinate is

𝑞
(
1
)
=
0.

Every 
𝑥
∈
Ω
 has a multiplicative inverse 
1
/
𝑥
, satisfying

𝑥
⋅
1
𝑥
=
1

and

𝑞
(
1
/
𝑥
)
=
−
𝑞
(
𝑥
)
.

Thus reciprocal composition cancels in logarithmic coordinates.

4. Composition Relative to a Boundary

The boundary-relative position of a product satisfies

𝑃
𝐵
(
𝑥
𝑦
)
	
=
ln
⁡
(
𝑥
𝑦
/
𝐵
)


	
=
ln
⁡
𝑥
+
ln
⁡
𝑦
−
ln
⁡
𝐵


	
=
𝑃
𝐵
(
𝑥
)
+
𝑃
𝐵
(
𝑦
)
+
ln
⁡
𝐵
.

Therefore,

𝑃
𝐵
(
𝑥
𝑦
)
=
𝑃
𝐵
(
𝑥
)
+
𝑃
𝐵
(
𝑦
)
+
𝑞
(
𝐵
)
.

When the boundary is normalized to 
𝐵
=
1
, this simplifies to

𝑃
1
(
𝑥
𝑦
)
=
𝑃
1
(
𝑥
)
+
𝑃
1
(
𝑦
)
.

This distinction matters: boundary-relative positions do not generally compose by simple addition unless the reference boundary is normalized or the coordinate convention is adjusted.

For any fixed boundary, the pairwise relation remains independent of that boundary:

𝑅
(
𝑥
,
𝑦
)
=
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
.
5. Composition of Relations

For 
𝑥
,
𝑦
,
𝑧
∈
Ω
, logarithmic relations satisfy

𝑅
(
𝑥
,
𝑦
)
+
𝑅
(
𝑦
,
𝑧
)
=
𝑅
(
𝑥
,
𝑧
)
.

Proof.

𝑅
(
𝑥
,
𝑦
)
+
𝑅
(
𝑦
,
𝑧
)
	
=
ln
⁡
(
𝑥
/
𝑦
)
+
ln
⁡
(
𝑦
/
𝑧
)


	
=
ln
⁡
(
𝑥
/
𝑧
)


	
=
𝑅
(
𝑥
,
𝑧
)
.

□

This property provides a composition rule for relational paths. The intermediate magnitude cancels, leaving the direct relation between the endpoints.

Additional identities include

𝑅
(
𝑥
,
𝑦
)
=
−
𝑅
(
𝑦
,
𝑥
)

and

𝑅
(
𝑥
,
𝑥
)
=
0.

The relational structure is therefore additive along paths, antisymmetric under reversal, and neutral on a path from an element to itself.

6. Composition of Collections

Let 
𝐴
 be a finite indexed collection of positive magnitudes,

𝐴
=
(
𝑥
1
,
…
,
𝑥
𝑛
)
.

Define its product composition by

Π
(
𝐴
)
=
∏
𝑖
=
1
𝑛
𝑥
𝑖
.

For a nonempty finite collection,

𝑞
(
Π
(
𝐴
)
)
=
∑
𝑖
=
1
𝑛
𝑞
(
𝑥
𝑖
)
.

For the empty collection, adopt the conventional empty-product identity

Π
(
∅
)
=
1
,

with logarithmic coordinate 
𝑞
(
1
)
=
0
.

The indexed-collection convention preserves multiplicity. If an ordinary set is used instead, repeated values are represented only once. Any framework operation that depends on repeated contributions must explicitly specify whether it operates on sets, multisets, or indexed collections.

For two finite indexed collections 
𝐴
 and 
𝐷
, concatenation satisfies

Π
(
𝐴
∥
𝐷
)
=
Π
(
𝐴
)
Π
(
𝐷
)

and

𝑞
(
Π
(
𝐴
∥
𝐷
)
)
=
𝑞
(
Π
(
𝐴
)
)
+
𝑞
(
Π
(
𝐷
)
)
.

These formulas describe finite composition. Infinite products and sums require additional convergence conditions.

7. Composition and Inversion

Define the inversion operation

𝜄
(
𝑥
)
=
1
/
𝑥
.

Then

𝜄
(
𝑥
𝑦
)
=
𝜄
(
𝑥
)
𝜄
(
𝑦
)

and

𝑞
(
𝜄
(
𝑥
𝑦
)
)
=
−
𝑞
(
𝑥
)
−
𝑞
(
𝑦
)
.

For finite products,

(
∏
𝑖
=
1
𝑛
𝑥
𝑖
)
−
1
=
∏
𝑖
=
1
𝑛
1
𝑥
𝑖
.

Consequently, if a finite indexed collection is closed under inversion with matching multiplicities, its logarithmic contributions cancel:
