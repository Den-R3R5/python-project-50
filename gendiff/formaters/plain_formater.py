def _format(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    return f"'{value}'"


def plain(tree, depth=1, directory=''):
    result = []
    
    for node in tree:
        node_type = node["type"]
        key = node["key"]

        if node_type == "attached":

            inner = plain(node["children"], depth + 1, directory + f"{key}.")
            
            print(directory)
            result.append(f"{inner}")
        elif node_type == "changed":
            result.append(f"Property '{directory}{key}' was updated. From {_format(node['value_old'], depth)} to {_format(node['value_new'], depth)}")
        elif node_type == "deleted":
            result.append(f"Property '{directory}{key}' was removed")
        elif node_type == "added":
            result.append(f"Property '{directory}{key}' was added with value: {_format(node['value'], depth)}")
    return "\n".join(result)
