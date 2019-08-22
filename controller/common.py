""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import store
from controller import store_controller
from model import common

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
    

def store_update(file_name, list_labels, title):
    id_ =  terminal_view.get_string('Updates element', 'ID: ')
    table, title_list = common.make_table(file_name)
    terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels,title)
    common.make_update(inputs,file_name,id_)





