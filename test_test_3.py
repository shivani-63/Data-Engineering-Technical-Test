import pytest
from test_3 import sum_current_time

def test_sum_current_time_correct():
    time = '01:02:03'
    assert sum_current_time(time) == 6


def test_sum_current_time_correct_2():
    time = '21:02:45'
    assert sum_current_time(time) == 68


def test_sum_current_time_raise_error_for_format():
    with pytest.raises(ValueError):
        sum_current_time('21-02-45')


def test_sum_current_time_raise_hour_error():
    with pytest.raises(ValueError):
        sum_current_time('29:02:45')


def test_sum_current_time_raise_minute_error():
    with pytest.raises(ValueError):
        sum_current_time('23:65:45')


def test_sum_current_time_raise_second_error():
    with pytest.raises(ValueError):
        sum_current_time('23:59:60')


def test_sum_raise_error_for_invalid_type():
    with pytest.raises(TypeError):
        sum_current_time(134254)


def test_sum_raise_error_for_invalid_input_length():
    with pytest.raises(ValueError):
        sum_current_time("3435:4354:12") 


def test_sum_raise_error_for_invalid_input_letters():
    with pytest.raises(ValueError):
        sum_current_time("he:ll:oo")
