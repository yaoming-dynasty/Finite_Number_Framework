# The Finite Number Framework

A relational framework for mapping `{All_Things}` as positions on a logarithmic line, anchored by an absolute `0`, and read through the **Many & Few** algorithm.

**Authors:** Christopher Thomas Ronio, Jeremey James Grice-Rosa
**Status:** Draft v0.1

---

## 1. Core Statement

```
{The_Finite_Number} --> {0} --> {Infinity}
    = {Inside_Boundary} + {Outside_Boundary} --> {Infinity}
```

`-->` reads as **"relative to"**. A finite number has no standalone meaning: it is defined by its position relative to its anchors (`0` and `Infinity`), and a boundary divides the space between them into an inside and an outside.

## 2. Axioms

1. **The sum of all numbers is nothing.**
2. **Every number is finite, and the only infinite number is `0`**, which is infinite potential. `0` is always absolute; every other number is finite relative to it.

## 3. The Log-Line

Every thing `x` in `{All_Things}` has a positive magnitude. Its position relative to a boundary `B` is:

```
{x --> B} := ln(x / B)
```

- Negative: inside the boundary
- Zero: on the boundary
- Positive: outside the boundary
- `0` and `Infinity` sit at the two ends (`-∞`, `+∞`) and are never reached.

### Relativity

Changing the boundary from `B` to `B′` shifts every position by the same constant:

```
{x --> B′} = {x --> B} + ln(B / B′)
```

Positions are relative. **Differences between positions are not**:

```
{x --> y} := ln(x / y) = {x --> B} - {y --> B}     (B cancels)
```

This is the frame-independent relation between two things.

### Inversion

```
{1/x --> B} = -{x --> B}
```

Inversion swaps inside and outside. Inside and outside are the two signed halves of one line.

### Axiom 1, made precise

For any set closed under inversion (`x ∈ S ⇒ 1/x ∈ S`), each pair contributes `{x --> B} + {1/x --> B} = 0`, so:

```
Σ {x --> B} = 0
```

The sum of the whole is nothing.

### Axiom 2, geometrically

Identifying the two ends of the log-line (`0 = Infinity`) closes it into a **circle** with a single absolute point. Every other number is a finite position on that circle, relative to the absolute point.

## 4. Many & Few

```
{Many & Few}(S) = (S, C(S))
Many & Few = Boundary1 + Boundary2
```

The two boundaries are set **as needed** for the problem at hand. `C(S)` is the classification of `S` induced by the boundaries on the log-line (inside `Boundary1`, between the boundaries, outside `Boundary2`).

> Open: the exact definition of `C(S)` is to be fixed by the authors.

## 5. Algebra

- Positions combine by addition (multiplication of the underlying magnitudes): a group.
- Inversion is an involution: `u ↦ -u`.
- Boundary changes act on positions by constant shifts: a group action.
- Relations `{x --> y}` are invariant under that action.

## 6. Planned Work

- Application of Many & Few to set-theoretic paradoxes
- Decomposition Bridge and Transformation Bridge (simultaneous and commuting)
- The Geometric side: the closed log-line and its geometry
- Application to 2-D models of DNA

## 7. Provenance and Authorship

Authorship of this work is claimed by the authors listed above. A mathematical algorithm cannot by itself establish who wrote a document, so authorship is recorded with standard cryptographic and version-control evidence:

| Item | Value |
|---|---|
| Content fingerprint (SHA-256 of this file) | `<fill in after final edit>` |
| Signed commit / tag, author 1 | `<GPG or SSH signature: Christopher Thomas Ronio>` |
| Signed commit / tag, author 2 | `<GPG or SSH signature: Jeremey James Grice-Rosa>` |
| External timestamp | `<OpenTimestamps proof or public commit date>` |

To compute the fingerprint:

```bash
sha256sum README.md
```

The framework's own boundary-independent invariants (the relations `{x --> y}`) may additionally be used as a structural identifier of the content, but a structural identifier shows *what* the work is, not *who* made it. The signatures above are what bind the work to its authors.

## 8. Citation

```
Ronio, C. T., & Grice-Rosa, J. J. (2026). The Finite Number Framework (Draft v0.1).
```
