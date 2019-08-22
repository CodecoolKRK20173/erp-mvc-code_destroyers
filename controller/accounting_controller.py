# everything you'll need is imported:
from model.accounting import accounting
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


    title = "Accounting Menu"
    list_options = ('List', "Add", "Remove", "Update")
    exit_message = "Back do main menu"
    file_name = 'model/accounting/items.csv'
    title_labels = ('ID', 'Month', 'Day', 'Year', 'Announcement', 'Elements')
    list_labels = ('Month:', 'Day:', 'Year:', 'Announcement:', 'Elements:')


    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == '1':
            common.show_table(file_name, title_labels)
        elif choice == '2':
            title = "Create record in store"
            common.fn_add(file_name, list_labels, title, accounting.add)
            common.show_table(file_name, title_labels)
        elif choice == '3':
            common.show_table(file_name, title_labels)
            common.remove_record_from_file(terminal_view.get_string("ID: "), accounting.remove, file_name, title_labels)
        elif choice == '4':
            common.show_table(file_name, title_labels)
            common.fn_update(file_name, list_labels, 'Update', accounting.update)
            common.show_table(file_name, title_labels)
        else:
            terminal_view.print_error_message("There is no such choice.")