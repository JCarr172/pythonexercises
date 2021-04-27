import pytest 
from applications.factorial import fact

def test_fact_0():
    assert fact(0) == 1

def test_fact_5():
    assert fact(5) == 120
    
