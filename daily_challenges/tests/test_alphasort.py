import pytest 
from solution.alphasort import alphasort

def test_function():
    assert alphasort('hello world and practice makes perfect and hello world again') == 'again and hello makes perfect practice world'

def test_no_space():
    assert alphasort('Thishasnospaces') == []

def test_capitals():
    assert alphasort('This string Is capitalised Weird') == 'capitalised is string this weird'