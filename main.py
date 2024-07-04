import random
from typing import List, Tuple, Dict

# ANSI escape codes for colors and cursor control
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[31m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_BLUE = "\033[34m"
COLOR_MAGENTA = "\033[35m"
COLOR_CYAN = "\033[36m"
COLOR_WHITE = "\033[37m"
CURSOR_UP_ONE = "\033[A"
ERASE_LINE = "\033[K"

moves = ["rock", "paper", "scissors"]

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
        (one == "rock" and two == "scissors") or
        (one == "scissors" and two == "paper") or
        (one == "paper" and two == "rock")
    )

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
        move = input(f"{COLOR_CYAN}{self.name}, enter your move (rock, paper, scissors): {COLOR_RESET}").lower()
        while move not in moves:
            move = input(f"{COLOR_RED}Invalid move! Please enter 'rock', 'paper', or 'scissors': {COLOR_RESET}").lower()
        print(f"{CURSOR_UP_ONE}{ERASE_LINE}", end="")  # Move cursor up and clear the line
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
        print(f"{COLOR_YELLOW}{self.p1.name}: {move1}{COLOR_RESET}  {COLOR_MAGENTA}{self.p2.name}: {move2}{COLOR_RESET}")

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
            print(f"{COLOR_GREEN}Result: {self.p1.name} wins the game with score {self.p1_score} to {self.p2_score}{COLOR_RESET}")
            return 1
        elif self.p2_score > self.p1_score:
            print(f"{COLOR_GREEN}Result: {self.p2.name} wins the game with score {self.p2_score} to {self.p1_score}{COLOR_RESET}")
            return -1
        else:
            print(f"{COLOR_BLUE}Result: The game is a tie with both players scoring {self.p1_score}{COLOR_RESET}")
            return 0

class Tournament:
    """
    Class to represent a tournament between multiple players.
    
    Attributes:
    - players (List[Player]): A list of players participating in the tournament.
    - results (Dict[str, int]): A dictionary to store the results of the tournament.
    """
    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self.results = {player.name: 0 for player in players}

    def play_tournament(self) -> None:
        """Plays the tournament by shuffling and playing all matchups."""
        matchups = self.create_matchups()
        random.shuffle(matchups)
        self.display_matchups(matchups)
        self.play_all_games(matchups)
        self.announce_winner()

    def create_matchups(self) -> List[Tuple[Player, Player]]:
        """Creates all possible matchups."""
        return [(self.players[i], self.players[j]) for i in range(len(self.players)) for j in range(i + 1, len(self.players))]

    def display_matchups(self, matchups: List[Tuple[Player, Player]]) -> None:
        """Displays all matchups."""
        print(f"{COLOR_CYAN}Tournament Matchups:{COLOR_RESET}")
        for p1, p2 in matchups:
            print(f"{p1.name} vs {p2.name}")
        print(f"\n{COLOR_CYAN}Starting Tournament...{COLOR_RESET}\n")

    def play_all_games(self, matchups: List[Tuple[Player, Player]]) -> None:
        """Plays all games in the tournament."""
        for p1, p2 in matchups:
            print(f"{COLOR_YELLOW}Next game: {p1.name} vs {p2.name}{COLOR_RESET}")
            game = Game(p1, p2)
            result = game.play_game()
            self.update_results(result, p1, p2)

    def update_results(self, result: int, p1: Player, p2: Player) -> None:
        """Updates the tournament results based on the game result."""
        if result == 1:
            self.results[p1.name] += 1
        elif result == -1:
            self.results[p2.name] += 1

    def announce_winner(self) -> None:
        """Announces the winner of the tournament."""
        print(f"{COLOR_CYAN}Tournament Results:{COLOR_RESET}")
        max_score = max(self.results.values())
        winners = [player for player, score in self.results.items() if score == max_score]

        for player, score in self.results.items():
            print(f"{player}: {score} wins")

        if len(winners) == 1:
            print(f"{COLOR_GREEN}The overall winner is: {winners[0]}{COLOR_RESET}")
        else:
            print(f"{COLOR_GREEN}The winners are: {', '.join(winners)}{COLOR_RESET}")

def get_player_choice(player_number: int) -> Player:
    """
    Prompts the user to choose the player type and enter the player's name.
    
    Args:
    - player_number (int): The player's number.
    
    Returns:
    - Player: The created player.
    """
    print(f"Configuring Player {player_number}")
    name = input("Enter the name of the player: ")
    print("Choose player type:\n1. Human\n2. RandomPlayer\n3. ReflectPlayer\n4. CyclePlayer")
    choice = input("Enter your choice (1-4): ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid choice! Please enter a number between 1 and 4: ")
    return create_player(choice, name)

def create_player(choice: str, name: str) -> Player:
    """
    Creates a player based on the user's choice.
    
    Args:
    - choice (str): The choice of player type.
    - name (str): The name of the player.
    
    Returns:
    - Player: The created player.
    """
    if choice == "1":
        return HumanPlayer(name)
    elif choice == "2":
        return RandomPlayer(name)
    elif choice == "3":
        return ReflectPlayer(name)
    elif choice == "4":
        return CyclePlayer(name)

def main() -> None:
    """Main function to run the tournament."""
    num_players = int(input("Enter the number of players: "))
    players = [get_player_choice(i) for i in range(1, num_players + 1)]
    tournament = Tournament(players)
    tournament.play_tournament()

if __name__ == "__main__":
    main()
