from fuel import gauge, convert
import pytest


def test_input():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_error():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    
    with pytest.raises(ValueError):
        convert("3/2")

def test_outputs():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"