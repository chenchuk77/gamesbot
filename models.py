from sqlalchemy import DateTime, Column, Integer, String, Boolean, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

# disable logging of sqlalchemy
# engine = create_engine('mysql+mysqlconnector://user:password@localhost/db', echo=True)
engine = create_engine('mysql+mysqlconnector://user:password@localhost/db')

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)
    started = Column(DateTime, default=datetime.datetime.utcnow)
    game_type = Column(String(255))
    name = Column(String(255))
    buyin_string = Column(String(255))
    is_bounty = Column(Boolean, default=False)
    bounties = Column(Integer, default=None)
    prize = Column(Integer, default=None)
    bounty_prize = Column(Integer, default=0)
    club = Column(String(255))
    bullets = Column(Integer, default=None)
    bullet_price = Column(Integer, default=0)
    total_buyin = Column(Integer, default=0)
    net_profit = Column(Integer, default=0)


class Club(Base):
    __tablename__ = 'clubs'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    balance = Column(Float)
    owner_phone = Column(String(15))


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

