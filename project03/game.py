import random


class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += card.__str__() + '\n'
        return deck_string


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
