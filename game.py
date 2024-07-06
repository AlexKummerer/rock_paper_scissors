from costants import COLOR_BLUE, COLOR_MAGENTA, COLOR_RESET, COLOR_YELLOW, COLOR_GREEN
from players import Player


def beats(one: str, two: str) -> bool:
    """
    Determines if move 'one' beats move 'two'.

    Args:
    - one (str): The move of the first player.
    - two (str): The move of the second player.

    Returns:
    - bool: True if 'one' beats 'two', otherwise False.
    """
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


class Game:
    """
    Class to represent a game between two players.

    Attributes:
    - p1 (Player): The first player.
    - p2 (Player): The second player.
    - p1_score (int): The score of the first player.
    - p2_score (int): The score of the second player.
    """

    def __init__(self, p1: Player, p2: Player) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self) -> None:
        """Plays a single round of the game."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        self.display_moves(move1, move2)
        self.update_scores(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def display_moves(self, move1: str, move2: str) -> None:
        """Displays the moves of both players."""
        print(
            f"{COLOR_YELLOW}{self.p1.name}: {move1}{COLOR_RESET}  {COLOR_MAGENTA}{self.p2.name}: {move2}{COLOR_RESET}"
        )

    def update_scores(self, move1: str, move2: str) -> None:
        """Updates the scores based on the moves."""
        if beats(move1, move2):
            self.p1_score += 1
            print(f"{COLOR_GREEN}{self.p1.name} wins this round!{COLOR_RESET}")
        elif beats(move2, move1):
            self.p2_score += 1
            print(f"{COLOR_GREEN}{self.p2.name} wins this round!{COLOR_RESET}")
        else:
            print(f"{COLOR_BLUE}It's a tie!{COLOR_RESET}")

    def play_game(self) -> int:
        """Plays a full game of 3 rounds."""
        for _ in range(3):
            self.play_round()
        return self.get_result()

    def get_result(self) -> int:
        """Gets the result of the game."""
        if self.p1_score > self.p2_score:
            print(
                f"{COLOR_GREEN}Result: {self.p1.name} wins the game with score {self.p1_score} to {self.p2_score}{COLOR_RESET}"
            )
            return 1
        elif self.p2_score > self.p1_score:
            print(
                f"{COLOR_GREEN}Result: {self.p2.name} wins the game with score {self.p2_score} to {self.p1_score}{COLOR_RESET}"
            )
            return -1
        else:
            print(
                f"{COLOR_BLUE}Result: The game is a tie with both players scoring {self.p1_score}{COLOR_RESET}"
            )
            return 0
