import sqlite3
from .config_parser import Config

class Database:

    def __init__(self):
        self.open()

    def initialise(self):
        operation = '''CREATE TABLE ims (events_as_ics TEXT)'''
        self.cursor.execute(operation)

        self.commit()

    def insert_ics(self, ics):
        operation = '''DELETE FROM ims'''
        self.cursor.execute(operation)

        operation = '''INSERT INTO ims (events_as_ics) VALUES (?)'''
        self.cursor.execute(operation, (ics,))

    def close(self):
        self.connection.close()

    def open(self):
        config = Config()

        self.connection = sqlite3.connect(config.get('SQLITE3', 'Path'))

        self.cursor = self.connection.cursor()

    def get_ics(self):
        operation = '''SELECT * FROM ims ORDER BY rowid DESC LIMIT 1'''
        return self.cursor.execute(operation).fetchall()[0][0]

    def commit(self):
        while True:
            try:
                self.connection.commit()
                break
            except sqlite3.OperationalError:
                print("Database locked, trying again")
