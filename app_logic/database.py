import sqlite3

def get_connection():
    return sqlite3.connect('niolingo_db.db')

def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            tg_id INTEGER UNIQUE NOT NULL,
            registred TEXT DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    # Dictionary table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
            user_id INTEGER,
            id INTEGER PRIMARY KEY,
            type TEXT NOT NULL,
            spelling TEXT,
            transcription TEXT,
            meaning TEXT,
            added_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id) REFERENCES Users (id)
        );
    ''')
    connection.commit()
    connection.close()

#___________________________________________________________________
#____________________________Items__________________________________
#___________________________________________________________________
def add_item(item):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Items (id, type, spelling, transcription, meaning, user_id)
        VALUES (NULL, ?, ?, ?, ?, ?);
    ''', (item.type, item.spelling, item.transcription, item.meaning, item.user_id))
    connection.commit()
    connection.close()

def remove_item(item_id, user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM Items
        WHERE id = ? AND user_id = ?;
    ''', (item_id, user_id))
    connection.commit()
    connection.close()

def update_item(item_id, new_item, user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE Items
        SET type = ?, spelling = ?, transcription = ?, meaning = ?
        WHERE id = ? AND user_id = ?;
    ''', (new_item.type, new_item.spelling, new_item.transcription, new_item.meaning, item_id, user_id))
    connection.commit()
    connection.close()

def get_item(param, user_id):
    connection = get_connection()
    cursor = connection.cursor()
    if param:
        cursor.execute('''
            SELECT id, type, spelling, transcription, meaning, added_at
            FROM Items
            WHERE (spelling = ? OR meaning = ?) AND user_id = ?;
        ''', (param, param))
    else:
        cursor.execute('''
            SELECT *
            FROM Items
            WHERE user_id = ?;
        ''', (user_id))
    rows = cursor.fetchall()
    connection.close()
    return rows

#___________________________________________________________________
#____________________________Users__________________________________
#___________________________________________________________________
def add_user(user):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO Users (id, tg_id, registred)
        VALUES (NULL, ?, ?);
    ''', (user.tg_id, user.registred))
    connection.commit()
    connection.close()