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

    # file_name = "games.csv"

    title = "Store menu"
    list_options = ("Show", "Add", "Remove", "Update")
    exit_message = "Back do main menu"
    file_name = 'model/store/games.csv'
    


   # terminal_view.print_menu(title,list_options,exit_message)
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == "1":
            common.show_table(file_name)
        elif choice == "2":
            list_labels = ('Name', 'Studio', 'Elements', 'Sales')
            title = "Create record in store"
            common.store_add(file_name, list_labels, title)
        elif choice == "3":
            store.remove_record_from_file(terminal_view.get_string("Remove record by ID", "ID: "))
        elif choice == "4":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
