"""
Python Is Easy course @Pirple.com
Project #1: A Simple Game
Patrick Kalkman / patrick@simpletechture.nl

Details:

Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro
company. In this project, your task is create a Connect 4 game in Python.
Before you get started, please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly
straightforward. You'll want to draw the board, and allow two players
to take turns placing their pieces on the board (but as you learned above,
they can only do so by choosing a column, not a row). The first player to get
4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.

Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure
out how to import a package like termcolor into your project. We're going to
cover importing later in the course, but try and see if you can figure it out
on your own. Or you might be able to find unicode characters to use instead,
depending on what your system supports. Here's a hint: print(u'\u2B24')


"""


from termcolor import colored


def createPiecesModel():
    pieces = []
    for row in range(6):
        pieces.append([])
        for column in range(7):
            pieces[row].append(0)
    return pieces


def getChipCharacter(row, column):
    typeOfChip = pieces[row][column]
    if typeOfChip == 0:
        return "  "
    elif typeOfChip == 1:
        return colored("\u2B24 ", "red")
    elif typeOfChip == 2:
        return colored("\u2B24 ", "green")


pieces = createPiecesModel()


def printConnectBoard(piecesModel):

    for row in range(12):
        if row % 2 == 0:
            for column in range(14):
                piece = getChipCharacter(int(row / 2), int(column / 2))
                if column % 2 == 1:
                    if column != 13:
                        print(piece, end="")
                    else:
                        print("  ")
                else:
                    print("|", end="")
        else:
            print("-" * 19)


def getFreeRow(column):
    for row in range(5, -1, -1):
        if pieces[row][column] == 0:
            return row


def addChipToColumn(column, pieceType):
    freeRow = getFreeRow(column - 1)
    pieces[freeRow][column - 1] = pieceType


player = 1
while True:
    printConnectBoard(pieces)
    column = input(f"Player {player} in which column do you want your piece? ")
    addChipToColumn(int(column), player)
    if player == 1:
        player = 2
    else:
        player = 1
