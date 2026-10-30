import sqlite3
import hashlib

class Database:

    def __init__(self):
        self.conn = sqlite3.connect(
            "tasks.db",
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT
            )
        """)

        self.conn.commit()

    def login(self, username, password):

        # check if the user exists
        self.cursor.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        )

        user = self.cursor.fetchone()

        if user:
            password_hash = hashlib.md5(
                password.encode()
            ).hexdigest()

            if password_hash == user[2]:
                return True

        return False

    def get_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def add_task(self, task):
        self.cursor.execute(
            "INSERT INTO tasks (task) VALUES (?)",
            (task,)
        )

        self.conn.commit()

    def create_admin(self):

        username = "admin"

        # temporary admin password
        password_md5 = "5fcfd41e547a12215b173ff47fdd3739"


        self.cursor.execute(
            "INSERT INTO users (username, password_md5) VALUES (?, ?)",
            (username, password)
        )

        self.conn.commit()
