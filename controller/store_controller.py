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
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")
