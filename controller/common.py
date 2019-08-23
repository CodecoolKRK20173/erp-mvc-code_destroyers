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

def show_table(file_name, title_list):
    table, title_list  = common.make_table(file_name, title_list)
    terminal_view.print_table(table,title_list)


def fn_add(file_name, list_labels, title, function_):
    
    table, title_list = common.make_table(file_name, list_labels)
   # terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels, title)
    common.make_record_to_add(inputs, file_name, function_)
    terminal_view.clear()


def remove_record_from_file(id_ , fun_, file_name, title_list):
   
    table = common.make_table(file_name)[0]
    done_table = fun_(table, id_)
    common.model_remove(file_name, done_table)
    #terminal_view.print_table(table, title_list)
    terminal_view.clear()


def fn_update(file_name, list_labels, title, function_):
   
    id_ =  terminal_view.get_string('Updates element \nID: ')
    table, title_list = common.make_table(file_name, list_labels)
   # terminal_view.print_table(table, title_list)
    inputs = terminal_view.get_inputs(list_labels, title)
    common.make_update(inputs, file_name, id_, function_)
    terminal_view.clear()