import sqlite3
from datetime import datetime

# Create connection to the database file
def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Create the scores table if it doesn't exist
def create_table(conn):
    """Create scores table"""
    try:
        sql_create_scores_table = """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
        );
        """
        conn.execute(sql_create_scores_table)
    except sqlite3.Error as e:
        print(e)

# Store the player's score
def save_score(conn, name, score):
    """Save the player's score to the database"""
    sql = """INSERT INTO scores(name, score, date)
             VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, (name, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    return cur.lastrowid

# Retrieve all previous scores
def get_all_scores(conn):
    """Query all rows in the scores table"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM scores ORDER BY score DESC")
    return cur.fetchall()

# ==============================
# Game starts here
print("Welcome to AskPython Quiz")

answer = input("Are you ready to play the Quiz? (yes/no): ")
score = 0
total_questions = 3

if answer.lower() == "yes":
    # Question 1
    if input("Question 1: What is your Favourite programming language? ").lower() == "python":
        score += 1
        print("Correct!")
    else:
        print("Wrong Answer :(")

    # Question 2
    if input("Question 2: Do you follow any author on AskPython? ").lower() == "yes":
        score += 1
        print("Correct!")
    else:
        print("Wrong Answer :(")

    # Question 3
    if input("Question 3: What is the name of your favourite website for learning Python? ").lower() == "askpython":
        score += 1
        print("Correct!")
    else:
        print("Wrong Answer :(")

    print(f"\nThank you for playing! You answered {score} questions correctly.")
    mark = int((score / total_questions) * 100)
    print(f"Marks obtained: {mark}%")

    player_name = input("Enter your name: ")
    database = "quiz_game.db"

    conn = create_connection(database)
    if conn:
        create_table(conn)  # ✅ ensures the table exists
        save_score(conn, player_name, score)

        print("\nPrevious scores:")
        for row in get_all_scores(conn):
            print(f"Name: {row[1]}, Score: {row[2]}, Date: {row[3]}")

        conn.close()
    else:
        print("Error! Cannot create the database connection.")
else:
    print("Please, when you're ready, enter the game again.")

print("BYE!")
