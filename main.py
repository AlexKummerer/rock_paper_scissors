import random

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


class Player:
    def __init__(self, name):
        self.name = name

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
    def __init__(self, name):
        super().__init__(name)
        self.their_move = None

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.my_move = None

    def move(self):
        if self.my_move is None:
            self.my_move = random.choice(moves)
        else:
            self.my_move = moves[(moves.index(self.my_move) + 1) % 3]
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
        print(
            f"{COLOR_YELLOW}{self.p1.name}: {move1}{COLOR_RESET}  {COLOR_MAGENTA}{self.p2.name}: {move2}{COLOR_RESET}"
        )
        if beats(move1, move2):
            self.p1_score += 1
            print(f"{COLOR_GREEN}{self.p1.name} wins this round!{COLOR_RESET}")
        elif beats(move2, move1):
            self.p2_score += 1
            print(f"{COLOR_GREEN}{self.p2.name} wins this round!{COLOR_RESET}")
        else:
            print(f"{COLOR_BLUE}It's a tie!{COLOR_RESET}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        for _ in range(3):
            self.play_round()
        if self.p1_score > self.p2_score:
            result = 1
            print(
                f"{COLOR_GREEN}Result: {self.p1.name} wins the game with score {self.p1_score} to {self.p2_score}{COLOR_RESET}"
            )
        elif self.p2_score > self.p1_score:
            result = -1
            print(
                f"{COLOR_GREEN}Result: {self.p2.name} wins the game with score {self.p2_score} to {self.p1_score}{COLOR_RESET}"
            )
        else:
            result = 0
            print(
                f"{COLOR_BLUE}Result: The game is a tie with both players scoring {self.p1_score}{COLOR_RESET}"
            )
        return result


class Tournament:
    def __init__(self, players):
        self.players = players
        self.results = {player.name: 0 for player in players}

    def play_tournament(self):
        matchups = [
            (self.players[i], self.players[j])
            for i in range(len(self.players))
            for j in range(i + 1, len(self.players))
        ]
        random.shuffle(matchups)
        print(f"{COLOR_CYAN}Tournament Matchups:{COLOR_RESET}")
        for p1, p2 in matchups:
            print(f"{p1.name} vs {p2.name}")
        print(f"\n{COLOR_CYAN}Starting Tournament...{COLOR_RESET}\n")
        for p1, p2 in matchups:
            print(f"{COLOR_YELLOW}Next game: {p1.name} vs {p2.name}{COLOR_RESET}")
            game = Game(p1, p2)
            result = game.play_game()
            if result == 1:
                self.results[p1.name] += 1
            elif result == -1:
                self.results[p2.name] += 1
        self.announce_winner()

    def announce_winner(self):
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


def get_player_choice(player_number):
    print(f"Configuring Player {player_number}")
    name = input("Enter the name of the player: ")
    print("Choose player type:")
    print("1. Human")
    print("2. RandomPlayer")
    print("3. ReflectPlayer")
    print("4. CyclePlayer")
    choice = input("Enter your choice (1-4): ")
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid choice! Please enter a number between 1 and 4: ")
    if choice == "1":
        return HumanPlayer(name)
    elif choice == "2":
        return RandomPlayer(name)
    elif choice == "3":
        return ReflectPlayer(name)
    elif choice == "4":
        return CyclePlayer(name)


if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(1, num_players + 1):
        players.append(get_player_choice(i))
    tournament = Tournament(players)
    tournament.play_tournament()
