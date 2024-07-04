import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        move = input("Enter your move (rock, paper, scissors): ").lower()
        while move not in moves:
            move = input(
                "Invalid move! Please enter 'rock', 'paper', or 'scissors': "
            ).lower()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = None

    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        else:
            self.my_move = moves[(moves.index(self.my_move) + 1) % len(moves)]
        return self.my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins this round!")
        elif beats(move2, move1):
            self.p2_score += 1
            print("Player 2 wins this round!")
        else:
            print("It's a tie!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print(f"Score: Player 1: {self.p1_score}  Player 2: {self.p2_score }")

        print("Game over!")
        print(f"Final Score: Player 1: {self.p1_score}  Player 2: {self.p2_score}")


if __name__ == "__main__":
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
