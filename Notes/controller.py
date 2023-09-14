import view
import model
import text

def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_notes(model.notes, text.empty_book)
            case 4:
                new = view.add_note()
                model.add_note(new)
                view.print_message(text.add_successful(new.get('heading')))
            case 5:
                search = text.search_type()
                if search == 1:
                    word = view.search_word()
                    result = model.search(word)
                    view.show_notes(result, text.empty_search(word))
                elif search == 2:
                    result = view.filter_date(text.filter_type(),model.notes)
                    view.show_notes(result, text.empty_book)
                else:
                    print('\033[31mОшибка ввода. Попробуйте еще раз.\033[0m')
            case 6:
                edit = view.search_word()
                result = model.search(edit)
                if result != {}:
                    view.show_notes(result, text.empty_search(edit))
                    view.edit_contact(model.notes)
                    model.save_file()
                    model.open_file()
                else:
                    error = text.empty_search(edit)
                    print(error)
            case 7:
                edit = view.search_word()
                result = model.search(edit)
                if result != {}:
                    view.show_notes(result, text.empty_search(edit))
                    view.delete_contact(model.notes)
                    model.save_file()
                    model.open_file()
                else:
                    error = text.empty_search(edit)
                    print(error)
            case 8:
                model.save_file()
                view.print_message(text.good_bye)
                break