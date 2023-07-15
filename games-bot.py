from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, chat_invite_link  # for reply keyboard (sends message)
import credentials
import logging
import sys
import random

from functions import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

bot = Bot(token=credentials.token)

dp = Dispatcher(bot)

# used to check the function to handle arbitrary text (default text)
last_function = ''

the_game = None

# dict of values for using to create a new game
new_game = {'name': '', 'game_type': '', 'buyin_string': '', 'club': ''}


def get_new_game_status():
    # if new_game['name'] == '':
    # status = "new game values:\n" + \
    # "🟥" if new_game['club'] == '' else "🟩" + "club: {}\n".format(new_game['club']) + \
    # "🟥" if new_game['game_type'] == '' else "🟩" + "type: {}\n".format(new_game['game_type']) + \
    # "🟥" if new_game['name'] == '' else "🟩" + "name: {}\n".format(new_game['name']) + \
    # "🟥" if new_game['buyin_string'] == '' else "🟩" + "buyin: {}\n".format(new_game['buyin_string'])
    #
    #
    status = "new game values:\nclub: {}\ntype: {}\nname: {}\nbuyin: {}\n".format(
        new_game['club'], new_game['game_type'], new_game['name'], new_game['buyin_string'],)
    logger.info(status)
    return status

    # # prepare update keyboard
    # update_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    # end_game_button = KeyboardButton('End Game ✅')
    # set_prize_button = KeyboardButton('Set Prize 💲')
    # bullet_button = KeyboardButton('Add Bullet 💰')
    # if the_game.is_bounty:
    #     bounty_button = 'Add KO #{} 🏆'.format(the_game.bounties + 1)
    #     update_kb.add(end_game_button, set_prize_button, bullet_button, bounty_button)
    # else:
    #     update_kb.add(end_game_button, set_prize_button, bullet_button)
    # update_kb.add('Back ↩')
    # game_description = "🔸Club: {}\n🔸Game type: {}\n🔸Tournament name: {}\n🔸Buyin: {}\n🔹Net profit: {}". \
    #     format(the_game.club, the_game.game_type, the_game.name,
    #            the_game.buyin_string, str(the_game.net_profit))


# def get_update_keyboard():
#     # prepare update keyboard
#     update_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     end_game_button = KeyboardButton('End Game ✅')
#     set_prize_button = KeyboardButton('Set Prize 💲')
#     bullet_button = KeyboardButton('Add Bullet 💰')
#     if the_game.is_bounty:
#         bounty_button = 'Add KO #{} 🏆'.format(the_game.bounties + 1)
#         update_kb.add(end_game_button, set_prize_button, bullet_button, bounty_button)
#     else:
#         update_kb.add(end_game_button, set_prize_button, bullet_button)
#     update_kb.add('Back ↩')
#     return update_kb



def get_games_keyboard():
    running_games = get_running_games()
    # gameKB = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, )
    games_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    # gameKB.add(new_game_button)
    for game in running_games:
        existing_game_button = KeyboardButton(
            '{}:{}:{}:{}'.format(game.club, game.game_type, game.name, game.buyin_string))
        games_kb.add(existing_game_button)
    new_game_button = KeyboardButton('Start a new Game 🎲')
    statistics_button = KeyboardButton('Statistics 📈')
    summary_button = KeyboardButton('Summary ➕')
    games_kb.add(new_game_button)
    games_kb.add(statistics_button)
    games_kb.add(summary_button)
    return games_kb


# # USE FOR DEVELOPING ONLY !!!
# @dp.message_handler(commands=['db_init'])
# async def db_init(message: types.Message):
#     logger.info("db_init() called ...")
#     create_clubs()
#     create_games()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    global last_function
    # global the_game
    logger.info("start() called ...")
    last_function = 'start'
    games_kb = get_games_keyboard()
    await message.answer('Im games-bot 🤓\npress the menu button to setup a new game\n or update existing ...',
                         reply_markup=games_kb)


