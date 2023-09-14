import datetime
import text

def menu() -> int:
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.imput_error)

def add_note():
    new = {}
    for key, value in text.new_note.items():
        new[key] = input(value)
    return new

def show_notes(notes_note, message):
    if notes_note:
        for index, note in notes_note.items():
            print('=' * 65)
            print(f'{index:>3}. \033[33m\033[3m\033[4mЗаголовок:\033[0m \033[1m{print_note(note.get("heading").upper())}\033[0m\n{" "*5}\033[33m\033[3m\033[4mДата создания/изменения:\033[0m {note.get("date")}\n{" "*5}\033[33m\033[3m\033[4mЗаметка:\033[0m {print_note(note.get("body"))}')
            print('=' * 65 + "\n")
    else:
        print_message(message)

def print_message(message: str):
    print("\n" + message + "\n")

def print_note(heading: str):
    format_heading = ''
    count = 0
    for char in heading:
        format_heading+=char
        count+=1
        if char == "." or char == " ":
            if count >= 40:
                format_heading+="\n" + " "*14
                count = 0
    return format_heading

def search_word() -> str:
    return input(text.search_word)

def edit_key():
    while True:
        change = input(text.change_massege)
        if change.isdigit() and 0 < int(change) < 3:
            return int(change)
        print(text.change_index_error)

def sure():
    while True:
        a_y_s = input(text.sure_massege).lower()
        if a_y_s.__contains__('д'):
            return 1
        elif a_y_s.__contains__('н'):
            return 0
        else:
            print(text.sure_error)
            continue

def edit_contact(note: dict):
    index = input(text.edit_index)
    find_key = edit_key()
    new_value = input(text.edit_new)
    if find_key == 1:
        note[index]['heading'] = new_value
        note[index]['date'] = (str(datetime.datetime.today().replace(microsecond=0)))
    elif find_key == 2:
        note[index]['body'] = new_value
        note[index]['date'] = (str(datetime.datetime.today().replace(microsecond=0)))
    print_message(text.edit_successfull)

def delete_contact(note: dict):
    index = input(text.delete_massege)
    confir = sure()
    if confir == 1:
        temp = note.pop(index)
        print_message(text.delete_successfull(temp['heading']))

def view_input(message: str) -> str:
    return input(message)

def filter_date(choice: int, notes: dict):
    result = {}
    match(choice):
        case 1:
            for index, note in notes.items():
                if note['date'].__contains__(str(datetime.date.today())):
                    result[index] = note
        case 2:
            for index, note in notes.items():
                if note['date'].__contains__(str(datetime.date.today().strftime('%Y-%m'))):
                    result[index] = note
        case 3:
            for index, note in notes.items():
                if note['date'].__contains__(str(datetime.date.today().strftime('%Y'))):
                    result[index] = note
    return result
