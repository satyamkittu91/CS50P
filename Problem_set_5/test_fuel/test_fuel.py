from fuel import get_fraction
import pytest


def test_input():
    assert get_fraction("1/2") == "50.0%"
    assert get_fraction("1/4") == "25.0%"
    assert get_fraction("3/4") == "75.0%"


def test_error():
    assert get_fraction("2/0") == None
    assert get_fraction("3/2") == None

def test_outputs():
    assert get_fraction("0/10") == "E"
    assert get_fraction("1/1") == "F"