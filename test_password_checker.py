import pytest
from password_checker import is_password_strong


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Password123!", True),
        ("A1#bcdef", True),
        ("12345678a!", True),
        ("VeryStrong1!", True),
        ("Кирилиця123!", True),
        ("Short1!", False),
        ("Password123", False),
        ("Password!", False),
        ("12345678!", False),
        ("Pass word1!", False),
        ("        ", False),
    ],
)
def test_is_password_strong(password, expected):
    assert is_password_strong(password) == expected


@pytest.mark.skip(reason="Test is not ready yet")
def test_password_diversity():
    pass