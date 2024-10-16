from bank import pay

def test_hello():
    assert pay('hello') == "$0"
    assert pay('hello, world') == "$20"


def test_h():
    assert pay('hey') == "$20"
    assert pay("hola") == "$20"
    assert pay("hagimaru") == "$20"
    assert pay("hajito") == "$20"


def test_hless():
    assert pay("What's up") == "$100"
    assert pay("nothing") == "$100"

def test_capitalwords():
    assert pay("HELLO") == "$100"
    assert pay("HEY") == "$20"