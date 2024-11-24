from numb3rs import validate

def test_validate():
    assert validate("1.3.4.5") == True
    assert validate("256.34.567.12") == False
    assert validate("0.1.23.45") == True
    assert validate("4.56.78.91") == True
    assert validate("cat") == False
    assert validate("32234") == False
    assert validate("259.36.238.12") == False
    assert validate("123.456.789.1000") == False
    assert validate("1.2.3.") == False
    assert validate("1.2.3.4.5") == False
    assert validate("254.253.91.296") == False
    assert validate("253.128.257.11") == False
