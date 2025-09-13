from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from app_logic import dictionary, user
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# перенести в мейн
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    tg_id = message.from_user.id
    if not user.User.get_user_id_by_tg_id(tg_id):
        new_user = user.User(tg_id=tg_id)
        new_user.add_user()
    await message.answer(f'Привет, {user.User.get_user_id_by_tg_id(tg_id)}, {tg_id}!')
    # add registation

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    pass # Make cool help output

@dp.message(Command(commands='add'))
async def process_add_command(message: Message):
    try:
        args = message.text.split(maxsplit=4)
        if len(args) < 5:
            await message.answer(f'Incorrect format!')
            return
        user_id = user.User.get_user_id_by_tg_id(message.from_user.id)
        item = dictionary.Item(item_type=args[1], spelling=args[2], transcription=args[3], meaning=args[4], user_id=user_id)
        item.add()
        await message.answer('grats!')
    except Exception as e:
        await message.answer(f'Error: {e}')


@dp.message(Command(commands='remove'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(commands='update'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(commands='get'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(commands='getall'))
async def process_add_command(message: Message):
    pass
