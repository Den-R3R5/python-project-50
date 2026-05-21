def _format(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
