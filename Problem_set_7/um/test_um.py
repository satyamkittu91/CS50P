from um import count

def test_no_um():
    # Test when there's no "um" in the text
    assert count("yummy") == 0
    assert count("hello world") == 0

def test_single_um():
    # Test for a single "um" occurrence
    assert count("um") == 1
    assert count("um...") == 1
    assert count("um, hello") == 1

def test_multiple_um():
    # Test for multiple "um" occurrences
    assert count("um um") == 2
    assert count("um, um, um") == 3
    assert count("um hello um") == 2

def test_um_with_other_words():
    # Test where "um" occurs with other words, but also inside another word
    assert count("yummy um") == 1
    assert count("um yummy um") == 2
    assert count("yummy ummy um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_um_boundary():
    # Test where "um" is next to non-word characters or spaces
    assert count("um...um") == 2
    assert count("um? um!") == 2
    assert count("um-um") == 2
