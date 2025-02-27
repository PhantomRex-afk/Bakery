import sqlite3
from tkinter import messagebox

def connect_db():
    '''Connect to the SQLite database.'''
    try:
        conn = sqlite3.connect('bakery.db')  # Replace with your DB filename
        return conn
    except sqlite3.Error as e:
        messagebox.showerror('Database Error', f"Failed to connect: {e}")
        return None

def create_db():
    '''Create the database and tables if they don't exist.'''
    conn = connect_db()  # Use the connect_db function to establish a connection
    if conn:
        cursor = conn.cursor()
        # Create the Bakery table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bakery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            role TEXT NOT NULL,
            gender TEXT NOT NULL
        )
        ''')

        # Create the users table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        ''')

        conn.commit()  # Commit the changes to the database
        conn.close()   # Close the connection

# Call the create_db function to create tables if necessary
create_db()
