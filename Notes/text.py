main_menu = ["\033[36mГлавное меню:",
             "Открыть файл",
             "Сохранить файл",
             "Показать все заметки",
             "Добавить заметку",
             "Найти заметку",
             "Изменить заметку",
             "Удалить заметку",
             "Выход\033[0m"]
select_menu = '\033[36mВыберете пункт меню: \033[0m'
imput_error = f'\033[31mОшибка ввода! Введите число от 1 до {len(main_menu)-1}.\033[0m'
new_note = {'heading':'\033[36mВведите заголовок заметки: \033[0m', 'body':'\033[36mВведите содержание заметки: \033[0m'}
empty_book = '\033[31mЗаметки пусты или не открыты.\033[0m'
def add_successful(heading: str) -> str:
    return f'\033[32mЗаметка "{heading}" успешно добавлена.\033[0m'
load_successful = '\033[32mЗаметки успешно загружены.\033[0m'
save_successful = '\033[32mЗаметки успешно сохранены.\033[0m'
error_load = '\033[31mОшибка загрузки заметок.\033[0m'
error_save = '\033[31mОшибка сохранения заметок.\033[0m'
search_word = '\033[36mВведите слово для поиска: \033[0m'
def empty_search(word: str) -> str:
    return f'\033[31mЗаметки, содержащие слово "{word}", не найдены.\033[0m'
edit_index = '\033[36mВведите порядковый номер заметки, которую хотите изменить: \033[0m'
change_index_error = '\033[31mОшибка! Введите 1 (заголовок заметки) или 2 (содержание заметки): '
change_massege = '''\033[36mЧто именно Вы хотите изменить? 
        Введите "1" для измения заголовка;
        Введите "2" для изменения содержания: \033[0m'''
edit_new = '\033[36mВведите новое значение: \033[0m'
edit_successfull = '\033[32mЗаметка успешно изменена!\033[0m'
delete_massege = '\033[36mВведите порядковы номер заметки, которую хотите удалить: \033[0m'
sure_massege = '\033[36mВы уверены? Да/Нет: \033[0m'
sure_error = '\033[31mОшибка ввода!\033[0m \033[36mВведите "Да" или "Нет": \033[0m'
def delete_successfull(note: dict):
    return f'\033[32mЗаметка "{note}" успешно удалена!\033[0m'

def search_type():
    type = input('''\033[36m
        Как именно Вы хотите искать заметки?\n
        Введите "1" для поиска по ключевому слову;
        Введите "2" для фильтрации заметок по дате;
        
        Ваш выбор: \033[0m''')
    if type.isdigit and 2 >= int(type) >= 1:
        return int(type)
    else:
        return False
def filter_type():
    type = input('''\033[36m
        1. За сегодня;
        2. За текущий месяц;
        3. За текущий год;
        
        Ваш выбор: \033[0m''')
    if type.isdigit and 3 >= int(type) >= 1:
        return int(type)
    else:
        return False
    
good_bye = '\033[32mВсего доброго! До новых встреч!\033[0m'