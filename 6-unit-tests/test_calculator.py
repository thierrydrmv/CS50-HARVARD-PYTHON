from calculator import square, sum, subtraction, division
import pytest

def test_square_positive():
  assert square(2) == 4
  assert square(3) == 9

def test_square_negative():
  assert square(-2) == 4
  assert square(-3) == 9

def test_square_zero():
  assert square(0) == 0

def test_square_str():
  with pytest.raises(TypeError):
    square("Cat")

def test_sum():
  assert sum(1, 2) == 3
  assert sum(4, 12) == 16

def test_subtraction():
  assert subtraction(12, 4) == 8
  assert subtraction(99, 32) == 67

def test_division():
  assert division(22, 4) == 5.5
  assert division(4, 1) == 4
