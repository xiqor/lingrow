from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from app_logic import dictionary, user

# перенести в мейн
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def process_start_command(message: Message):
    await message.answer('Привет!')

@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    pass # Make cool help output

@dp.message(Command(comannds='add'))
async def process_add_command(message: Message):
    pass # через try except и split message

@dp.message(Command(comannds='remove'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(comannds='update'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(comannds='get'))
async def process_add_command(message: Message):
    pass

@dp.message(Command(comannds='getall'))
async def process_add_command(message: Message):
    pass

dp.run_polling(bot)