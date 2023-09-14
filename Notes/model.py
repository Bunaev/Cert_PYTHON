import datetime
import json

notes = {}
path = 'Notes\\notes.json'

def open_file():
    global notes
    try:
        with open(path, 'r', encoding='UTF=8') as file:
            notes = json.load(file)
        return True
    except:
        return False
    
def search(word: str):
    result = {}
    for index, note in notes.items():
        if word.lower() in ' '.join(note.values()).lower():
            result[index] = note
    return result
    


def save_file():
    try:
        with open(path, 'w', encoding='UTF=8') as file:
            json.dump(notes, file, ensure_ascii=False)
        return True
    except:
        return False

def add_note(new):
    new['date'] = (str(datetime.datetime.today().replace(microsecond=0)))
    note = {check_id(): new}
    notes.update(note)
    save_file()
    open_file()

def check_id():
    if notes:
        return max(list(map(int, notes))) + 1
    return 1
