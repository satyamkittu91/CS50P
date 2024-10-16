import pytest
from seasons import season

def test_valid_date():
    assert season("2006-03-09") == "nine million, seven hundred and fifty-four thousand, five hundred and sixty"

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

def test_large_valid_date():
    # Testing with an old valid date
    result = season("1800-01-01")
    assert isinstance(result, str)  # Checking for valid output without failure
