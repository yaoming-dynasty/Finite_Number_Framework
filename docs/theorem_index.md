# Theorem Numbering and Index Appendix

## Purpose

This appendix provides a compact numbering scheme for the formal results in the Finite Number Framework. Its purpose is to make the structure of the manuscript easier to reference and to provide a stable index for theorems, propositions, lemmas, corollaries, definitions, and axioms.

The framework is organized around the canonical logarithmic coordinate and the boundary-relative position. The numbering below follows the convention that:

- Axioms are labeled A1, A2, ...
- Definitions are labeled D1, D2, ...
- Lemmas are labeled L1, L2, ...
- Propositions are labeled P1, P2, ...
- Corollaries are labeled C1, C2, ...
- Theorems are labeled T1, T2, ...

---

## 1. Core Definitions and Notation

### D1. Positive magnitude domain

Ω = ℝ_{>0}

### D2. Canonical logarithmic coordinate

q(x) := ln(x)

### D3. Boundary-relative position

P_B(x) := ln(x / B)

### D4. Relative relation

R(x, y) := ln(x / y)

### D5. Inversion

Inv(x) := 1/x

### D6. Inversion-closed set

A set S ⊆ Ω is inversion-closed if x ∈ S implies 1/x ∈ S.

### D7. Two-boundary classification

Given boundaries 0 < B1 < B2 and set S ⊆ Ω, the classification C_{B1,B2}(S) is defined by:

- inside B1 if P_{B1}(x) < 0
- between B1 and B2 if P_{B1}(x) ≥ 0 and P_{B2}(x) ≤ 0
- outside B2 if P_{B2}(x) > 0

### D8. Many & Few

Many&Few(S; B1, B2) := (S, C_{B1,B2}(S))

---

## 2. Axioms

### A1. Positive magnitude domain

All magnitudes lie in Ω = ℝ_{>0}.

### A2. Logarithmic representation

Every magnitude x is represented by q(x) = ln(x).

### A3. Boundary-relative representation

Every magnitude x relative to a boundary B is represented by P_B(x) = ln(x/B).

### A4. Inversion symmetry

For all x ∈ Ω, q(1/x) = -q(x).

### A5. Relative comparison invariance

For all x, y ∈ Ω, q(x/y) = q(x) - q(y).

### A6. Boundary translation

For all x, B, B' ∈ Ω, P_{B'}(x) = P_B(x) + ln(B/B').

### A7. Inversion closure

A system of interest may be closed under inversion, so that x ∈ S implies 1/x ∈ S.

---

## 3. Lemmas

### L1. Multiplication becomes addition

For all x, y ∈ Ω,

q(xy) = q(x) + q(y).

### L2. Division becomes subtraction

For all x, y ∈ Ω,

q(x/y) = q(x) - q(y).

### L3. Inversion negates the logarithmic coordinate

For all x ∈ Ω,

q(1/x) = -q(x).

### L4. Boundary change is translation

For all x, B, B' ∈ Ω,

P_{B'}(x) = P_B(x) + ln(B/B').

### L5. Relative position is boundary-independent

For all x, y, B ∈ Ω,

P_B(x) - P_B(y) = ln(x/y).

---

## 4. Propositions

### P1. Boundary translation law

For all x, B, B' ∈ Ω,

P_{B'}(x) = P_B(x) + ln(B/B').

### P2. Relative positions are invariant under boundary choice

For all x, y, B, B' ∈ Ω,

P_B(x) - P_B(y) = P_{B'}(x) - P_{B'}(y).

### P3. Inversion under a normalized boundary

If B = 1, then for all x ∈ Ω,

P_1(1/x) = -P_1(x).

### P4. Inversion swaps inside and outside

If B = 1, then for all x ∈ Ω,

P_1(x) < 0 iff P_1(1/x) > 0.

### P5. Pairwise cancellation

If S is inversion-closed and finite, then for all pairs x and 1/x ∈ S,

q(x) + q(1/x) = 0.

### P6. Two-boundary classification is a partition

For every S ⊆ Ω and boundaries 0 < B1 < B2, the classes induced by C_{B1,B2}(S) are mutually exclusive and exhaustive.

### P7. Many & Few is invariant up to boundary translation

Classification under a pair of boundaries differs from classification under another pair only by a translation of the coordinate system.

### P8. The logarithmic map is a group isomorphism

The map q : Ω → ℝ is a group isomorphism from (Ω, ×) to (ℝ, +).

---

## 5. Corollaries

### C1. Boundary-free relative comparison

For all x, y ∈ Ω and any boundary B > 0,

ln(x/y) = P_B(x) - P_B(y).

### C2. Inverse pairs cancel

For any inversion pair x and 1/x,

q(x) + q(1/x) = 0.

### C3. Total sum over paired inversion-closed sets is zero

If S is finite and inversion-closed, then

Σ_{x∈S} q(x) = 0

when grouped by inverse pairs.

---

## 6. Theorems

### T1. Boundary translations preserve relative structure

For all x, B, B' ∈ Ω,

P_{B'}(x) = P_B(x) + ln(B/B').

### T2. Relative structure is independent of the chosen boundary

For all x, y, B, B' ∈ Ω,

P_B(x) - P_B(y) = P_{B'}(x) - P_{B'}(y).

### T3. Inversion is reflection on the logarithmic line

For a normalized boundary B = 1,

P_1(1/x) = -P_1(x).

### T4. Inversion-closed systems admit pairwise cancellation

If S is inversion-closed and finite, then its paired sum under the logarithmic coordinate is zero.

### T5. The two-boundary classification is well-defined

For all S and all B1 < B2, the induced classification C_{B1,B2}(S) is a valid partition of S.

### T6. The logarithmic coordinate embodies the algebraic structure

The map q : Ω → ℝ is an isomorphism between the multiplicative structure of positive magnitudes and the additive structure of the real line.

---

## 7. Index of Main Results by Concept

### Boundary and position

- D3, A3, P1, P2, T1, T2

### Inversion

- D5, A4, L3, P3, P4, T3

### Cancellation

- D6, A7, P5, C2, C3, T4

### Many & Few

- D7, D8, P6, P7, T5

### Algebraic structure

- D2, A2, L1, L2, P8, T6

---

## 8. Recommended Cross-References

- Use D3 in conjunction with A3 and P1.
- Use D5 with A4 and P3.
- Use D6 with P5 and T4.
- Use D7 and D8 with P6 and T5.
- Use D2 and P8 for the algebraic backbone of the framework.

---

## 9. Closing Note

This numbering scheme is intended to make the framework easier to reference and easier to evaluate as a formal mathematical theory. Any future extension of the framework should maintain consistency with this numbering system and use the same convention for cross-references.
