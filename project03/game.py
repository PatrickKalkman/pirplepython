import random
import functools as ft


class Stack:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def clear(self):
        self.cards.clear()


class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def combine(self, card1, card2):
        return card1 + card2 + '\n'

    def __str__(self):
        return ft.reduce(self.combine, self.cards)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value}:{self.suit}"


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def get_card(self, card_string):
        return self.hand[0]


class Rules:

    def __init__(self):
        self.rules = ""

    def read_rules(self):
        with open("cheatrules.txt", "r") as file:
            self.rules = file.readlines()

    def __str__(self):
        return ''.join(self.rules)
