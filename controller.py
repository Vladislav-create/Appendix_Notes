import views
import model



def select_user_menu():
    res = views.menu()
    if res == 1:
        views.views_show_notes(model.show_notes())
        select_user_menu()
    elif res == 2:
        model.create_note(views.note_data_entry())
        select_user_menu()
    elif res == 3:
        views.views_show_notes(model.show_notes())
        model.delete_note(views.user_num_for_delete())
        views.views_show_notes(model.show_notes())
        select_user_menu()
    elif res == 5:
        views.exit()    
    else:
        views.views_show_notes(model.show_notes())
        model.apdate_note(views.user_num_for_update(), model.show_notes())
        views.views_show_notes(model.show_notes())
        select_user_menu()