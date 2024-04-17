from nbo.finite_field import FieldElement


def test_positive_pow():
    a = FieldElement(3, 13)
    b = FieldElement(1, 13)
    print(a**3)
    assert a**3 == b


def test_negative_pow():
    a = FieldElement(7, 13)
    b = FieldElement(8, 13)
    assert a**-3 == b
