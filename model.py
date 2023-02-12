import csv
import views


PATH_FILE = 'Заметки.csv'

def create_note(note_data):
    with open(PATH_FILE, 'a', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        file_writer.writerow(note_data)
     

def show_notes():
    lst = []
    with open(PATH_FILE, 'r', encoding='UTF8') as file:
        file_reader = csv.reader(file, delimiter=';', lineterminator='\r')
        for item in file_reader:
            lst.append(item)       
    return lst

def delete_note(user_select):
    lst = show_notes()
    del lst[user_select-1]
    with open(PATH_FILE, 'w', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        for item in lst:
            file_writer.writerow(item)

def apdate_note(user_select, lst):
    lst[user_select] = views.note_data_entry()
    with open(PATH_FILE, 'w', encoding='UTF8') as file:
        file_writer = csv.writer(file, delimiter=';', lineterminator='\r')
        for item in lst:
            file_writer.writerow(item)
