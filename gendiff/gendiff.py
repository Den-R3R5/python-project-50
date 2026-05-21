from .stylish_formater import stylish


def diff_builder(first_file, second_file):
    keys_massive = sorted(first_file.keys() | second_file.keys())
    result = []
    for key in keys_massive:
        if key in first_file and key in second_file:
            if isinstance(first_file[key], dict) and isinstance(
                second_file[key], dict
            ):
                result.append({
                    "key": key,
                    "type": "attached",
                    "children": diff_builder(first_file[key], second_file[key]),
                })
            elif first_file[key] == second_file[key]:
                result.append({
                    "key": key,
                    "type": "unchanged",
                    "value": first_file[key],
                })
            else:
                result.append({
                    "key": key,
                    "type": "changed",
                    "value_old": first_file[key],
                    "value_new": second_file[key],
                })
        elif key in first_file:
            result.append({
                "key": key,
                "type": "deleted",
                "value": first_file[key],
            })
        else:
            result.append({
                "key": key,
                "type": "added",
                "value": second_file[key],
            })
    return result


def generate_diff(first_file, second_file, format_name="stylish"):
    tree = diff_builder(first_file, second_file)
    result = stylish(tree)
    return result
