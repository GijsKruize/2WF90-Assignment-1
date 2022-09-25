##
# 2WF90 Algebra for Security -- Software Assignment 1
# Integer and Modular Arithmetic
# solve.py
#
#
# Group number: 31
# group_number
#
# Author names and student IDs:
# Gijs Kruize (1658662)
# Christian Groothuis (1715534)
# Jordy Verhoeven (1001249)
# author_name_4 (author_student_ID_4)
##
# Import built-in json library for handling input/output
import json

from euclidian.int_euclidian import extended_euclidian
from multiply.mod_multiplication import mod_multiplication
from add.int_addition import addition


def solve(exercise):
    answer = {}
    ### Parse and solve ###
    x = exercise["x"]
    y = exercise["y"]
    radix = exercise["radix"]
    operation = exercise["operation"]

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to

        if operation == "addition":
            # Solve integer arithmetic addition exercise
            result = addition(radix, x, y)
            return {
                "answer": result
            }
            pass
        elif operation == "subtraction":
            # Solve integer arithmetic subtraction exercise
            pass
        elif operation == "multiplication_primary":
            # Solve integer arithmetic primary multiplication exercise
            pass
        elif operation == "multiplication_karatsuba":
            # Solve integer arithmetic karatsuba multiplication exercise
            pass
        elif operation == "extended_euclidean_algorithm":
            gcd, answer_a, answer_b = extended_euclidian(radix, x, y)

            return {
                "answer-a": answer_a,
                "answer-b": answer_b,
                "answer-gcd": gcd,
            }

    elif exercise["type"] == "modular_arithmetic":
        modulus = exercise["modulus"]

        # Check what operation within the modular arithmetic operations we need to
        if operation == "addition":
            # Solve modular arithmetic reduction exercise
            pass
        elif operation == "subtraction":
            pass
        elif operation == "multiplication":
            return {"answer": mod_multiplication(radix, x, y, modulus)}
        elif operation == "reduction":
            pass
        elif operation == "inversion":
            pass


def solve_from_file(exercise_location: str) -> object:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_exercise(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
