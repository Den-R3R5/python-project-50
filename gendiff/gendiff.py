import json


def _load_and_sort_files(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    return dict(sorted(first_file.items())), dict(sorted(second_file.items()))


def _to_lower_bool(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(first_file, second_file):
    first_file, second_file = _load_and_sort_files(first_file, second_file)
    keys_massive = sorted(first_file.keys() | second_file.keys())
    result = ["{"]
    for key in keys_massive:
        if key in first_file and key in second_file:
            if first_file[key] == second_file[key]:
                result.append(f"    {key}: {_to_lower_bool(first_file[key])}")
            else:
                result.append(f"  - {key}: {_to_lower_bool(first_file[key])}")
                result.append(f"  + {key}: {_to_lower_bool(second_file[key])}")
        elif key in first_file:
            result.append(f"  - {key}: {_to_lower_bool(first_file[key])}")
        else:
            result.append(f"  + {key}: {_to_lower_bool(second_file[key])}")
    result.append("}")
    return "\n".join(result)
