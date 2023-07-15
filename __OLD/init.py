import mysql.connector

def create_tables():
    db = mysql.connector.connect(
        host="localhost",
        user="user",
        password="password",
        database="db"
    )

    cursor = db.cursor()

    # Create table 'clubs'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            balance DECIMAL(10, 2),
            owner_phone VARCHAR(15),
            games VARCHAR(255)
        )
    """)

    # Create table 'games'
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id INT AUTO_INCREMENT PRIMARY KEY,
            game_type VARCHAR(255) NOT NULL,
            buyin_string VARCHAR(255),
            is_bounty BOOLEAN DEFAULT FALSE,
            prize INT DEFAULT 0
        )
    """)

    print("Tables 'clubs' and 'games' created successfully.")

create_tables()
