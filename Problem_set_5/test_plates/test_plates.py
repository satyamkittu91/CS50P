from plates import is_valid

def test_length():
    assert is_valid('a') == False
    assert is_valid("a123") == False
    assert is_valid("ink1234") == False
    assert is_valid("sat123") == True

def test_start():
    assert is_valid("a2") == False
    assert is_valid("non123") == True

def test_middle():
    assert is_valid("a2aa2") == False
    assert is_valid("cl4t") == False
    assert is_valid("AAA222") == True

def test_special():
    assert is_valid("tt2.3") == False
    assert is_valid("aa a2") == False
    assert is_valid("saty91") == True