import sqlite3

def connect_db():
    '''Connect to the SQLite database.'''
    try:
        conn = sqlite3.connect('bakery.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def create_table():
    '''Create a users table in the SQLite database.'''
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT NOT NULL,
                          password TEXT NOT NULL)''')
        conn.commit()
        conn.close()