# handles request to update a game record, ie: "Spades:PLO:Warmup:(60+60+12)"
@dp.message_handler(regexp=r"^.*\:.*\:.*\:.*$")
async def update_game(message: types.Message):
    global last_function
    global the_game
    logger.info("update_game() called ...")
    game_string = message.text
    logger.info("game {} will be edited".format(game_string))
    game_club = game_string.split(':')[0]
    game_type = game_string.split(':')[1]
    game_name = game_string.split(':')[2]
    game_buyin_string = game_string.split(':')[3]

    # get the game from db into the main context
    rg = get_running_games()
    the_game = [x for x in rg if x.name == game_name and
                x.club == game_club and
                x.game_type == game_type and
                x.buyin_string == game_buyin_string][0]

    # prepare update keyboard
    update_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    end_game_button = KeyboardButton('End Game ✅')
    set_prize_button = KeyboardButton('Set Prize 💲')
    bullet_button = KeyboardButton('Add Bullet 💰')
    if the_game.is_bounty:
        bounty_button = 'Add KO #{} 🏆'.format(the_game.bounties + 1)
        update_kb.add(end_game_button, set_prize_button, bullet_button, bounty_button)
    else:
        update_kb.add(end_game_button, set_prize_button, bullet_button)
    update_kb.add('Back ↩')
    game_description = "🔸Club: {}\n🔸Game type: {}\n🔸Tournament name: {}\n🔸Buyin: {}\n🔹Net profit: {}". \
        format(the_game.club, the_game.game_type, the_game.name,
               the_game.buyin_string, str(the_game.net_profit))
    await message.answer(game_description, reply_markup=update_kb)


@dp.message_handler(regexp='End Game ✅')
async def end_game(message: types.Message):
    global the_game
    logger.info("end_game() called ...")
    set_game_prize(the_game, 0)
    games_kb = get_games_keyboard()
    await message.answer('Game ends with no prize 🙁\nDone.', reply_markup=games_kb)
    # win no money


@dp.message_handler(regexp='Set Prize 💲')
async def set_prize(message: types.Message):
    global the_game
    global last_function
    last_function = 'set_prize'
    logger.info("set_prize() called ...")
    await message.answer('What is the prize ?')
    set_game_prize(the_game, int(message.text))


@dp.message_handler(regexp='Add Bullet 💰')
async def add_bullet(message: types.Message):
    global the_game
    logger.info("add_bullet() called ...")
    add_game_bullet(the_game)
    games_kb = get_games_keyboard()
    await message.answer('1 Bullet added, GOOD LUCK ❗ 🤞\nDone.', reply_markup=games_kb)


@dp.message_handler(regexp='Back ↩')
async def back(message: types.Message):
    global the_game
    logger.info("back() called ...")
    the_game = None
    games_kb = get_games_keyboard()
    await message.answer('Choose a game to update, Or start a new one by using the menu 🙄', reply_markup=games_kb)


@dp.message_handler(regexp=r"^Add KO.*$")
async def add_bounty(message: types.Message):
    global the_game
    logger.info("add_bounty() called ...")
    win_bounty(the_game)
    games_kb = get_games_keyboard()
    await message.answer('Done.', reply_markup=games_kb)


@dp.message_handler(regexp='Start a new Game 🎲')
async def add_new_game(message: types.Message):
    global the_game
    global new_game
    global last_function
    logger.info("add_new_game() called ...")
    logger.info("preparing a new game record (club)")
    clubs = list_club_names()
    clubs_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    for club in clubs:
        clubs_kb.add(KeyboardButton(club))
    back_button = KeyboardButton('Back ↩')
    clubs_kb.add(back_button)
    await message.answer(get_new_game_status() + 'Choose club', reply_markup=clubs_kb)
    last_function = 'add_new_game'


# setting a gametype
@dp.message_handler(regexp=r"NL|PLO|PLO5|PLO6")
async def set_game_type(message: types.Message):
    global the_game
    global new_game
    global last_function
    logger.info("set_game_type() called ...")
    new_game['game_type'] = message.text
    logger.info("preparing a new game record (buyin_string)")
    buyin_strings = list_buyin_strings()
    buyin_strings_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    for buyin_string in buyin_strings:
        buyin_strings_kb.add(KeyboardButton(buyin_string))
    back_button = KeyboardButton('Back ↩')
    buyin_strings_kb.add(back_button)
    await message.answer(get_new_game_status() + 'Choose buyin structure', reply_markup=buyin_strings_kb)
    # new_game['buyin_string'] = message.text
    last_function = 'set_buyin'


# @dp.message_handler(regexp=r"^:")
# async def set_game_name(message: types.Message):
#     global the_game
#     global new_game
#     global last_function
#     logger.info("set_game_name() called ...")
#     logger.info("preparing a new game record (name)")
#     game_names = list_game_names()
#     game_names_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
#     for game_name in game_names:
#         game_names_kb.add(KeyboardButton(game_name))
#     back_button = KeyboardButton('Back ↩')
#     game_names_kb.add(back_button)
#     await message.answer('Choose buyin structure', reply_markup=game_names_kb)
#     new_game['name'] = message.text
#     last_function = 'set_game_name'


