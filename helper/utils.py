import re

def is_digit(input_str):
    return re.match(r'^[0-9]*$', input_str)