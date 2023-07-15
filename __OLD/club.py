import mysql.connector
from game import Game  # import the Game class

class Club:
    def __init__(self, name, balance, owner_phone, games):
        self.name = name
        self.balance = balance
        self.owner_phone = owner_phone
        self.games = games  # this should be a list of Game objects
        self.db = self.connect_to_db()

    def connect_to_db(self):
        db = mysql.connector.connect(
            host="localhost",  # replace with your host name if not running on localhost
            user="user",  # replace with your MySQL username
            password="password",  # replace with your MySQL password
            database="db"  # replace with your database name
        )
        return db

    def save_to_db(self):
        cursor = self.db.cursor()
        # assuming games is a string column that stores the names of games
        games_names = ', '.join([game.name for game in self.games])
        query = "INSERT INTO clubs (name, balance, owner_phone, games) VALUES (%s, %s, %s, %s)"
        values = (self.name, self.balance, self.owner_phone, games_names)
        cursor.execute(query, values)
        self.db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_from_db(club_name):
        db = Club("", 0, "", []).connect_to_db()  # create a dummy Club instance to connect to the database
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM clubs WHERE name=%s"
        values = (club_name,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            # assuming games is a string column that stores the names of games
            games = [Game.get_from_db(name) for name in result['games'].split(', ')]
            return Club(result['name'], result['balance'], result['owner_phone'], games)
        else:
            return None
