import view
import model
import text

def start():
    my_pb = model.PhoneBook()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                my_pb.open()
                view.print_message(text.load_successful)
            case 2:
                my_pb.save()
                view.print_message(text.save_successful)
            case 3:
                pb = my_pb.load()
                view.print_contact(pb, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = my_pb.add(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                name = view.input_name(text.find_name_contact)
                model.find_contact(name)
            case 6:
                pass
            case 7:
                pb=model.get_pb()
                index = view.input_index(text.index_del_contact,pb,text.load_error)
                name =  model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break

