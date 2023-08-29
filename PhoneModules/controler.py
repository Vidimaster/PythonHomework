from model import PhoneBook
import text
import view

def search_contact(pb):
    word = view.input_requset(text.input_search_word)
    result = pb.find_contact(word)
    
    view.show_book(result, text.not_find(word))
    if result:
        return True

def start():

    pb = PhoneBook()

    while True:
        choice = view.main_menu()
        if choice == 1:
            pb.open_file()
            view.print_message(text.load_successful)
        elif choice == 2:
            pb.save_file()
            view.print_message(text.save_successful)
        elif choice == 3:
            view.show_book(pb.phone_book, text.empty_book_error)
        elif choice == 4:
            new_contact = view.input_contact(text.input_contact)
            pb.add_contact(new_contact)
            view.print_message(text.contact_action(new_contact[0], text.operation[0]))
        elif choice == 5:
            search_contact(pb)

        elif choice == 6:
            if search_contact(pb):
                c_id = int(view.input_requset(text.input_contact_id))
                new_contact = view.input_contact (text.input_edit_contact)
                name = pb.edit_contact(c_id, new_contact)
                view.print_message (text.contact_action(name, text.operation[1]))
        elif choice == 7:
            if search_contact(pb):
                c_id = int(view.input_requset(text.input_del_contact_id))
                name = pb.delete_contact(c_id)
                view.print_message(text.contact_action(name, text.operation[2]))
        elif choice == 8:
            if search_contact(pb):
                c_id = int(view.input_requset(text.input_contact_id))
                name = pb.make_contact_favorite(c_id)
                view.print_message(text.contact_action(name, text.operation[1]))
        elif choice == 9:
            view.show_favorites(pb.phone_book, text.empty_book_error)        
        elif choice == 10:
            if pb.original_book != pb.phone_book:
                if view.input_requset(text.confirm_changes).lower() == 'y':
                    pb.save_file()
                    view.print_message(text.save_successful)

            view.print_message(text.exit_program)
            break


