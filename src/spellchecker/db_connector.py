import sqlite3


def get_db_connection():
    try:
        sqlite_connection = sqlite3.connect('SQLite_Python.db')
        cursor = sqlite_connection.cursor()
        print("Database created and Successfully Connected to SQLite")

        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        cursor.close()
        return sqlite_connection
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def create__request_history_table():
    connection = None
    try:
        connection = get_db_connection()
        sqlite_create_table_query = '''CREATE TABLE REQUEST_HISTORY (
                                    request_id TEXT NOT NULL PRIMARY KEY,
                                    request_date text datetime,
                                    request_text TEXT NOT NULL,
                                    request_response TEXT NOT NULL
                                    );'''

        cursor = connection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        connection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("sqlite connection is closed")


def insert_row_into_request_history(request_id, request_date, request_text, request_response):
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO REQUEST_HISTORY
                              (request_id, request_date, request_text, request_response) 
                               VALUES (?, ?, ?, ?)"""

        data_tuple = (request_id, request_date, request_text, request_response)
        cursor.execute(sqlite_insert_query, data_tuple)
        connection.commit()
        print("Python Variables inserted successfully into request_history table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")


def get_all_rows_from_request_registry():
    connection = None
    try:
        keys = ["request_id", "request_date", "request_text", "request_response"]
        connection = get_db_connection()
        cursor = connection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from REQUEST_HISTORY"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return [dict(zip(keys, record)) for record in records]
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if connection:
            connection.close()
            print("The SQLite connection is closed")
