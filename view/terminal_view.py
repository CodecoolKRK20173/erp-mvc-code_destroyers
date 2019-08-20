""" Terminal view module """


def print_table(table, title_list):
    from model.common import print_line
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    # your goes code
    if len(title_list)==len(table[0]):
        width=[]
        columns=len(title_list)

        for k,title in enumerate(title_list):
            width.append(len(title))
        for line in table:
            for k,space in enumerate(line):
                if width[k]<len(space):
                    width[k]=len(space)
        full_width=len(width)*2+len(width)-1
        for unit in width:
            full_width+=unit
        
        
        line1=''.join(['/','-'*full_width,'\\'])
        line3=''.join(['\\','-'*full_width,'/'])
        
    
        print(line1)
        print(print_line(width,title_list))
        
        for line in table:
            for k,space in enumerate(line):
                linex='-'*(width[k]+2)
                print(f'|{linex}',end='')
            print('|')
            print(print_line(width,line))
        print(line3)

    else:
        print_error_message('Wrong number of titles to the table')
        

    




def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
    print(label,end=' : ')
    print(result)

def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(title,'\n')
    for k,line in enumerate(list_options,1):
        print(f' ({k}) {line}.')
    print(f' (0) {exit_message}')
    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code
    print(title)
    for line in list_labels:
        ans=input(f'{line} : ')
        inputs.append(ans)
    return inputs

def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code

    print('Oops! ', message)
