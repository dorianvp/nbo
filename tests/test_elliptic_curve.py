import pytest
from nbo.elliptic_curve import Point


def test_eq():
    a = Point(-1, -1, 5, 7)
    b = Point(-1, -1, 5, 7)
    assert a == b


def test_ne():
    with pytest.raises(ValueError):
        a = Point(-1, -1, 5, 7)
        b = Point(-1, -2, 5, 7)
        assert a == b
