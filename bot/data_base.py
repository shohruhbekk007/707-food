import sqlite3


def Food_Sql():
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()
        sqlite_select_query = """SELECT * FROM telegram_bot_taomlar"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def Menyu_Sql():
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * FROM telegram_bot_menyu"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def Ichimliklar():
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * FROM telegram_bot_taomlar Where taom_tur_id = 2"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()


def Taomlar():
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * FROM telegram_bot_taomlar Where taom_tur_id = 1"""
        cursor.execute(sqlite_select_query)
        totalRows = cursor.fetchall()
        cursor.close()
        return totalRows

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()



def UsersAdd(title, phone_number, telegram_id, username):
    try:
        sqliteConnection = sqlite3.connect('../db.sqlite3')
        cursor = sqliteConnection.cursor()

        sqlite_insert_query = """
        INSERT INTO telegram_bot_users (title, phone_number, telegram_id, username) 
                                 VALUES (?, ?, ?, ?)
        ON CONFLICT(telegram_id) DO UPDATE SET
        title=excluded.title,
        phone_number=excluded.phone_number,
        username=excluded.username
        """
        cursor.execute(sqlite_insert_query, (title, phone_number, telegram_id, username))

        sqliteConnection.commit()
        print("Record inserted/updated successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
