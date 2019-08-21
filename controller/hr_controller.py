# everything you'll need is imported:
from view import terminal_view
from model.hr import hr
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    title = "Hr Menu"
    list_options = ('List', "Add", "Remove", "Update")
    exit_message = "Back do main menu"

    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == '1':
            table, title_list =  hr.show_table()
            terminal_view.print_table(table, title_list)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            terminal_view.print_error_message("There is no such choice.")