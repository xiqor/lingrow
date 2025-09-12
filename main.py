from app_logic import dictionary, database
from interface.tgbot.bot import bot, dp

database.create_tables()

if __name__ == '__main__':
    dp.run_polling(bot)
