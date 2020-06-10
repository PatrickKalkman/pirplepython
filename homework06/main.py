"""
Python Is Easy course @Pirple.com
Homework Assignment #6: Advanced Loops
Patrick Kalkman / patrick@simpletechture.nl

Details:

Create a function that takes in two parameters: rows, and columns, both of
which are integers. The function should then proceed to draw a playing board
(as in the examples from the lectures) the same number of rows and columns as
specified. After drawing the board, your function should return True.


Extra Credit:

Try to determine the maximum width and height that your terminal and screen
 can comfortably fit without wrapping. If someone passes a value greater
 than either maximum, your function should return False.

"""

import os


def printPlayingBoard(rows, columns):

    numberOfRows = rows * 2
    numberOfColumns = columns * 2
    size = os.get_terminal_size()

    if numberOfColumns > size.columns or numberOfRows > size.lines:
        return False

    for row in range(numberOfRows - 1):
        if row % 2 == 0:
            for column in range(1, numberOfColumns):
                if column % 2 == 1:
                    if column != numberOfColumns - 1:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print("|", end="")
        else:
            print("-" * (numberOfColumns - 1))


printPlayingBoard(5, 5)
