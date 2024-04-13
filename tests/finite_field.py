from nbo.finite_field import FieldElement

def test_basic_op():
	a = FieldElement(3, 13)
	b = FieldElement(1, 13)
	print(a ** 3)
	assert a ** 3==b