# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common


def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """


    title = "Store menu"
    list_options = ("Show", "Add", "Remove", "Update")
    exit_message = "Back do main menu"
    file_name = 'model/store/games.csv'
    title_labels = ('ID', 'Name', 'Studio', 'Elements', 'Sales')
    list_labels = ('Name:', 'Studio:', 'Elements:', 'Sales:')

    

    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == "1":
            common.show_table(file_name, title_labels)
        elif choice == "2":
            title = "Create record in store"
            common.store_add(file_name, list_labels, title)
        elif choice == "3":
<<<<<<< HEAD
            common.remove_record_from_file(terminal_view.get_string, store.remove, file_name)
=======
            store.remove_record_from_file(terminal_view.get_string('ID: '))
>>>>>>> f5735d700ba0c7cf4d75835d3d2139be4b27d9f3
        elif choice == "4":
            common.store_update(file_name, list_labels, 'Update')
        else:
            terminal_view.print_error_message("There is no such choice.")
