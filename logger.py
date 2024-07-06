import csv

class DataLogger:
    def __init__(self, filename: str = 'game_data.csv') -> None:
        self.filename = filename
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Round', 'Player1', 'Move1', 'Player2', 'Move2', 'Winner'])

    def log(self, round_num: int, player1: str, move1: str, player2: str, move2: str, winner: str) -> None:
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([round_num, player1, move1, player2, move2, winner])
