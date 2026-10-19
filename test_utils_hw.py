from utils import calculate_discount, get_full_name, is_even


def test_calculate_discount_20_percent():
    assert calculate_discount(100, 20) == 80.0


def test_calculate_discount_50_percent():
    assert calculate_discount(200, 50) == 100.0


def test_calculate_discount_zero_discount():
    assert calculate_discount(150, 0) == 150.0


def test_calculate_discount_zero_price():
    assert calculate_discount(0, 30) == 0.0


def test_calculate_discount_float_values():
    assert calculate_discount(99.99, 10) == 89.991


def test_is_even_positive_even():
    assert is_even(4) is True


def test_is_even_positive_odd():
    assert is_even(7) is False


def test_is_even_negative_even():
    assert is_even(-8) is True


def test_is_even_negative_odd():
    assert is_even(-5) is False


def test_is_even_zero():
    assert is_even(0) is True


def test_get_full_name_standard():
    assert get_full_name("Тарас", "Шевченко") == "Тарас Шевченко"


def test_get_full_name_short():
    assert get_full_name("Ян", "Лі") == "Ян Лі"


def test_get_full_name_long():
    assert (
        get_full_name("Костянтин-Максиміліан", "Константинопольський")
        == "Костянтин-Максиміліан Константинопольський"
    )


def test_get_full_name_single_char():
    assert get_full_name("О", "К") == "О К"


def test_get_full_name_another_valid():
    assert get_full_name("John", "Doe") == "John Doe" #