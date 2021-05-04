import pytest 
from solution.fibbinacci import f

def test_fifth_number():
    assert f(5) == 5

def test_seventh_number():
    assert f(7) == 13

def test_ninth_number():
    assert f(9) == 34

def test_negatives():
    assert f(-1) == "Function requires a positive integer"

def test_floats():
    assert f(3.14) == "Function requires a positive integer"

def test_letters():
    assert f('fibbinacci') == "Function requires a positive integer"