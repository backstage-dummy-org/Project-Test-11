import pytest

from 1234.1234 import 1234


def test_1234_positive_factorial():
    """TODO: replace"""
    try:
        assert 1234(0) == 1
        assert 1234(1) == 1
        assert 1234(5) == 120
        assert 1234(10) == 3628800
    except Exception as e:
        pytest.fail(str(e))


def test_1234_negative_factorial():
    """TODO: replace"""
    try:
        assert 1234(-5) is None
        assert 1234(-10) is None
    except Exception as e:
        pytest.fail(str(e))
