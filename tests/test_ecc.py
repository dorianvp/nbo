import pytest
from nbo.finite_field import FieldElement
from nbo.elliptic_curve import Point
from nbo.ecc import S256Point, N, G


# def test_curve():
#     prime = 223
#     a = FieldElement(0, prime)
#     b = FieldElement(7, prime)
#     valid_points = ((192, 105), (17, 56), (1, 193))
#     invalid_points = ((200, 119), (42, 99))
#     for x_raw, y_raw in valid_points:
#         x = FieldElement(x_raw, prime)
#         y = FieldElement(y_raw, prime)
#         Point(x, y, a, b)
#     for x_raw, y_raw in invalid_points:
#         x = FieldElement(x_raw, prime)
#         y = FieldElement(y_raw, prime)
#         with pytest.raises(ValueError):
#             Point(x, y, a, b)


def test_signature():
    z = 0xBC62D4B80D9E36DA29C16C5D4D9F11731F36052C72401A76C23C0FB5A9B74423
    r = 0x37206A0610995C58074999CB9767B87AF4C4978DB68C06E8E6E81D282047A7C6
    s = 0x8CA63759C1157EBEAEC0D03CECCA119FC9A75BF8E6D0FA65C841C8E2738CDAEC
    px = 0x04519FAC3D910CA7E7138F7013706F619FA8F033E6EC6E09370EA38CEE6A7574
    py = 0x82B51EAB8C27C66E26C858A079BCDF4F1ADA34CEC420CAFC7EAC1A42216FB6C4
    point = S256Point(px, py)
    s_inv = pow(s, N - 2, N)
    u = z * s_inv % N
    v = r * s_inv % N
    print("=====>", u * G)
    # assert (u * G + v * point).x.num == r
