import sqlite3

connection = sqlite3.connect('chess_data.db')
cursor = connection.cursor()
connection.execute("CREATE TABLE games("
                   "id INTEGER PRIMARY KEY, "
                   "site_id INTEGER NOT NULL, "
                   "date TEXT, "
                   "white_id INTEGER, "
                   "black_id INTEGER, "
                   "white_elo INTEGER NOT NULL, "
                   "black_elo INTEGER NOT NULL, "
                   "result TEXT NOT NULL, "
                   "time_control TEXT NOT NULL, "
                   "opening_ECO TEXT, "
                   "moves BLOB NOT NULL)")