from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from app_logic import dictionary, user
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    tg_id = message.from_user.id
    if not user.User.get_user_id_by_tg_id(tg_id):
        new_user = user.User(tg_id=tg_id)
        new_user.add_user()
    await message.answer(f'Hello, {user.User.get_user_id_by_tg_id(tg_id)}, {tg_id}!')

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer('''
You can use following commands:
IMPORTANT: always use 'word' as type, pls
/add <type> <spelling> <transcription> <meaning> - to add new word to your dictionary
/remove <id> (to get id use /get or /getall) - to remove word from your dictionary
/update <item_to_change> <param_to_change> <new_value> - to update word's info
/get <spelling OR meaning> - to get specific word
/getall - to get your whole dictionary''')

@dp.message(Command(commands='add'))
async def process_add_command(message: Message):
    try:
        args = message.text.split(maxsplit=4)
        if len(args) < 5:
            await message.answer(f'Incorrect format! Try using \n"/add <type> <spelling> <transcription> <meaning>"')
            return
        user_id = user.User.get_user_id_by_tg_id(message.from_user.id)
        item = dictionary.Item(item_type=args[1], spelling=args[2], transcription=args[3], meaning=args[4], user_id=user_id)
        item.add()
        await message.answer('Congrats! New word added to your dictionary')
    except Exception as e:
        await message.answer(f'Error: {e}')

# make it not from id but by spelling
@dp.message(Command(commands='remove'))
async def process_remove_command(message: Message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            await message.answer(f'Incorrect format! Try using \n"/remove <id>" to get id use "/get" or "/getall"')
            return
        item_id = args[1]
        user_id = user.User.get_user_id_by_tg_id(message.from_user.id)
        dictionary.Item.remove(item_id, user_id)
        await message.answer(f'Success! Word {item_id} removed from your dictionary')
    except Exception as e:
        await message.answer(f'Error: {e}')

@dp.message(Command(commands='update'))
async def process_update_command(message: Message):
    try:
        args = message.text.split(maxsplit=3)
        if len(args) < 4:
            await message.answer(f'Incorrect format! Try using \n"/update <item_to_change> <param_to_change> <new_value>"')
            return
        user_id = user.User.get_user_id_by_tg_id(message.from_user.id)
        item, param, value = args[1:]
        dictionary.Item.update(item, param, value, user_id)
        await message.answer(f'Yes! Word {item} updated')
    except Exception as e:
        await message.answer(f'Error: {e}')

@dp.message(Command(commands='get'))
async def process_get_command(message: Message):
    try:
        args = message.text.split(maxsplit=1)
        if len(args) != 2:
            await message.answer(f'Incorrect format! Try using "/get <spelling OR meaning>"')
            return
        param = args[1]
        user_id = user.User.get_user_id_by_tg_id(message.from_user.id)
        await message.answer(dictionary.Item.get(param, user_id))
    except Exception as e:
        await message.answer(f'Error: {e}')

@dp.message(Command(commands='getall'))
async def process_getall_command(message: Message):
    pass
