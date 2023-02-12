import datetime


def menu():
    menu = ['Показать все заметки', 'Добавить заметку',
            'Удалить заметку', 'Редактировать заметку', 'Выход.']
    for item in enumerate(menu, 1):
        print(*item)
    print('')    
    num = int(input('Выберите пункт меню: '))
    print('')
    return num


def note_data_entry():
    header = input('Введите заголовок: ')
    text = input('Введите текст заметки: ')
    date = datetime.datetime.now()
    data_new_note = [header, text, date]
    return data_new_note


def views_show_notes(users):
    for item in enumerate(users, 1):
        print(*item)
    

def user_num_for_delete():
    print('')
    return int(input('Введите номер записи для удаления: '))


def user_num_for_update():
    print('')
    return int(input('Введите номер записи для редактирования: '))-1

def exit():
    print('')
    print('Пока!!!')
    quit()