from app_logic import dictionary, database
from interface.tgbot import bot

database.create_tables
dp = bot.dp

if __name__ == '__main__':
    dp.run_polling(bot)
