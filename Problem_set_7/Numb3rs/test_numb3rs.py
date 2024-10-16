from numb3rs import validate

def test_validate():
    assert validate("1.3.4.5") == True
    assert validate("256.34.567.12") == False
    assert validate("0.1.23.45") == True
    assert validate("4.56.78.91") == True
    assert validate("cat") == False
    assert validate("32234") == False