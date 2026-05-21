def _format(value, depth):
    indent = (4 * (depth + 1)) * " "
    close_indent = 4 * (depth) * " "
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        result = ["{"]

        for key, val in value.items():
            inner = _format(val, depth + 1)
            result.append(f"{indent}{key}: {inner}")
        result.append(f"{close_indent}}}")
        return "\n".join(result)
    return value

def stylish(tree, depth=1):
    result = ["{"]
    for node in tree:
        indent = (4 * depth) * " "
        sign_indent = (4 * depth - 2) * " "
        close_indent = 4 * (depth - 1) * " "
        node_type = node["type"]
        key = node["key"]

        if node_type == "attached":
            inner = stylish(node["children"], depth + 1)
            result.append(f"{indent}{key}: {inner}")
        elif node_type == "unchanged":
            result.append(f"{indent}{key}: {_format(node["value"], depth)}")
        elif node_type == "changed":
            result.append(f"{sign_indent}- {key}: {_format(node["value_old"], depth)}")
            result.append(f"{sign_indent}+ {key}: {_format(node["value_new"], depth)}")
        elif node_type == "deleted":
            result.append(f"{sign_indent}- {key}: {_format(node["value"], depth)}")
        elif node_type == "added":
            result.append(f"{sign_indent}+ {key}: {_format(node["value"], depth)}")
    result.append(f"{close_indent}}}")
    return "\n".join(result)