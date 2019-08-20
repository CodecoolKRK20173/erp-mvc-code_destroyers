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

    # your code
    file_name = "game_test.csv"

    title = "Store menu"
    list_options = ("Add", "Remove", "Update")
    exit_message = "Back do main menu"

    test_list = ("1", "2", "3", "4", "5")
    test_string = "test"


   # terminal_view.print_menu(title,list_options,exit_message)
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(title,list_options,exit_message)
        if choice == "1":
            store.add(test_list, test_list)
        elif choice == "2":
            store.remove()
        elif choice == "3":
            store.update()
        else:
            terminal_view.print_error_message("There is no such choice.")
