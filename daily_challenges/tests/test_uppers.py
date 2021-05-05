import pytest 
from solution.uppers import upper_letter

def test_Hello():
    assert upper_letter('Hello world') == [("H",0)]

def test_Hello_World():
    assert upper_letter("HeLlO wOrLd!") == [("H",0), ("L",2), ("O",4), ("O",7), ("L",9)]

def test_not_string():
    assert upper_letter(345) == "Not a string"

def test_no_capitals():
    assert upper_letter("hello world") == []