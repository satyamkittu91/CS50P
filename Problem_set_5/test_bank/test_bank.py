from bank import value

def test_hello():
    assert value('hello') == 0
    assert value('hello, world') == 0


def test_h():
    assert value('hey') == 20
    assert value("hola") == 20
    assert value("hagimaru") == 20
    assert value("hajito") == 20


def test_hless():
    assert value("What's up") == 100
    assert value("nothing") == 100

def test_capitalwords():
    assert value("HELLO") == 0
    assert value("HEY") == 20