# setting a buyin string in the form of "( .* )"
@dp.message_handler(regexp=r"^\(.*\)$")
async def set_buyin(message: types.Message):
    global the_game
    global new_game
    global last_function
    logger.info("set_buyin() called ...")
    new_game['buyin_string'] = message.text
    # logger.info("preparing a new game record (buyin)")
    # buyin_strings = list_buyin_strings()
    # buyin_strings_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    # for buyin_string in buyin_strings:
    #     buyin_strings_kb.add(KeyboardButton(buyin_string))
    # back_button = KeyboardButton('Back ↩')
    # buyin_strings_kb.add(back_button)
    logger.info("preparing a new game record (name)")
    game_names = list_game_names()
    game_names_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
    for game_name in game_names:
        game_names_kb.add(KeyboardButton(game_name))
    back_button = KeyboardButton('Back ↩')
    game_names_kb.add(back_button)
    # await message.answer('Choose buyin structure', reply_markup=game_names_kb)
    # new_game['name'] = message.text
    # last_function = 'default'

    await message.answer(get_new_game_status() + 'Set game name', reply_markup=game_names_kb)
    last_function = 'set_buyin'






# generic default handler for all ( must be declared LAST ! )
@dp.message_handler()
async def default(message: types.Message):
    global last_function
    global the_game
    global new_game
    if last_function == '':
        logger.warning("default() called but not by us ... ignoring ...")
        return
    logger.info("default() called")

    await message.answer(message.text)
    if last_function == 'set_prize':
        logger.info("setting prize to close game record")
        set_game_prize(the_game, int(message.text))
        last_function = 'default'
        return
    if last_function == 'add_new_game':
        new_game['club'] = message.text
        logger.info("preparing a new game record (game_type)")
        game_types = list_game_types()
        game_types_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
        for game_type in game_types:
            game_types_kb.add(KeyboardButton(game_type))
        back_button = KeyboardButton('Back ↩')
        game_types_kb.add(back_button)
        await message.answer(get_new_game_status() + 'Choose game type', reply_markup=game_types_kb)
        new_game['game_type'] = message.text
        last_function = 'default'
        return
    if last_function == 'set_buyin':
        new_game['name'] = message.text
        logger.info("preparing a new game record (name)")
        if new_game['club'] != '' and new_game['name'] != '' and new_game['buyin_string'] != '' and new_game['game_type'] != '':
            start_new_game(new_game['game_type'], new_game['name'], new_game['buyin_string'], new_game['club'])
            game_description = get_new_game_status()
            # init
            new_game = {'name': '', 'game_type': '', 'buyin_string': '', 'club': ''}

            games_kb = get_games_keyboard()
            # # prepare update keyboard
            # update_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            # end_game_button = KeyboardButton('End Game ✅')
            # set_prize_button = KeyboardButton('Set Prize 💲')
            # bullet_button = KeyboardButton('Add Bullet 💰')
            # if the_game.is_bounty:
            #     bounty_button = 'Add KO #{} 🏆'.format(the_game.bounties + 1)
            #     update_kb.add(end_game_button, set_prize_button, bullet_button, bounty_button)
            # else:
            #     update_kb.add(end_game_button, set_prize_button, bullet_button)
            # update_kb.add('Back ↩')
            #
            await message.answer('game added successfuly.\n\nU can now update it from the menu' + game_description, reply_markup=games_kb)
            last_function = 'default'


        return

        # game_names = list_game_names()
        # game_names_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
        # for game_name in game_names:
        #     game_names_kb.add(KeyboardButton(game_name))
        # back_button = KeyboardButton('Back ↩')
        # game_names_kb.add(back_button)
        # await message.answer('Choose buyin structure', reply_markup=game_names_kb)
        # new_game['name'] = message.text
        # last_function = 'default'
        # return

        # buyin_strings = list_buyin_strings()
        # buyin_strings_kb = ReplyKeyboardMarkup(one_time_keyboard=True)
        # for buyin_string in buyin_strings:
        #     buyin_strings_kb.add(KeyboardButton(buyin_string))
        # back_button = KeyboardButton('Back ↩')
        # game_types_kb.add(back_button)
        # await message.answer('Choose buyin structure', reply_markup=game_types_kb)
        # new_game['buyin_string'] = message.text


        # await message.answer('Choose Buyin', reply_markup=game_types_kb)
        # new_game['game_type'] = message.text

    last_function = 'default'



# this is the last line
executor.start_polling(dp)
