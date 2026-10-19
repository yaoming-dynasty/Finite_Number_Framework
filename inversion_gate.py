# Gates

Companion to the Finite Number Framework README and `C_of_S.md`.

**Authors:** Christopher Thomas Ronio, Jeremey James Grice-Rosa

**Copyright (c) 2026 Christopher Thomas Ronio and Jeremey James Grice-Rosa. All rights reserved.**

---

## 1. Values

Each input is classified by `C(S)` (see `C_of_S.md`) and read as a balanced-ternary value:

| Class | Meaning | Value |
|---|---|---|
| `S_in` | Few | −1 |
| `S_mid` | between the boundaries | 0 |
| `S_out` | Many | +1 |

## 2. Basic gates

| Gate | Definition | Framework meaning |
|---|---|---|
| `NOT(v)` | `−v` | inversion `u ↦ −u` |
| `AND(v₁, …)` | `min` | |
| `OR(v₁, …)` | `max` | |

## 3. Relation gate `R(x, y)`

Inputs are two positive magnitudes. The gate classifies their frame-independent relation `{x --> y} = ln(x / y)` using a tolerance `t`:

| `ln(x / y)` | Output |
|---|---|
| `< −t` | −1 (x is Few relative to y) |
| within `±t` | 0 (comparable) |
| `> +t` | +1 (x is Many relative to y) |

Properties:

- **Scale-free:** `R(x, y) = R(kx, ky)` for any `k > 0`.
- **No common origin needed:** the boundary cancels in `ln(x / y)`.
- **Inversion symmetry:** `R(x, y) = NOT(R(y, x))`.

## 4. Balance gate `Bal(v₁, …, vₙ)`

Outputs the sign of the plain sum of the values: `0` if the sum is 0, otherwise `−1` or `+1`.

- A set whose Few and Many cancel is **balanced** (`Bal = 0`). This checks Axiom 1 (the sum of all numbers is nothing).
- The plain sum is used rather than a saturated one, because saturation breaks associativity: `(−1 + −1) + 1 = 0` but `−1 + (−1 + 1) = −1`.
- For a set closed under inversion, the `C(S)` values with symmetric boundaries sum to 0, so `Bal = 0`.

Example: inputs `(−1, +1, 0, −1, +1)` give `Bal = 0`. Adding one more `−1` gives `Bal = −1` (Few-heavy).

## 5. What the gates add

- **Scale-free comparison** of things with no shared reference (`R`).
- **Balance detection** across a whole set (`Bal`).

## 6. Implementation

See `gates.py`. Run it to execute the self-checks:

```bash
python3 gates.py
```

## 7. Notice

This is a copyright notice in the names of the two authors. It is not a registration and not a license; the authors choose a license (for example MIT, Apache-2.0, CC BY 4.0, or all rights reserved) and, if desired, register the work with their national copyright office. For authorship evidence, hash and sign the files as described in the README's Provenance section.
