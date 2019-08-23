""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
from model import data_manager
from model import common


file_name = 'model/accounting/items.csv'
table = data_manager.get_table_from_file(file_name)


def show_table():
    """
    Display data from data file
    """

    title_list = ('ID', 'Month', 'Day', 'Year', 'Announcement', 'Elements')
    
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

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
