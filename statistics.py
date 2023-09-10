from models import Game, Club, Session
from datetime import *
import datetime
import matplotlib.pylab as plt


def get_games_last_n_days(n):
    # n=0 means today results   (games started after today 08:00 AM)
    # n=1 means today+testerday (games started after yesterday 08:00 AM)
    now = datetime.datetime.utcnow().date()
    last_0800_am = datetime.datetime.fromisoformat(now.isoformat() + ' 08:00')
    start_point = last_0800_am - timedelta(days=n)
    session = Session()
    db_games = session.query(Game)
    # find games after the start_point
    games_last_n_days = [x for x in db_games if x.started > start_point]
    session.close()
    return games_last_n_days

def get_games_count_last_n_days(n):
    return len(get_games_last_n_days(n))


def get_net_profit_last_n_days(n):
    games_last_n_days = get_games_last_n_days(n)
    return sum(game.net_profit for game in games_last_n_days)


def get_today_buyin():
    today_games = get_games_last_n_days(0)
    return sum(game.total_buyin for game in today_games)


def get_today_netprofit():
    today_games = get_games_last_n_days(0)
    return sum(game.net_profit for game in today_games)


def get_7days_netprofit():
    today_games = get_games_last_n_days(7)
    return sum(game.net_profit for game in today_games)


def get_30days_netprofit():
    today_games = get_games_last_n_days(30)
    return sum(game.net_profit for game in today_games)


def get_extended_statistics():
    daily_profits = {}
    total_profits = {}
    total = 0

    session = Session()
    db_games = session.query(Game)
    all_games = [x.__dict__ for x in db_games]

    # count daily profit into a dictionary
    for game in all_games:
        date = str(datetime.datetime.date(game['started']))
        if date in daily_profits:
            daily_profits[date] += int(game['net_profit'])
        else:
            daily_profits[date] = int(game['net_profit'])

    # find first day
    first_day = str(datetime.date.today()) # will be overriden
    for date_str in daily_profits.keys():
        if date_from_str(date_str) < date_from_str(first_day):
            first_day = date_str

    # create total profit
    day = first_day
    while day != today():
        if day in daily_profits:
            total = total + daily_profits[day]
        total_profits[day] = total
        day = tomorrow(day)

    lists = sorted(total_profits.items())
    x, y = zip(*lists)
    plt.plot(x,y)
    plt.savefig('total_profits.png')
    session.close()


def date_from_str(s):
    d = datetime.datetime.fromisoformat(s).date()
    return d


def today():
    return str(datetime.date.today())


def tomorrow(s):
    today=date_from_str(s)
    tomorrow=today + timedelta(days=1)
    return str(tomorrow)
