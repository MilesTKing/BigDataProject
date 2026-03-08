import chess.pgn as chess
 
with open("../../data/raw/lichess.pgn") as f:
    for line in range(5):
        game = chess.read_game(f)