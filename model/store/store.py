""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
from model import data_manager
from model import common


file_name = 'model/store/games.csv'
table = data_manager.get_table_from_file(file_name)


def show_table():
    """
    Display data from data files
    """

    title_list = ('ID', 'Name', 'Studio', 'Elements', 'Sales')
    return table, title_list


def make_record_to_add(inputs):

    generated_id = common.generate_random(table)
    record = []
    record.append(generated_id)
    for i in inputs:
        record.append(i)
    table_to_write = add(table, record)

    data_manager.write_table_to_file(file_name, table)


def add(table, record):
    """
    Add new record to table

    Args:
        table (list): table to add new record to
        record (list): new record

    Returns:
        list: Table with a new record
    """

    table.append(record)
   
    return table


def remove_record_from_file(id_):

    done_table = remove(table, id_)
    data_manager.write_table_to_file(file_name, done_table)


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for element in table:
        if id_ == element[0]:
            table.remove(element)
    return table


def update_record_from_table(inputs):

    record = []
    for i in table:
        common.send()
    # table_to_write = update(table, record)

    # data_manager.write_table_to_file(file_name, table)


def update(table, id_, record):
    """
    Updates specified record in the table.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update
        record (list): updated record

    Returns:
        list: table with updated record
    """

    # your code
    new_table = []
    for element in table:
        if id_ == element[0]:
            element = record
            new_table.append(element)
        else:
            new_table.append(element)
            
    table = new_table
    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code

