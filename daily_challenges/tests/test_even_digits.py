import pytest 
from solution.even_digits import even_digits

def test_ten_thirty():
    assert even_digits(10,30) == [20, 22, 24, 26, 28]

def test_none():
    assert even_digits(10, 15) == []

def test_letters():
    assert even_digits('a', 'c') == None