from players import AIPlayer, CyclePlayer, HumanPlayer, Player, RandomPlayer, ReflectPlayer
from tournament import Tournament


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
    print(
         "Choose player type:\n1. Human\n2. RandomPlayer\n3. ReflectPlayer\n4. CyclePlayer\n5. AIPlayer"
    )
    choice = input("Enter your choice (1-5): ")
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Invalid choice! Please enter a number between 1 and 5: ")
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
    elif choice =="5":
        return AIPlayer(name)


def main() -> None:
    """Main function to run the tournament."""
    num_players = int(input("Enter the number of players: "))
    players = [get_player_choice(i) for i in range(1, num_players + 1)]
    tournament = Tournament(players)
    tournament.play_tournament()


if __name__ == "__main__":
    main()
