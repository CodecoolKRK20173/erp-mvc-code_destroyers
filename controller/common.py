""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import store
from model import hr
from model import inventory
from model import accounting
from model import sales
from model import crm
from controller import store_controller
from model import common

<<<<<<< HEAD
def show_table(file_name):
    table, title_list  = common.make_table(file_name)
    terminal_view.print_table(table,title_list)

def store_add(file_name, list_labels, title):
    table, title_list = common.make_table(file_name)
    terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels,title)
    common.make_record_to_add(inputs,file_name)

def remove_record_from_file(id_ , fun_, file_name):
    table, title_list = common.make_table(file_name)
    done_table = fun_(table, id_)
    common.model_remowe(file_name, done_table)
    
=======

def show_table(file_name, title_list):
>>>>>>> f5735d700ba0c7cf4d75835d3d2139be4b27d9f3

    table, title_list = common.make_table(file_name, title_list)
    terminal_view.print_table(table, title_list)


def store_add(file_name, list_labels, title):

    table, title_list = common.make_table(file_name, list_labels)
    terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels, title)
    common.make_record_to_add(inputs, file_name)


def store_update(file_name, list_labels, title):

    id_ =  terminal_view.get_string('Updates element \nID: ')
    table, title_list = common.make_table(file_name, list_labels)
    terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels, title)
    common.make_update(inputs, file_name, id_)