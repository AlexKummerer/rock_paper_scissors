import csv
import random
from typing import Dict, Optional

from costants import (
    COLOR_CYAN,
    COLOR_RED,
    COLOR_RESET,
    CURSOR_UP_ONE,
    ERASE_LINE,
    MOVES,
)


moves = MOVES


class Player:
    """
    Base class for all players.

    Attributes:
    - name (str): The name of the player.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def move(self) -> str:
        """
        Returns the player's move. Default is "rock".

        Returns:
        - str: The move of the player.
        """
        return "rock"

    def learn(self, my_move: str, their_move: str) -> None:
        """
        Learns from the opponent's move. No implementation for base class.

        Args:
        - my_move (str): The player's move.
        - their_move (str): The opponent's move.
        """
        pass


class RandomPlayer(Player):
    """Player that chooses a move randomly."""

    def move(self) -> str:
        return random.choice(moves)


class HumanPlayer(Player):
    """Human player that inputs moves."""

    def move(self) -> str:
        move = input(
            f"{COLOR_CYAN}{self.name}, enter your move (rock, paper, scissors): {COLOR_RESET}"
        ).lower()
        while move not in moves:
            move = input(
                f"{COLOR_RED}Invalid move! Please enter 'rock', 'paper', or 'scissors': {COLOR_RESET}"
            ).lower()
        print(
            f"{CURSOR_UP_ONE}{ERASE_LINE}", end=""
        )  # Move cursor up and clear the line
        return move


class ReflectPlayer(Player):
    """Player that reflects the opponent's last move."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.their_move: Optional[str] = None

    def move(self) -> str:
        return random.choice(moves) if self.their_move is None else self.their_move

    def learn(self, my_move: str, their_move: str) -> None:
        self.their_move = their_move

class CyclePlayer(Player):
    """Player that cycles through the moves."""
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.move_index = 0

    def move(self) -> str:
        move = moves[self.move_index]
        self.move_index = (self.move_index + 1) % len(moves)
        return move



class AIPlayer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.transition_matrix: Dict[str, Dict[str, Dict[str, int]]] = {
            move1: {move2: {move3: 0 for move3 in moves} for move2 in moves} for move1 in moves
        }
        self.last_move: Optional[str] = None
        self.second_last_move: Optional[str] = None
        self.load_data("game_data.csv")

    def move(self) -> str:
        if not self.last_move or not self.second_last_move or not any(self.transition_matrix[self.second_last_move][self.last_move].values()):
            return random.choice(moves)
        predicted_move = max(self.transition_matrix[self.second_last_move][self.last_move], key=self.transition_matrix[self.second_last_move][self.last_move].get)
        return self.counter_move(predicted_move)

    def learn(self, my_move: str, their_move: str) -> None:
        if self.second_last_move and self.last_move:
            self.transition_matrix[self.second_last_move][self.last_move][their_move] += 1
        self.second_last_move = self.last_move
        self.last_move = their_move

    def counter_move(self, predicted_move: str) -> str:
        return {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }[predicted_move]

    def load_data(self, filename: str) -> None:
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    move1, move2 = row["Move1"], row["Move2"]
                    second_last_move = row.get("SecondLastMove")
                    if move1 in moves and move2 in moves and second_last_move in moves:
                        self.transition_matrix[second_last_move][move1][move2] += 1
        except FileNotFoundError:
            print(f"No historical data found at {filename}. Starting with an empty transition matrix.")