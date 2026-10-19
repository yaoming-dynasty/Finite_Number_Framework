# Formal Proof Appendix

## Introduction

This appendix gives a compact but formal set of lemmas and proofs for the Finite Number Framework. The goal is to make the framework auditable as a mathematical structure rather than merely interpretive.

Let Ω = ℝ_{>0}, and define the canonical logarithmic coordinate

q(x) := ln(x),

and for each boundary B > 0,

P_B(x) := ln(x/B).

The framework makes five core claims:

1. multiplication in Ω becomes addition under q,
2. inversion becomes negation under q,
3. boundary shifts act by translation on P_B,
4. relative comparisons are boundary-invariant,
5. inversion-closed systems cancel in reciprocal pairs.

## Lemma 1. Multiplication becomes addition.

For all x, y ∈ Ω,

q(xy) = q(x) + q(y).

Proof.
q(xy) = ln(xy) = ln(x) + ln(y) = q(x) + q(y).
QED.

## Lemma 2. Division becomes subtraction.

For all x, y ∈ Ω,

q(x/y) = q(x) - q(y).

Proof.
q(x/y) = ln(x/y) = ln(x) - ln(y) = q(x) - q(y).
QED.

## Lemma 3. Inversion negates the logarithmic coordinate.

For all x ∈ Ω,

q(1/x) = -q(x).

Proof.
q(1/x) = ln(1/x) = -ln(x) = -q(x).
QED.

## Proposition 4. Boundary changes act by translation.

For all x, B, B' ∈ Ω,

P_{B'}(x) = P_B(x) + ln(B / B').

Proof.
P_{B'}(x) = ln(x/B') = ln(x/B) + ln(B/B') = P_B(x) + ln(B/B').
QED.

## Proposition 5. Relative positions are boundary-invariant.

For all x, y, B ∈ Ω,

P_B(x) - P_B(y) = ln(x / y).

Proof.
P_B(x) - P_B(y) = ln(x/B) - ln(y/B) = ln((x/B)/(y/B)) = ln(x / y).
QED.

## Corollary 6. Relative comparison is independent of the boundary.

For all x, y ∈ Ω and all boundaries B, B' > 0,

P_B(x) - P_B(y) = P_{B'}(x) - P_{B'}(y).

Proof.
By Proposition 5,

P_B(x) - P_B(y) = ln(x/y) = P_{B'}(x) - P_{B'}(y).
QED.

## Proposition 7. Inversion under a normalized boundary.

If B = 1, then for all x ∈ Ω,

P_1(1/x) = -P_1(x).

Proof.
P_1(x) = ln(x). Therefore P_1(1/x) = ln(1/x) = -ln(x) = -P_1(x).
QED.

## Proposition 8. Inversion swaps inside and outside.

For all x ∈ Ω and normalized boundary B = 1,

P_1(x) < 0 iff P_1(1/x) > 0.

Proof.
P_1(1/x) = -P_1(x). The sign reverses.
QED.

## Definition 9. Inversion-closed set.

A set S ⊆ Ω is inversion-closed if x ∈ S implies 1/x ∈ S.

## Proposition 10. Pairwise cancellation in inversion-closed sets.

Let S be inversion-closed and finite. Then for every pair x and 1/x in S,

q(x) + q(1/x) = 0.

Proof.
By Lemma 3, q(1/x) = -q(x). So q(x) + q(1/x) = q(x) - q(x) = 0.
QED.

## Corollary 11. Total cancellation over inversion-closed finite sets.

If S is inversion-closed and finite, then the sum of q-values over pairs (x, 1/x) is zero.

Proof.
Partition S into inverse pairs. Each pair sums to zero by Proposition 10; the total sum is therefore zero.
QED.

## Definition 12. Two-boundary classification.

Let 0 < B1 < B2 and S ⊆ Ω. For each x ∈ S, define a(x) = P_{B1}(x) and b(x) = P_{B2}(x). Then x is classified by:

- inside B1 if a(x) < 0,
- between B1 and B2 if a(x) ≥ 0 and b(x) ≤ 0,
- outside B2 if b(x) > 0.

This classification is denoted C_{B1,B2}(S).

## Proposition 13. The two-boundary classification is a partition.

For every S ⊆ Ω and every B1 < B2, the classes induced by C_{B1,B2}(S) are mutually exclusive and exhaustive.

Proof.
For each x ∈ S, exactly one of the three conditions above holds. These conditions are disjoint and cover all possibilities.
QED.

## Definition 14. Many & Few.

Many&Few(S; B1, B2) := (S, C_{B1,B2}(S)).

## Proposition 15. The logarithmic map is a group isomorphism.

The map q : Ω → ℝ defined by q(x) = ln(x) is a group isomorphism from (Ω, ×) to (ℝ, +).

Proof.
By Lemma 1, q(xy) = q(x) + q(y), so q preserves multiplication as addition. By Lemma 3, q(1/x) = -q(x), so inversion corresponds to negation. The map is bijective because ln : ℝ_{>0} → ℝ is a bijection. Therefore q is a group isomorphism.
QED.

## Summary of the formal core

The essential mathematical content of the framework is captured by the identities:

1. q(xy) = q(x) + q(y)
2. q(1/x) = -q(x)
3. P_{B'}(x) = P_B(x) + ln(B/B')
4. P_B(x) - P_B(y) = ln(x/y)
5. q(x) + q(1/x) = 0 for inverse pairs
6. C_{B1,B2}(S) is a valid partition induced by two boundaries

These identities make the framework formally testable and provide the basis for its algebraic and geometric interpretation.
