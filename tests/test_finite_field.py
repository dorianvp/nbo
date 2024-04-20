import pytest
from nbo.finite_field import FieldElement


def test_addition():
    a = FieldElement(3, 13)
    b = FieldElement(2, 13)
    c = FieldElement(11, 13)
    d = FieldElement(2, 5)
    assert a + b == FieldElement(5, 13)
    assert a + c == FieldElement(1, 13)
    with pytest.raises(TypeError):
        a + d


def test_subtraction():
    a = FieldElement(3, 13)
    b = FieldElement(2, 13)
    c = FieldElement(11, 13)
    d = FieldElement(2, 5)
    assert a - b == FieldElement(1, 13)
    assert a - c == FieldElement(5, 13)
    with pytest.raises(TypeError):
        a - d


def test_mul():
    pass


def test_div():
    pass


def test_positive_pow():
    a = FieldElement(3, 13)
    b = FieldElement(1, 13)
    print(a**3)
    assert a**3 == b


def test_negative_pow():
    a = FieldElement(7, 13)
    b = FieldElement(8, 13)
    assert a**-3 == b
