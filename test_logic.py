from logic import calculate


def test_add():
    assert calculate("10+20") == 30


def test_subtract():
    assert calculate("20-5") == 15


def test_multiply():
    assert calculate("5*6") == 30


def test_divide():
    assert calculate("10/2") == 5


def test_sqrt():
    assert calculate("sqrt(16)") == 4


def test_power():
    assert calculate("2x^y3") == 8


def test_sin():
    assert round(calculate("sin(0)"), 2) == 0


def test_error():
    assert calculate("10/0") == "Error"

