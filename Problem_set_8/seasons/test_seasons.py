import pytest
from seasons import season
import datetime


def test_leap_year():
    # Testing with a leap year date, result might differ in terms of exact minutes based on today's date
    result = season("2004-02-29")
    assert isinstance(result, str)  # Just checking it doesn't raise an error

def test_invalid_date_format():
    # Testing with an invalid date format
    with pytest.raises(SystemExit):
        season("09-03-2006")  # this is an Incorrect format
    
def test_future_date():
    #future date
    with pytest.raises(SystemExit):
        season("2030-01-01")
