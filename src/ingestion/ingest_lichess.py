import chess.pgn as chess
import sqlite3

connection = sqlite3.connect('chess_data.db')
cursor = connection.cursor()


with open("../../data/raw/lichess.pgn") as f:
    for line in range(10):
        game = chess.read_game(f)