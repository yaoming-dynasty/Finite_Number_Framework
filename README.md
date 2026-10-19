# The Finite Number Framework

A relational theory of magnitude on a logarithmic line.

## Overview

This repository contains the formal documentation for the Finite Number Framework, a relational theory in which magnitudes are not treated as absolute quantities but as positions on a logarithmic line relative to a chosen boundary.

The framework is built around the canonical logarithmic coordinate

q(x) = ln(x),

which turns multiplication into addition, inversion into negation, and boundary change into translation. The essential idea is that finite quantities acquire meaning only relative to a boundary and an absolute reference point.

## Documentation

- [docs/manuscript.md](docs/manuscript.md) — the main journal-style manuscript
- [docs/decomposition_bridge.md](docs/decomposition_bridge.md) — the bridge between magnitude space, logarithmic coordinates, and the classification scheme
- [docs/composition_bridge.md](docs/composition_bridge.md) — how element-level magnitudes compose into larger structures
- [docs/transformation_bridge.md](docs/transformation_bridge.md) — how transformations and frame changes affect the system
- [docs/verification.md](docs/verification.md) — a finite verification procedure for the framework
- [docs/proof_appendix.md](docs/proof_appendix.md) — formal lemmas and proofs
- [docs/theorem_index.md](docs/theorem_index.md) — theorem numbering and index
- [docs/README.md](docs/README.md) — documentation index

## Suggested reading order

1. [docs/manuscript.md](docs/manuscript.md)
2. [docs/decomposition_bridge.md](docs/decomposition_bridge.md)
3. [docs/composition_bridge.md](docs/composition_bridge.md)
4. [docs/transformation_bridge.md](docs/transformation_bridge.md)
5. [docs/verification.md](docs/verification.md)
6. [docs/proof_appendix.md](docs/proof_appendix.md)
7. [docs/theorem_index.md](docs/theorem_index.md)

## Core mathematical identities

The framework is structured around the following identities:

- q(xy) = q(x) + q(y)
- q(1/x) = -q(x)
- P_B(x) = ln(x/B)
- P_{B'}(x) = P_B(x) + ln(B/B')
- P_B(x) - P_B(y) = ln(x/y)
- q(x) + q(1/x) = 0 for inverse pairs

These identities define the formal algebraic backbone of the theory.

## Repository status

This repository is organized as a working formal document set for the framework, with the main manuscript and appendices kept in the docs directory.
