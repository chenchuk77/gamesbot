import mysql.connector


game_types=['NL', 'PLO', 'PLO5', 'PLO6']


class Game:
    def __init__(self, game_type, buyin_string):
        # def __init__(self, game_type, buyin_string, is_bounty=False, prize=0):

        self.game_type = game_type
        self.buyin_string = buyin_string

        self.is_bounty = buyin_string.count('+') == 2
        # self.is_bounty = is_bounty
        self.prize = 0
        self.db = self.connect_to_db()

    def connect_to_db(self):
        db = mysql.connector.connect(
            host="localhost",  # replace with your host name if not running on localhost
            user="user",  # updated username
            password="password",  # replace with your MySQL password
            database="db"  # updated database name
        )
        return db

    def save_to_db(self):
        cursor = self.db.cursor()
        query = "INSERT INTO games (game_type, buyin_string, is_bounty, prize) VALUES (%s, %s, %s, %s)"
        values = (self.game_type, self.buyin_string, self.is_bounty, self.prize)
        cursor.execute(query, values)
        self.db.commit()
        return cursor.lastrowid

    @staticmethod
    def get_from_db(game_type):
        db = Game("", "").connect_to_db()  # create a dummy Game instance to connect to the database
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM games WHERE game_type=%s"
        values = (game_type,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        if result:
            return Game(result['game_type'], result['buyin_string'], result['is_bounty'], result['prize'])
        else:
            return None
