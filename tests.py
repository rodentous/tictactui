import os
from board import *
from draw import *


def run_tests():
    print("RUNNING TESTS from tests.txt")
    test = 0

    # check if file exists (if not skip tests)
    if not os.path.isfile("tests.txt"):
        print(term.red + "tests.txt DOES NOT EXIST. SKIPPING TESTS" + term.normal)
        print("PRESS ENTER")
        input()
        return

    # run tests
    with open('tests.txt', 'r') as file:
        # iterate through lines (tests)
        for line in file:
            test += 1
            grid = [['' for i in range(3)] for j in range(3)]

            if len(line) != 16:
               # invalid test, abort
               print(term.red + f"TEST {test} IS INVALID" + term.normal)
               exit(1)

            # read first 9 characters (a grid)
            for i in range(3):
                for j in range(3):
                    character = line[i * 3 + j]
                    if character == 'x' or character == 'o':
                        grid[i][j] = character
                    elif character == ' ' or character == '_':
                        grid[i][j] = ''
                    else:
                        # unknown character, abort
                        print(term.red + f"TEST {test} IS INVALID" + term.normal)
                        exit(1)

            # read 10th character (find optimal move for which character?)       
            player = line[10]

            # read 12th and 14th characters (expected x and y)
            expected_x, expected_y = line[12], line[14]

            # calculate real answer
            x, y = predict(grid, player)

            # test failed, abort
            if str(x) != expected_x or str(y) != expected_y:
                print(term.red + f"TEST {test} FAILED (expected {expected_x} {expected_y} got {x} {y})" + term.normal)
                exit(1)
            # test succeded
            else:
                print(term.green + f"TEST {test} OK" + term.normal)

    print("PRESS ENTER")
    input()
