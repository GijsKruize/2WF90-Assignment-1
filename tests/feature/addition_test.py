from solver.solve import *
from .assert_answer import assert_exercise


def test_simple_exercise_0():
    assert_exercise("simple", 0)


def test_simple_exercise_8():
    assert_exercise("simple", 8)


def test_realistic_exercise_6():
    assert_exercise("realistic", 6)


def test_realistic_exercise_7():
    assert_exercise("realistic", 7)
