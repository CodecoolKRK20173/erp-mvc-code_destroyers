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
    list_options = ("(1) Add", "(2) Remove", "(3) Update")
    exit_message = "(0) Back do main menu"


    terminal_view.print_menu(title,list_options,exit_message)