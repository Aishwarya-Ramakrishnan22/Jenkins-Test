"""
Tests for math_utils
====================
Simple pytest tests for Jenkins CI/CD learning.
"""

from math_utils import add, multiply, subtract, is_even


# ── Addition Tests ────────────────────────────────────────────────────

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5


# ── Multiplication Tests ─────────────────────────────────────────────

def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative_numbers():
    assert multiply(-2, -3) == 6


# ── Subtraction Tests ────────────────────────────────────────────────

def test_subtract():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 7) == -4


# ── Even/Odd Tests ───────────────────────────────────────────────────

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False

def test_is_even_zero():
    assert is_even(0) is True
