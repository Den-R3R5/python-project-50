from .json_formater import to_json
from .plain_formater import plain
from .stylish_formater import stylish


def set_format(tree, format_name):
    if format_name == "plain":
        return plain(tree)
    if format_name == "json":
        return to_json(tree)
    return stylish(tree)
