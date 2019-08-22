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
    


   # terminal_view.print_menu(title,list_options,exit_message)
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == "1":
           table, title_list =  store.show_table()
           terminal_view.print_table(table, title_list)
        elif choice == "2":
            list_labels = ('Name: ', 'Studio: ', 'Elements: ', 'Sales: ')
            title = "Create record in store"
            inputs = terminal_view.get_inputs(list_labels, title)
            store.make_record_to_add(inputs)
        elif choice == "3":
            store.remove_record_from_file(terminal_view.get_string('ID: '))
        elif choice == "4":
            store.update_record_from_table(terminal_view.get_string('Put your ID: '))
        else:
            terminal_view.print_error_message("There is no such choice.")
