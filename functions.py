from models import Game, Club, Session


def get_running_games():
    session = Session()
    db_games = session.query(Game)
    running_games = [x for x in db_games if x.prize is None]
    return running_games


def set_game_prize(game, prize):
    session = Session()
    db_game = session.query(Game).filter(Game.id == game.id).first()
    db_game.prize = prize
    db_game.net_profit += prize
    session.commit()


def add_game_bullet(game):
    session = Session()
    db_game = session.query(Game).filter(Game.id == game.id).first()
    db_game.bullets += 1
    db_game.total_buyin -= db_game.bullet_price
    db_game.net_profit -= db_game.bullet_price
    session.commit()


def win_bounty(game):
    session = Session()
    db_game = session.query(Game).filter(Game.id == game.id).first()
    db_game.bounties += 1
    db_game.net_profit += get_bounty_value(db_game.buyin_string)
    session.commit()


def is_game_running(game):
    session = Session()
    db_game = session.query(Game).filter(Game.id == game.id).first()
    return db_game.prize is not None


def is_bounty(buyin_string):
    return buyin_string.count('+') == 2


def get_total_buyin(buyin_string):
    buyin_string = buyin_string.replace("(", "").replace(")", "")
    if buyin_string.count('+') == 2:
        # buyin_string is '(x+y+z)'
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


def get_bounty_value(buyin_string):
    return int(buyin_string.split('+')[1])


def start_new_game(game_type, name, buyin_string, club_name):
    session = Session()
    bounty_count = 0 if is_bounty(buyin_string) else None
    new_game = Game(game_type=game_type,
                    name=name,
                    buyin_string=buyin_string,
                    club=club_name,
                    is_bounty=is_bounty(buyin_string),
                    bounties=0 if is_bounty(buyin_string) else None,
                    bullets=1,
                    prize=None,
                    bounty_prize=0,
                    bullet_price=get_total_buyin(buyin_string),
                    total_buyin=get_total_buyin(buyin_string),
                    net_profit=(-1) * get_total_buyin(buyin_string))

    session.add(new_game)
    session.commit()


def list_club_names():
    session = Session()
    all_clubs = session.query(Club)
    club_names = [x.name for x in all_clubs]
    return sorted(club_names)


def list_game_types():
    session = Session()
    all_games = session.query(Game)
    game_types = [x.game_type for x in all_games]
    return sorted(list(set(game_types)))


def list_game_names():
    session = Session()
    all_games = session.query(Game)
    game_names = [x.name for x in all_games]
    return sorted(list(set(game_names)))


def list_buyin_strings():
    session = Session()
    all_games = session.query(Game)
    buyin_strings = [x.buyin_string for x in all_games]
    # set to remove dups
    return sorted(list(set(buyin_strings)))


def create_clubs():
    session = Session()

    all_db_club = session.query(Club)
    club_names = list_club_names()
    print(str(club_names))
    if 'Spades' not in club_names:
        print('creating club Spades')
        spades = Club(name="Spades", balance=0, owner_phone="000999888")
        session.add(spades)
    if 'Matrix' not in club_names:
        print('creating club Matrix')
        matrix = Club(name="Matrix", balance=0, owner_phone="000999888")
        session.add(matrix)
    if 'FullHouse' not in club_names:
        print('creating club FullHouse')
        fullhouse = Club(name="FullHouse", balance=0, owner_phone="000999888")
        session.add(fullhouse)
    if 'PPC' not in club_names:
        print('creating club PPC')
        fullhouse = Club(name="PPC", balance=0, owner_phone="000999888")
        session.add(fullhouse)
    session.commit()


def create_games():
    start_new_game("PLO",    "LUNCH",      "(60+60+12)",   "Matrix")
    # start_new_game("NL",     "MOON MAIN",  "(100+100+20)", "Matrix")
    # start_new_game("PLO6",   "NOON HYPER", "(50+50+10)",   "Matrix")
    # start_new_game("NL-SAT", "1/5 - 333",  "(73+0)",       "Spades")


