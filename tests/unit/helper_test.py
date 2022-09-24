from helpers import *


def test_is_positive():
    assert is_positive("AB894F")


def test_zero_is_not_positive():
    assert not is_positive("0000")


def test_is_not_positive():
    assert not is_positive("-AB894F")


def test_is_at_least_zero():
    assert is_at_least_zero("AB894F")


def test_zero_is_not_at_least_zero():
    assert is_at_least_zero("0000")


def test_is_not_at_least_zero():
    assert not is_at_least_zero("-AB894F")


def test_remove_leading_zeros():
    assert "1" == remove_leading_zeros("0000001")


def test_remove_leading_zeros_empty():
    assert "0" == remove_leading_zeros("0000000")
