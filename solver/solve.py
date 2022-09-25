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
from re import I


def solve(exercise: object):
    ### Parse and solve ###
    x = exercise["x"]
    radix = exercise["radix"]
    operation = exercise["operation"]

    # Check type of exercise
    if exercise["type"] == "integer_arithmetic":
        # Check what operation within the integer arithmetic operations we need to

        if operation == "addition":
            # Solve integer arithmetic addition exercise
            from add.int_addition import addition
            result = addition(radix, x, exercise["y"])
            return {"answer": result}

        elif operation == "subtraction":
            from subtraction.int_subtraction import subtraction
            return {"answer": subtraction(radix, x, exercise["y"])}

        elif operation == "multiplication_primary":
            from multiply.int_multiplication import multiplication
            return {"answer": multiplication(radix, x, exercise["y"])}

        elif operation == "multiplication_karatsuba":
            from karatsuba.int_karatsuba import karatsuba
            return {"answer": karatsuba(radix, x, exercise["y"])}

        elif operation == "extended_euclidean_algorithm":
            from euclidian.int_euclidian import extended_euclidian
            gcd, answer_a, answer_b = extended_euclidian(
                radix, x, exercise["y"])

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
            from add.int_addition import addition

            return {"answer": addition(radix, x, exercise["y"])}
        elif operation == "subtraction":
            from subtraction.mod_subtraction import mod_subtraction
            return {"answer": mod_subtraction(radix, x, exercise["y"], exercise["modulus"])}

        elif operation == "multiplication":
            from multiply.mod_multiplication import mod_multiplication
            return {"answer": mod_multiplication(radix, x, exercise["y"], modulus)}

        elif operation == "reduction":
            from reduction.mod_reduction import mod_reduction
            return {"answer": mod_reduction(radix, x, modulus)}

        elif operation == "inversion":
            from inverse.inversion import inversion

            # return {"answer": inversion(radix, x, exercise["y"])}


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
