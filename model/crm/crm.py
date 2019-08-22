""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
from model import data_manager
from model import common


file_name = 'model/crm/customers.csv'
table = data_manager.get_table_from_file(file_name)


def show_table():
    """
    Display data from data file
    """
    
    title_list = ('ID', 'Developer', 'E-mail Address', 'Elements')
    
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


def update_record_from_table(inputs):

    record = []
    for i in table:
        common.send()


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

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    # your code


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    # your code
