"""
Python Is Easy course @Pirple.com
Project #2: Hangman
Patrick Kalkman / patrick@simpletechture.nl


Details:

Have you ever played hangman? It's a children's game, normally played by kids
when they're supposed to be doing homework instead. If you've never played here
are the rules:

https://www.youtube.com/watch?v=cGOeiQfjYPk

https://www.wikihow.com/Play-Hangman

For this assignment, we want to play hangman in 2-player mode. The game should
start by prompting player 1 to pick a word. Then the screen should clear itself
so that player 2 can't see the word

hint: print(chr(27) + "[2J")

After the screen is clear, the "gallows" and the empty letter spaces should be
drawn, and player 2 should be allowed to guess letters until they either win,
or lose. As they choose correct letters, the letters should appear on the
screen in place of the blank space (clear and redraw the whole screen).
As they choose wrong letters, the "man" himself should come end up being
drawn, piece by piece. How many guesses they get before losing is up to you
(depending on how complicated of a man you want to draw).

Important: If you'd rather not do "hangman" because of the violence aspect,
that's fine! Please make "snowman" instead. You can see an example in the
wikihow link above.

Extra Credit:

Try finding a large list of dictionary words and embedding them in your
application. When the game starts, instead of player 1 choosing the word to
play with, the computer should pick a random word from the dictionary.
This will allow you to play against the computer instead of only 2-player
mode. When the game starts, the user should be prompted to choose between
1-player or 2-player mode.

"""

# This program uses curses, on windows install the library by
# using 'pip install windows-curses'

import curses
import time
from enum import Enum


class GameState(Enum):
    RUNNING = 1
    PLAYER1WINS = 2
    PLAYER2WINS = 3


def drawBoard(hangman):
    stdscr.addstr(0,   0, "Guess by typing a letter")
    stdscr.addstr(5,  10, "***************")
    stdscr.addstr(6,  10, "*             *")
    stdscr.addstr(7,  10, "*             *")
    stdscr.addstr(8,  10, "*")
    stdscr.addstr(9,  10, "*")
    stdscr.addstr(10, 10, "*")
    stdscr.addstr(11, 10, "*")
    stdscr.addstr(12, 10, "*")
    stdscr.addstr(13, 10, "*")
    stdscr.addstr(14, 10, "*")
    stdscr.addstr(15, 10, "*")
    stdscr.addstr(16, 10, "*")
    stdscr.addstr(17, 10, "*")
    stdscr.addstr(18, 10, "*")
    stdscr.addstr(19, 10, "*")

    if hangman > 0:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")

    if hangman > 1:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")
        stdscr.addstr(12, 10, "*             * ")
        stdscr.addstr(13, 10, "*             * ")
        stdscr.addstr(14, 10, "*             * ")
        stdscr.addstr(15, 10, "*             * ")
        stdscr.addstr(16, 10, "*             * ")
        stdscr.addstr(17, 10, "*             * ")

    if hangman > 2:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")
        stdscr.addstr(12, 10, "*             * ")
        stdscr.addstr(13, 10, "*       ******* ")
        stdscr.addstr(14, 10, "*             * ")
        stdscr.addstr(15, 10, "*             * ")
        stdscr.addstr(16, 10, "*             * ")
        stdscr.addstr(17, 10, "*             * ")

    if hangman > 3:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")
        stdscr.addstr(12, 10, "*             * ")
        stdscr.addstr(13, 10, "*       *************")
        stdscr.addstr(14, 10, "*             * ")
        stdscr.addstr(15, 10, "*             * ")
        stdscr.addstr(16, 10, "*             * ")
        stdscr.addstr(17, 10, "*             * ")

    if hangman > 4:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")
        stdscr.addstr(12, 10, "*             * ")
        stdscr.addstr(13, 10, "*       *************")
        stdscr.addstr(14, 10, "*             * ")
        stdscr.addstr(15, 10, "*             * ")
        stdscr.addstr(16, 10, "*             * ")
        stdscr.addstr(17, 10, "*       ******* ")

    if hangman > 5:
        stdscr.addstr(8,  10, "*           ***** ")
        stdscr.addstr(9,  10, "*           *   * ")
        stdscr.addstr(10, 10, "*           *   * ")
        stdscr.addstr(11, 10, "*           ***** ")
        stdscr.addstr(12, 10, "*             * ")
        stdscr.addstr(13, 10, "*       *************")
        stdscr.addstr(14, 10, "*             * ")
        stdscr.addstr(15, 10, "*             * ")
        stdscr.addstr(16, 10, "*             * ")
        stdscr.addstr(17, 10, "*       *************")


def allLettersGuessed():
    return guessedLetters == splittedWord


def drawWord():
    xPox = 0
    for letter in guessedLetters:
        if letter is None:
            stdscr.addstr(1, xPox, "_")
        else:
            stdscr.addstr(1, xPox, letter)
        xPox += 1


hangman = 0

state = GameState.RUNNING
print("Starting the hangman game")
word = input("Player 1, enter the word that you want Player 2 to guess: ")

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)

# Create a list with the same size as the word, to stored the guessed letters
guessedLetters = []
for _ in range(len(word)):
    guessedLetters.append('_')
splittedWord = list(word)

drawBoard(0)
while state == GameState.RUNNING:
    drawWord()
    guessLetter = stdscr.getkey()
    if guessLetter in word:
        # Reveal letter
        for index, letter in enumerate(splittedWord):
            if letter == guessLetter:
                guessedLetters[index] = letter

        if allLettersGuessed():
            # Player 1 wins
            state = GameState.PLAYER2WINS

    else:
        hangman += 1
        drawBoard(hangman)
        if hangman > 5:
            # Player 1 wins
            state = GameState.PLAYER1WINS

if state == GameState.PLAYER1WINS:
    stdscr.addstr(20, 18, "Player 1 wins!!!!")
else:
    stdscr.addstr(20, 18, "Player 2 wins!!!!")

stdscr.refresh()
time.sleep(2)
curses.endwin()



