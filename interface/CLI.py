import cmd
from app_logic import dictionary

class Cli(cmd.Cmd):
    intro = '''
    Welcome to Vocaboo: simple CLI vocabulary (for now:D)
    Type 'help' or '?' for help
    '''
    prompt = 'vocaboo >> '

    def do_add(self, arg):
        '''Add new word to your dictionary:
        add <type> <spelling> <transcription> <meaning>'''
        args = arg.split()
        item = dictionary.Item(item_type=args[0], spelling=args[1], transcription=args[2], meaning=args[3])
        item.add()

    def do_remove(self, item_id):
        '''Remove existing word from your dictionary by id (use 'get' to get id):
        remove <id>'''
        dictionary.Item.remove(item_id)
# update update func)
    def do_update(self, arg): # add default from existing item and maybe change logic for more user-friendly use
        '''Update info about any existing word by id
        update <id> <new_type> <new_spelling> <new_transcription> <new_meaning>'''
        args = arg.split()
        item = dictionary.Item(item_type=args[1], spelling=args[2], transcription=args[3], meaning=args[4])
        item.update(args[0])

    # find a way to make it pretty
    def do_get(self, arg):
        '''Get info about existing word in dictionary:
        get <spelling/meaning>'''
        print(dictionary.Item.get(arg))

    # find a way to make it pretty
    def do_getall(self, arg):
        '''Get info about all words in dictionary:
        getall'''
        for item in dictionary.Item.get(None):
            print(item)

    def do_exit(self, arg):
        return True

    #Todo add comand for review mode: set number of questions and randomize it
