import random

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
        self.their_move: str = None

    def move(self) -> str:
        return random.choice(moves) if self.their_move is None else self.their_move

    def learn(self, my_move: str, their_move: str) -> None:
        self.their_move = their_move


class CyclePlayer(Player):
    """Player that cycles through the moves."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.my_move: str = None

    def move(self) -> str:
        if self.my_move is None:
            self.my_move = random.choice(moves)
        else:
            self.my_move = moves[(moves.index(self.my_move) + 1) % 3]
        return self.my_move
