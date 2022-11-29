import sqlite3


def create_tables():
    create_cw_table = "CREATE TABLE current_weather (ID integer PRIMARY KEY, date TEXT, time TEXT, temp TEXT)"
    sql_put(create_cw_table)
    create_history_table = "CREATE TABLE history(date TEXT, temp TEXT)"
    sql_put(create_history_table)

    sqlite_insert = f"""INSERT INTO current_weather(date, time, temp) VALUES ("30.11.2022", "0:10", "-11.18")"""
    sql_put(sqlite_insert)


def sql_put(sqlite_insert: str):
    sqlite_connection = sqlite3.connect('weather_db')
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_insert)
    sqlite_connection.commit()
    cursor.close()


def sql_get(sqlite_select: str):
    sqlite_connection = sqlite3.connect('weather_db')
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_select)
    return cursor.fetchall()


def get_last_temp():
    sqlite_select = "SELECT * from current_weather WHERE id=(SELECT max(id) FROM current_weather)"
    weather = sql_get(sqlite_select)
    return weather[0]


def put_temp(date: str, time: str, temp: str):
    sqlite_insert = f"""INSERT INTO current_weather(date, time, temp) VALUES ("{date}", "{time}", "{temp}")"""
    sql_put(sqlite_insert)


def get_history():
    sqlite_select = "SELECT * from history"
    temps = sql_get(sqlite_select)
    return temps


def get_all_values(date: str):
    sqlite_connection = sqlite3.connect('weather_db')
    cursor = sqlite_connection.cursor()
    cursor.row_factory = lambda sq_cursor, row: row[0]
    sqlite_select = f"""SELECT temp from current_weather WHERE date='{date}'"""
    cursor.execute(sqlite_select)
    temps = cursor.fetchall()
    return temps


def update_average(date: str, temp: str):
    sqlite_insert = f"SELECT * FROM history WHERE date = '{date}'"
    history = sql_get(sqlite_insert)
    if not history:
        sqlite_upsert = f"INSERT INTO history VALUES ('{date}', '{temp}')"
        print('gtnz')
    else:
        sqlite_upsert = f"UPDATE history SET temp='{temp}' WHERE date = '{date}'"
        print("петя")
    sql_put(sqlite_upsert)
