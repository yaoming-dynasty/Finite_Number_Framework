"""Three-valued gates for the Finite Number Framework.

Copyright (c) 2026 Christopher Thomas Ronio and Jeremey James Grice-Rosa.
All rights reserved.

Values: -1 = S_in (Few), 0 = S_mid, +1 = S_out (Many).
"""

from math import log, isclose


def classify(m, b1, b2):
    """Class of a positive magnitude m given log-boundaries b1 < b2 (C(S))."""
    if m <= 0:
        raise ValueError("magnitudes must be positive; 0 and infinity are not elements of S")
    if b1 >= b2:
        raise ValueError("need b1 < b2")
    u = log(m)
    if u < b1:
        return -1   # S_in  (Few)
    if u > b2:
        return 1    # S_out (Many)
    return 0        # S_mid (boundary points go here)


def NOT(v):
    """Inversion u -> -u."""
    return -v


def AND(*vs):
    return min(vs)


def OR(*vs):
    return max(vs)


def R(x, y, t=0.1):
    """Relation gate: class of ln(x/y) with tolerance band [-t, t].

    Frame-independent: needs no common origin, only the ratio x/y.
    """
    if x <= 0 or y <= 0:
        raise ValueError("magnitudes must be positive")
    r = log(x / y)
    if r < -t:
        return -1   # x is Few relative to y
    if r > t:
        return 1    # x is Many relative to y
    return 0        # comparable


def Bal(*vs):
    """Balance gate: sign of the plain sum of values (0 means balanced).

    Uses the plain sum, not a saturated one, so it is associative.
    """
    s = sum(vs)
    return (s > 0) - (s < 0)


if __name__ == "__main__":
    # NOT is an involution
    assert all(NOT(NOT(v)) == v for v in (-1, 0, 1))

    # classify with symmetric boundaries b1 = -b2
    b1, b2 = -1.0, 1.0
    assert classify(0.1, b1, b2) == -1
    assert classify(1.0, b1, b2) == 0
    assert classify(50.0, b1, b2) == 1

    # Relation gate: boundary-free, scale-free
    assert R(1, 10) == -1 and R(10, 1) == 1 and R(5, 5.1) == 0
    assert R(3, 7) == R(3e6, 7e6)          # same ratio, any scale

    # Inversion symmetry: R(x, y) = -R(y, x)
    assert R(2, 9) == NOT(R(9, 2))

    # Balance gate
    assert Bal(-1, 1, 0, -1, 1) == 0
    assert Bal(-1, 1, 0, -1, 1, -1) == -1

    # Axiom 1 check: a set closed under inversion is balanced
    S = [0.2, 5.0, 0.5, 2.0, 1.0]          # {x, 1/x} pairs plus 1
    vals = [classify(m, -0.5, 0.5) for m in S]
    assert Bal(*vals) == 0

    print("all checks passed")
