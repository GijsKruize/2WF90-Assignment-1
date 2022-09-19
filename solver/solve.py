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
# author_name_3 (author_student_ID_3)
# author_name_4 (author_student_ID_4)
##
# Import built-in json library for handling input/output
import json
import re


def solve(exercise):
    ### Parse and solve ###
    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to

        if exercise["operation"] == "addition":
            # Solve integer arithmetic addition exercise
            pass
        elif exercise["operation"] == "subtraction":
            # Solve integer arithmetic subtraction exercise
            pass
        elif exercise["operation"] == "multiplication_primary":
            # Solve integer arithmetic primary multiplication exercise
            pass
        elif exercise["operation"] == "multiplication_karatsuba":
            # Solve integer arithmetic karatsuba multiplication exercise
            pass
        elif exercise["operation"] == "extended_euclidean_algorithm":
            # Solve integer arithmetic extended euclidean algorithm exercise
            pass

    else:  # exercise["type"] == "modular_arithmetic"
        # Check what operation within the modular arithmetic operations we need to

        if exercise["operation"] == "addition":
            # Solve modular arithmetic reduction exercise
            pass
        elif exercise["operation"] == "subtraction":
            pass
        elif exercise["operation"] == "multiplication":
            pass
        elif exercise["operation"] == "reduction":
            pass
        elif exercise["operation"] == "inversion":
            pass

    # Sample answer
    answer = {
        "answer": "32"
    }

    return answer


def solve_from_file(exercise_location: str) -> object:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object, ):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_from_file_and_to_file(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
