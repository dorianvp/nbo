import pytest
from nbo.elliptic_curve import Point
from nbo.finite_field import FieldElement


def test_eq():
    a = Point(-1, -1, 5, 7)
    b = Point(-1, -1, 5, 7)
    assert a == b


def test_ne():
    with pytest.raises(ValueError):
        a = Point(-1, -1, 5, 7)
        b = Point(-1, -2, 5, 7)
        assert a == b


def test_addition():
    p1 = Point(-1, -1, 5, 7)
    inf = Point(None, None, 5, 7)
    assert p1 + inf == Point(-1, -1, 5, 7)


def test_mul():
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    x = FieldElement(47, prime)
    y = FieldElement(71, prime)
    p = Point(x, y, a, b)

    e = FieldElement(24, 31)
    f = 2
    assert f * e == e + e
