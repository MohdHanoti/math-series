import pytest
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_fibonacci_01():
    actual=fibonacci(0)
    excepted=0
    
    assert actual == excepted

def test_fibonacci_02():
    actual=fibonacci(1)
    excepted=1
    assert actual == excepted

def test_fibonacci_03():
    actual=fibonacci(3)
    excepted=2
    assert actual == excepted

def test_fibonacci_04():
    actual=fibonacci(7)
    excepted=13
    assert actual == excepted

def test_fibonacci_05():
    actual=fibonacci("string")
    excepted="you have to enter positive int value"
    assert actual == excepted

def test_fibonacci_06():
    actual=fibonacci(-1)
    excepted="you have to enter positive int value"
    assert actual == excepted



# lucas tests:
#---------------------------------------------------------
def test_lucas_01():
    actual=lucas(0)
    excepted=2
    assert actual == excepted 

def test_lucas_02():
    actual=lucas(1)
    excepted=1
    assert actual == excepted

def test_lucas_03():
    actual=lucas(3)
    excepted=4
    assert actual == excepted

def test_lucas_04():
    actual=lucas(7)
    excepted=29
    assert actual == excepted

def test_lucas_05():
    actual=lucas("string")
    excepted="you have to enter positive int value"
    assert actual == excepted

def test_lucas_06():
    actual=lucas(-1)
    excepted="you have to enter positive int value"
    assert actual == excepted    

#sum series tests:
#---------------------------------------------------------
def test_sum_series_01():
    actual=sum_series(100,0,0)
    excepted = 0
    assert actual == excepted

def test_sum_series_02():
    actual=sum_series(3)
    excepted = 2
    assert actual == excepted

def test_sum_series_03():
    actual=sum_series(2,1,1)
    excepted = 2
    assert actual == excepted

def test_sum_series_04():
    actual=sum_series(3,2,2)
    excepted = 6
    assert actual == excepted         

def test_sum_series_05():
    actual=sum_series("string")
    excepted = "you have to enter positive int value"
    assert actual == excepted

def test_sum_series_06():
    actual=sum_series(-1)
    excepted = "you have to enter positive int value"
    assert actual == excepted

