"""
Python Is Easy course @Pirple.com
Project #3: Pick a Card Game!
Patrick Kalkman / patrick@simpletechture.nl

Details:

Everyone has their favorite card game. What's yours? For this assignment,
choose a card game (other than Blackjack), and turn it into a Python program.
It doesn't matter if it's a 1-player game, or a 2 player game, or more!
That's totally up to you. A few requirements:

It's got to be a card game (no board games, etc)
When the game starts up, you should ask for the players' names.
And after they enter their names, your game should refer to them by name only.
("It's John's turn" instead of "It's player 1's turn).
At any point during the game, someone should be able to type "--help" to be
taken to a screen where they can read the rules of the game and instructions
for how to play. After they're done reading, they should be able to type
"--resume" to go back to the game and pick up where they left off.

Extra Credit:

Want to make this much much harder on yourself? Okay, you asked for it!

For extra credit, allow 2 players to play on two different computers that are
on the same network. Two people should be able to start identical versions of
your program, and enter the internal IP address of the user on the network who
they want to play against. The two applications should communicate with each
other, across the network using simple HTTP requests. Try this library to send
requests:

http://docs.python-requests.org/en/master/
http://docs.python-requests.org/en/master/user/quickstart/

And try Flask to receive them:

http://flask.pocoo.org/

The 2-player game should only start if one person has challenged the other
(by entering their internal IP address), and the 2nd person has accepted
the challenge. The exact flow of the challenge mechanism is up to you.

"""

from enum import Enum

from game import Deck, Player, Rules, Stack


class GameEngine:
    class States(Enum):
        INIT = 1
        PLAYING = 2
        FINISHED = 3

    def __init__(self):
        self.state = self.States.INIT
        self.current_player_index = 0
        self.players = []
        self.deck = Deck()
        self.rules = Rules()
        self.stack = Stack()
        self.cheat_card = ""

    def initialize_game(self):
        self.deck.build()
        self.deck.shuffle()
        self.rules.read_rules()

    def create_players(self):
        number_players = int(input("Enter the number of players? "))
        for player_number in range(1, number_players + 1):
            player_question = f"Enter the name of player{player_number}? "
            name = input(player_question)
            self.players.append(Player(name))

    def current_player(self):
        return self.players[self.current_player_index]

    def deal_cards(self):
        player_index = 0
        for card in self.deck.cards:
            self.players[player_index].hand.append(card)
            player_index += 1
            if player_index >= len(self.players):
                player_index = 0

    def next_player(self):
        if self.current_player().no_more_cards():
            print(f"{self.current_player().name} won the game!!!!!")
            self.state = self.States.FINISHED

        self.current_player_index += 1
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def previous_player(self):
        if self.current_player_index > 0:
            return self.players[self.current_player_index - 1]
        else:
            return self.players[len(self.players) - 1]

    def print_rules(self):
        print(self.rules)

    def game_loop(self):
        while self.state != self.States.FINISHED:
            if self.state == self.States.INIT:
                self.create_players()
                self.deal_cards()
                self.state = self.States.PLAYING

            print(f"{self.current_player().name} it is your turn")
            print(self.stack)
            print(self.current_player())

            command = input((f"What do you want to do?" " (help, playcard, cheater) "))

            if command == "help":
                self.print_rules()
            elif command == "playcard":
                call_card = input("Which card do you want to play? ")
                if self.current_player().has_card(call_card):
                    card = self.current_player().get_card(call_card)
                    self.stack.add_card(card)
                    self.cheat_card = input(
                        ("What card do you " "want to say you " "played? ")
                    )
                    self.next_player()
                else:
                    print("You don't have that card")
            elif command == "cheater":
                lastcard = self.stack.get_last_card()
                print(f"Last card was: {lastcard}")
                if self.cheat_card == str(lastcard):
                    print(
                        (
                            f"No, {self.previous_player().name} did not cheat, "
                            "you will get all the played cards"
                        )
                    )
                    played_cards = self.stack.get_cards()
                    self.current_player().add(played_cards)
                    self.stack.clear()
                else:
                    print(
                        (
                            f"Yes, you are right {self.previous_player().name} "
                            f"cheated. {self.previous_player().name} will get "
                            "all played cards"
                        )
                    )
                    played_cards = self.stack.get_cards()
                    self.previous_player().add(played_cards)
                    self.stack.clear()

    def start_game(self):
        self.initialize_game()
        self.game_loop()


game = GameEngine()
game.start_game()
