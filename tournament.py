import random
from typing import List, Tuple
from costants import COLOR_CYAN, COLOR_RESET, COLOR_YELLOW, COLOR_GREEN
from game import Game
from logger import DataLogger
from players import Player


class Tournament:
    """
    Class to represent a tournament between multiple players.

    Attributes:
    - players (List[Player]): A list of players participating in the tournament.
    - results (Dict[str, int]): A dictionary to store the results of the tournament.
    """

    def __init__(self, players: List[Player], games_per_matchup: int = 5, rounds_per_game: int = 3) -> None:
        self.players = players
        self.results = {player.name: 0 for player in players}
        self.games_per_matchup = games_per_matchup
        self.rounds_per_game = rounds_per_game
        self.logger = DataLogger()



    def play_tournament(self) -> None:
        """Plays the tournament by shuffling and playing all matchups."""
        matchups = self.create_matchups()
        random.shuffle(matchups)
        self.display_matchups(matchups)
        self.play_all_games(matchups)
        self.announce_winner()

    def create_matchups(self) -> List[Tuple[Player, Player]]:
        """Creates all possible matchups."""
        return [
            (self.players[i], self.players[j])
            for i in range(len(self.players))
            for j in range(i + 1, len(self.players))
        ]

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
            for _ in range(self.games_per_matchup):
                game = Game(p1, p2, self.rounds_per_game, self.logger)
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
        winners = [
            player for player, score in self.results.items() if score == max_score
        ]

        for player, score in self.results.items():
            print(f"{player}: {score} wins")

        if len(winners) == 1:
            print(f"{COLOR_GREEN}The overall winner is: {winners[0]}{COLOR_RESET}")
        else:
            print(f"{COLOR_GREEN}The winners are: {', '.join(winners)}{COLOR_RESET}")
