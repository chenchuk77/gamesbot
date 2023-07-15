from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://user:password@localhost/db', echo=True)

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    game_type = Column(String(255))
    buyin_string = Column(String(255))
    is_bounty = Column(Boolean, default=False)
    prize = Column(Integer, default=None)
    club_id = Column(Integer, ForeignKey('clubs.id'))  # new line
    bullets = Column(Integer, default=None)
    total_buyin = Column(Integer, default=0)  # added this line

    # Updated constructor method

    def __init__(self, game_type, buyin_string, club):
        def is_bounty(buyin_string):
            return buyin_string.count('+') == 2

        def get_total_buyin(buyin_string):
            if buyin_string.count('+') == 2:
                # buyin_string is 'x+y+z'
                buyin = int(buyin_string.split('+')[0])
                bounty = int(buyin_string.split('+')[1])
                rake = int(buyin_string.split('+')[2])
                return buyin + bounty + rake
            elif buyin_string.count('+') == 1:
                # buyin_string is 'x+y' (non bounty)
                buyin = int(buyin_string.split('+')[0])
                rake = int(buyin_string.split('+')[1])
                return buyin + rake
            else:
                buyin = int(buyin_string)
                return buyin

        self.game_type = game_type
        self.buyin_string = buyin_string
        self.prize = None
        self.club_id = club.id
        self.total_buyin = get_total_buyin(buyin_string)
        self.is_bounty = is_bounty(buyin_string)


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    balance = Column(Float)
    owner_phone = Column(String(15))
    games = relationship("Game", backref="club")  # updated line

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

