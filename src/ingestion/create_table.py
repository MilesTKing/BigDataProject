import sqlite3

connection = sqlite3.connect('chess_data.db')
cursor = connection.cursor()
try:
    connection.execute("DROP TABLE games")
    connection.execute("CREATE TABLE games("
                       "id INTEGER PRIMARY KEY, "
                       "site_id INTEGER NOT NULL, "
                       "date TEXT, "
                       "white_id INTEGER, "
                       "black_id INTEGER, "
                       "white_elo INTEGER NOT NULL, "
                       "black_elo INTEGER NOT NULL, "
                       "result TEXT NOT NULL, "
                       "termination_condition TEXT NOT NULL, "
                       "time_control TEXT NOT NULL, "
                       "opening_ECO TEXT, "
                       "moves BLOB NOT NULL)")
except Exception as e:
    print(e)
else:
    print("Table created successfully")