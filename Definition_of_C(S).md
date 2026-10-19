# Definition of C(S)

Companion to the Finite Number Framework README (section 4, Many & Few).

**Authors:** Christopher Thomas Ronio, Jeremey James Grice-Rosa

---

## Context

```
{Many & Few}(S) = (S, C(S))
Many & Few = Boundary1 + Boundary2
```

The two boundaries are set **as needed** for the problem at hand. This file gives a definition of `C(S)` that uses only classical mathematics: order, preimages, and cuts of the real line.

## Setup

Let `S` be a set with a magnitude function `m: S → (0, ∞)`. The log-position of `x ∈ S` is:

```
u(x) = ln m(x) ∈ ℝ
```

The two boundaries are real numbers `b₁ < b₂` in log coordinates (multiplicatively, `B₁ = e^b₁` and `B₂ = e^b₂`).

## Cuts

Each boundary is a cut of `ℝ`. Together they split `ℝ` into three intervals:

```
I₁ = (−∞, b₁)      I₂ = [b₁, b₂]      I₃ = (b₂, +∞)
```

## Definition

```
C(S) := { u⁻¹(I₁), u⁻¹(I₂), u⁻¹(I₃) } = (S_in, S_mid, S_out)
```

Equivalently, `C(S)` is the quotient `S/~`, where `x ~ y` iff `u(x)` and `u(y)` lie in the same interval. Then `{Many & Few}(S) = (S, C(S))` is a set together with its partition.

## Properties

1. **Partition.** The three intervals are disjoint and cover `ℝ`, so the preimages are disjoint and cover `S`. Some classes may be empty.
2. **Relativity.** A change of frame by `c` replaces `u` with `u + c`. If the boundaries shift by the same `c`, `C(S)` is unchanged. `C(S)` depends only on where `S` sits relative to the boundaries.
3. **Invariant width.** `b₂ − b₁` is a difference of positions, so it is frame-independent.
4. **Inversion.** `u ↦ −u` swaps `S_in` and `S_out` when the boundaries are symmetric (`b₁ = −b₂`). If `S` is closed under inversion, then `|S_in| = |S_out|`, consistent with Axiom 1 (the sum of all numbers is nothing).
5. **Refinement.** `n` boundaries give `n + 1` classes by the same construction, and adding a boundary only refines the partition.

## Conventions

- Elements exactly on a boundary are assigned to `S_mid`.
- `S` contains only positive magnitudes. `0` and `Infinity` are the ends of the log-line and are not elements of `S`, consistent with Axiom 2.
- Optionally, `C(S)` may also record the sizes `(|S_in|, |S_mid|, |S_out|)`, so "few" and "many" are read as cardinalities (or measures) of the classes.
