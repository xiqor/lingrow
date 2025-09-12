from app_logic import database

class User:
    def __init__(self, tg_id, registred, id=None):
        self.id = id
        self.tg_id = tg_id
        self.registred = registred

    @classmethod
    def get_user_id_by_tg_id(self, tg_id):
        return database.get_user_by_tg_id(tg_id)
