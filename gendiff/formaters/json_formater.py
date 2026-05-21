def to_json(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, list):
        items = [to_json(item) for item in value]
        return f"[{', '.join(items)}]"
    if isinstance(value, dict):
        result = []
        for key, item in value.items():
            result.append(f'"{key}": {to_json(item)}')
        return f"{{{', '.join(result)}}}"
    return value
