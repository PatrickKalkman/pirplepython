"""
Python Is Easy course @Pirple.com
Homework Assignment #11: Error Handling
Patrick Kalkman / patrick@simpletechture.nl

Details:

Details:
 
As you've been completing the past homework assignments and projects, you've
undoubtedly run into errors a few times, and noticed that if you pass certain
types of variables to your functions, they will throw exceptions. Now's your
time to go back and make those functions better (bullet-proof them).

For this assignment you can choose any of the homeworks or projects you've
done so far. Pick a function that you know is particularly problematic and
add try/except/finally cases to it so that it can handle the errors more
gracefully.

Extra Credit:

Below your function, add 10 - 20 tests that call your function in different
ways, and show that it can now handle various different conditions and cases.


"""


from termcolor import colored


def createPiecesModel():
    pieces = []
    for row in range(6):
        pieces.append([])
        for _ in range(7):
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


# Used exception handling to make sure that a correct column was entered 
def addChipToColumn(choosen_column, pieceType):
    try:
        column = int(choosen_column)
        if column < 1 or column > 6:
            raise IndexError()
        freeRow = getFreeRow(column - 1)
        pieces[freeRow][column - 1] = pieceType
        return True
    except ValueError:
        print(f"{choosen_column} is not a valid column, please enter a number")
    except IndexError:
        print(f"There is no column {choosen_column}, please enter a number between 1 - 6")
    except Exception as e:
        print(f"An error occurred while trying to add a chip to a column: {e}")
    return False


def gameLoop():

    player = 1
    while True:
        printConnectBoard(pieces)
        column = input(
            f"Player {player} in which column do you want your piece? ")
        if addChipToColumn(column, player):
            if player == 1:
                player = 2
            else:
                player = 1

# Uncomment gameLoop for playing the game instead of running tests
#gameLoop()

# tests for validating the correct behavior
result = addChipToColumn('A', 1)
print(f"addChipToColumn('A', 1) should return False = {result}")
result = addChipToColumn(100, 1)
print(f"addChipToColumn(100, 1) should return False = {result}")
result = addChipToColumn(-100, 1)
print(f"addChipToColumn(-100, 1) should return False = {result}")
result = addChipToColumn(0, 1)
print(f"addChipToColumn(0, 1) should return False = {result}")

result = addChipToColumn(1, 1)
print(f"addChipToColumn(1, 1) should return True = {result}")
result = addChipToColumn(6, 1)
print(f"addChipToColumn(6, 1) should return True = {result}")