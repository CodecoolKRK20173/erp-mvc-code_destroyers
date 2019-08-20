""" Common functions for models
implement commonly used functions here
"""
import random
import string

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
    the_string=[]
    digits='0123456789'
    lower='abcdefghijklmnopqrstuvwxyz'
    upper=lower.upper()
    other='!@#$%^&*()_+-={[]}|<>'
    for char in first_id:
        if char.isdigit():
            the_string.append(random.choice(digits))
        elif char.isupper():
            the_string.append(random.choice(upper))
        elif char.islower():
            the_string.append(random.choice(lower))
        else:
            the_string.append(random.choice(other))
    # your code
    generated=''.join(the_string)
    return generated

def print_line(width_list,unit_list):
    line=[]
    for k,space in enumerate(unit_list):
        front=((width_list[k]-len(space))//2)
        line.append('|')
        line.append(' '*(front+1))
        line.append(space)
        line.append(' '*(front+(width_list[k]-len(space))%2+1))
    line.append('|')    
    to_print_line=''.join(line)
    return to_print_line
