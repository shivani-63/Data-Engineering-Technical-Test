"""Test file for test_3.py."""

import pytest

from test_3 import sum_current_time

def test_sum_current_time_correct():
    """Test to show the function works correctly."""
    time = '01:02:03'
    assert sum_current_time(time) == 6


def test_sum_current_time_correct_2():
    """Second test to show function works for two digit numbers."""
    time = '21:02:45'
    assert sum_current_time(time) == 68


def test_sum_current_time_raise_error_for_format():
    """Test error raised when string format is incorrect."""
    with pytest.raises(ValueError):
        sum_current_time('21-02-45')


def test_sum_current_time_raise_hour_error():
    """Test value error raised when hour exceeds 23."""
    with pytest.raises(ValueError):
        sum_current_time('29:02:45')


def test_sum_current_time_raise_minute_error():
    """Test value error raised when minute exceeds 59."""
    with pytest.raises(ValueError):
        sum_current_time('23:65:45')


def test_sum_current_time_raise_second_error():
    """Test value error raised when second exceeds 59."""
    with pytest.raises(ValueError):
        sum_current_time('23:59:60')


def test_sum_raise_error_for_invalid_type():
    """Test type error raised when input not a string."""
    with pytest.raises(TypeError):
        sum_current_time(134254)


def test_sum_raise_error_for_invalid_input_letters():
    """Test value error raised when invalid numbers."""
    with pytest.raises(ValueError):
        sum_current_time("he:ll:oo")
