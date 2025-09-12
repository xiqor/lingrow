from app_logic import database
class Item:
    # initialization
    def __init__(self, item_type, spelling, transcription, meaning, user_id, item_id=None, added_at=None):
        self.id = item_id
        self.type = item_type
        self.spelling = spelling
        self.transcription = transcription
        self.meaning = meaning
        self.added_at = added_at
        self.user_id = user_id

    # save new item to db WORKS
    def add(self):
        database.add_item(self)

    # remove item from db WORKS
    @classmethod
    def remove(self, item_id):
        database.remove_item(item_id)

    def update(self, item_id):
        database.update_item(item_id, self)

    @classmethod
    def get(cls, param):
        return database.get_item(param)

    # pretty print of item
    def pprint(self):
        pass