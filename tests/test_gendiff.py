from pathlib import Path

from gendiff.gendiff import generate_diff
from gendiff.parse import parse


def get_test_data_pathlib(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_pathlib(filename).read_text()


def test_gendiff_json():
    file1 = get_test_data_pathlib("file1.json")
    file2 = get_test_data_pathlib("file2.json")
    file1, file2 = parse(file1, file2)
    assert generate_diff(file1, file2) == read_file("result.txt")


def test_gendiff_yml():
    file1 = get_test_data_pathlib("file1.yml")
    file2 = get_test_data_pathlib("file2.yml")
    file1, file2 = parse(file1, file2)
    assert generate_diff(file1, file2) == read_file("result.txt")
