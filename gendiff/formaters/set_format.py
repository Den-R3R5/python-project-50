from .stylish_formater import stylish
from .plain_formater import plain

def set_format(tree, format_name):
    if format_name == "plain":
        return plain(tree)
    return stylish(tree)