# everything you'll need is imported:
from model.hr import hr
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

    title = "HR Menu"
    list_options = ('List', "Add", "Remove", "Update")
    exit_message = "Back do main menu"
    file_name = 'model/hr/persons.csv'
    title_labels = ('ID', 'Developer', 'Year')
    list_labels = ('Developer:', 'Year:')


    choice = None
    while choice != '0':
        choice = terminal_view.get_choice(title, list_options, exit_message)
        if choice == '1':
            common.show_table(file_name, title_labels)
        elif choice == '2':
            title = "Create record in HR"
            common.fn_add(file_name, list_labels, title, hr.add)
            common.show_table(file_name, title_labels)
        elif choice == '3':
            common.show_table(file_name, title_labels)
            common.remove_record_from_file(terminal_view.get_string("ID: "), hr.remove, file_name, title_labels)
        elif choice == '4':
            common.show_table(file_name, title_labels)
            if common.fn_update(file_name, list_labels, 'Update', hr.update):
                common.show_table(file_name, title_labels)
        else:
            terminal_view.print_error_message("There is no such choice.")