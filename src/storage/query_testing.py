import sqlite3

connection = sqlite3.connect('chess_data.db')
result = connection.execute("SELECT * FROM games")
for game in result:
    print(game)