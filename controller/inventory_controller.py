# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """


    title = "Inventory Menu"
    list_options = ('List', "Add", "Remove", "Update")
    exit_message = "Back do main menu"
    file_name = 'model/inventory/inventory.csv'
    title_labels = ('ID', 'Platform', 'Producer', 'Year', 'Elements')
    list_labels = ('Platform:', 'Producer:', 'Year:', 'Elements:')


    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == '1':
            common.show_table(file_name, title_labels)
        elif choice == '2':
            title = "Create record in inventory"
            common.fn_add(file_name, list_labels, title, inventory.add)
            common.show_table(file_name, title_labels)
        elif choice == '3':
            common.show_table(file_name, title_labels)
            common.remove_record_from_file(terminal_view.get_string("ID: "), inventory.remove, file_name, title_labels)
        elif choice == '4':
            common.show_table(file_name, title_labels)
            if common.fn_update(file_name, list_labels, 'Update', inventory.update):
                common.show_table(file_name, title_labels)
        else:
            terminal_view.print_error_message("There is no such choice.")