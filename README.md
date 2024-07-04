# Rock, Paper, Scissors Tournament

This Python program simulates a Rock, Paper, Scissors tournament. Players can be human or various types of computer-controlled strategies. The program supports multiple players who compete in a round-robin tournament to determine the overall winner.

## Features

- Multiple player types:
  - **Human Player**: A human player who inputs their move each round.
  - **Random Player**: A computer player that chooses moves randomly.
  - **Reflect Player**: A computer player that mimics the opponent's last move.
  - **Cycle Player**: A computer player that cycles through rock, paper, and scissors.
- Round-robin tournament format
- Colored terminal output for a better user experience
- Input validation and clear input handling

## Requirements

- Python 3.x

## Installation

1. **Clone the repository or download the `rps_tournament.py` file.**

2. **Create a Virtual Environment (recommended):**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```

## How to Play

1. **Run the Program:**

    Execute the following command in the terminal:

    ```bash
    python main.py
    ```

2. **Follow the prompts to configure the number of players and their types.**

3. **The program will simulate the tournament and display the results.**

## Example

```bash
Enter the number of players: 3

Configuring Player 1
Enter the name of the player: Alex
Choose player type:
1. Human
2. RandomPlayer
3. ReflectPlayer
4. CyclePlayer
Enter your choice (1-4): 1

Configuring Player 2
Enter the name of the player: Bot1
Choose player type:
1. Human
2. RandomPlayer
3. ReflectPlayer
4. CyclePlayer
Enter your choice (1-4): 2

Configuring Player 3
Enter the name of the player: Bot2
Choose player type:
1. Human
2. RandomPlayer
3. ReflectPlayer
4. CyclePlayer
Enter your choice (1-4): 3

Tournament Matchups:
Alex vs Bot1
Alex vs Bot2
Bot1 vs Bot2

Starting Tournament...

Next game: Alex vs Bot1
Alex: rock  Bot1: paper
Bot1 wins this round!
Alex: paper  Bot1: rock
Alex wins this round!
Alex: scissors  Bot1: scissors
It's a tie!
Result: The game is a tie with both players scoring 1

Next game: Alex vs Bot2
...

Tournament Results:
Alex: 1 wins
Bot1: 1 wins
Bot2: 1 wins
The overall winner is: Alex, Bot1, Bot2
```

## Code Structure
**Player**: Base class for all players.
**RandomPlayer, HumanPlayer, ReflectPlayer, CyclePlayer**: Classes that define different player behaviors.
**Game**: Class that handles the logic of a single game between two players.
**Tournament**: Class that manages the tournament, including creating matchups and determining the winner.
## License
This project is licensed under the MIT License. See the LICENSE file for details.
