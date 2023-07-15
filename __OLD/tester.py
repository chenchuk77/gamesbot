from game import Game
from club import Club
from init import create_tables

create_tables()

# Creating clubs
c1 = Club("c1", 1000, "1234567890", [])
c2 = Club("c2", 2000, "0987654321", [])
c3 = Club("c3", 1500, "1122334455", [])

# Saving clubs to the database
c1.save_to_db()
c2.save_to_db()
c3.save_to_db()

# Creating games
game1 = Game("NL", "150+150+25")
game2 = Game("PLO", "100+20")

# Saving games to the database
game1.save_to_db()
game2.save_to_db()

# # Updating c1's games list and saving it to the database
# c1.games = [game1, game2]
# c1.save_to_db()
