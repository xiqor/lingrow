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
    def remove(self, item_id, user_id):
        database.remove_item(item_id,user_id)

    @classmethod
    def update(self, item, param, value, user_id):
        database.update_item(item, param, value, user_id)

    @classmethod
    def get(cls, param, user_id):
        # make it pretty
        return str(database.get_item(param, user_id))

    # pretty print of item
    def pprint(self):
        pass