import functools as ft
import random


# A card that can be played
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return (
            self.suit.lower() == other.suit.lower()
            and self.value.lower() == other.value.lower()
        )

    def __str__(self):
        return f"{self.value}:{self.suit}"


# The Stack contains the cards that each player plays.
class Stack:
    def __init__(self):
        self.cards = []

    def __str__(self):
        stack_cards = f"Stack cards: [{len(self.cards)}] ("
        for card in self.cards:
            stack_cards += f"{card}, "

        stack_cards += ") \n"
        return stack_cards

    def add_card(self, card):
        self.cards.append(card)

    def get_cards(self):
        return self.cards

    def get_last_card(self):
        return self.cards[-1]

    def clear(self):
        self.cards.clear()


# The deck contains all the play cards at the start of the game
class Deck:
    def __init__(self):
        self.cards = []

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, str(value)))

    def shuffle(self):
        random.shuffle(self.cards)

    def combine(self, card1, card2):
        return card1 + card2 + "\n"

    def __str__(self):
        return ft.reduce(self.combine, self.cards)


# The player plays the game
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        player = f"Your cards: [{len(self.hand)}] ("
        for card in self.hand:
            player += f"{card}, "

        player += ") \n"
        return player

    def get_card(self, card_string):
        splitted_card = card_string.split(":")
        if len(splitted_card) != 2:
            return None
        else:
            selected_card = Card(splitted_card[1], splitted_card[0])
            found_card = None
            for card in self.hand:
                if card == selected_card:
                    found_card = card

            self.hand.remove(found_card)
            return found_card

    def has_card(self, card_string):
        splitted_card = card_string.split(":")
        if len(splitted_card) != 2:
            return False
        else:
            card = Card(splitted_card[1], splitted_card[0])
            return any(c for c in self.hand if c == card)

    def add(self, cards):
        self.hand.extend(cards)

    def no_more_cards(self):
        return len(self.hand) == 0


# Read and expose the rules of the game
class Rules:
    def __init__(self):
        self.rules = ""

    def read_rules(self):
        with open("cheatrules.txt", "r") as file:
            self.rules = file.readlines()

    def __str__(self):
        return "".join(self.rules)
