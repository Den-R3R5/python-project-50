import json
from pathlib import Path



def _check_format(file_path):
    return Path(file_path).suffix


def _load_file(file_path):
    file_format = _check_format(file_path)
    with open(file_path, "r") as f:
        if file_format in ".json":
            return json.load(f)


def parse(first_file, second_file):
    first_file_parsed = _load_file(first_file)
    second_file_parsed = _load_file(second_file)
    return dict(first_file_parsed.items()), dict(second_file_parsed.items())
