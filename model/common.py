""" Common functions for models
implement commonly used functions here
"""
import random
from model import data_manager
import controller.store_controller
import controller.common
from model.store import store
from model.hr import hr
from model.inventory import inventory
from model.accounting import accounting
from model.sales import sales
from model.crm import crm


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''
    first_id = table[0][0]
    the_string = []
    digits = '0123456789'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    other = '!@#$%^&*()_+-={[]}|<>'
    

    for char in first_id:
        if char.isdigit():
            the_string.append(random.choice(digits))
        elif char.isupper():
            the_string.append(random.choice(upper))
        elif char.islower():
            the_string.append(random.choice(lower))
        else:
            the_string.append(random.choice(other))

    generated = ''.join(the_string)
    return generated

def print_line(width_list,unit_list):

    line = []
    for k, space in enumerate(unit_list):
        front = ((width_list[k] - len(space)) // 2)
        line.append('|')
        line.append(' ' * (front + 1))
        line.append(space)
        line.append(' ' * (front + (width_list[k] - len(space)) % 2 + 1))
    line.append('|')    
    to_print_line = ''.join(line)
    return to_print_line

def make_table(file_name, title_list = ""): #  return to show list 
    """
    Display data from data file
    """
    table = data_manager.get_table_from_file(file_name)
    return table, title_list


def make_record_to_add(inputs, file_name):
    table = data_manager.get_table_from_file(file_name)
    generated_id = generate_random(table)
    record = []
    record.append(generated_id)
    for i in inputs:
        record.append(i)
    table_to_write = store.add(table, record)

    data_manager.write_table_to_file(file_name, table_to_write)


def make_update(inputs, file_name, id_):
    table = data_manager.get_table_from_file(file_name)
    record = []
    record.append(id_)
    for i in inputs:
        record.append(i)

    table_to_write =  store.update(table, id_, record)
    data_manager.write_table_to_file(file_name, table_to_write)


def model_remowe(file_name, done_table):
    data_manager.write_table_to_file(file_name, done_table)
