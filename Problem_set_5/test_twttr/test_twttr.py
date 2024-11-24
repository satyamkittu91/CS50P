from twttr import shorten

def test_nonAlpha():
    assert shorten('$20') == '$20'
    assert shorten('20 dollars') == "20 dllrs"
    assert shorten('twentydollars') == "twntydllrs"

def test_consonants():
    assert shorten("rtx") == "rtx"
    assert shorten("mtg") == "mtg"

def test_vowels():
    assert shorten("aie") == ''
    assert shorten("ou") == ''

def test_capital():
    assert shorten("APPLE") == 'PPL'
    assert shorten("BANANA") == 'BNN'

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"