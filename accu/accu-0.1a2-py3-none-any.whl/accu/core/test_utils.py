from .utils import is_true


def test_true():
    assert True


def test_is_true():
    """Test the is_true function."""
    # False assertations
    assert is_true("False") is False
    assert is_true("F") is False
    assert is_true("0") is False

    # True assertations
    assert is_true("1")
    assert is_true("y")
    assert is_true("yes")
    assert is_true("t")
    assert is_true("true")
    assert is_true("on")
