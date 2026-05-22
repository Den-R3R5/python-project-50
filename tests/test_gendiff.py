from pathlib import Path

from gendiff.gendiff import generate_diff


def get_test_data_pathlib(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_pathlib(filename).read_text()


def test1_gendiff_json():
    file1 = get_test_data_pathlib("file1.json")
    file2 = get_test_data_pathlib("file2.json")
    assert generate_diff(file1, file2) == read_file("result1-2.txt")


def test1_gendiff_yml():
    file1 = get_test_data_pathlib("file1.yml")
    file2 = get_test_data_pathlib("file2.yml")
    assert generate_diff(file1, file2) == read_file("result1-2.txt")


def test2_gendiff_json():
    file1 = get_test_data_pathlib("file3.json")
    file2 = get_test_data_pathlib("file4.json")
    assert generate_diff(file1, file2) == read_file("result3-4.txt")


def test2_gendiff_yml():
    file1 = get_test_data_pathlib("file3.yml")
    file2 = get_test_data_pathlib("file4.yml")
    assert generate_diff(file1, file2) == read_file("result3-4.txt")


def test_gendiff_plain_json():
    file1 = get_test_data_pathlib("file3.json")
    file2 = get_test_data_pathlib("file4.json")
    assert generate_diff(file1, file2, "plain") == read_file(
        "result3-4-plain.txt"
    )


def test_gendiff_plain_yml():
    file1 = get_test_data_pathlib("file3.yml")
    file2 = get_test_data_pathlib("file4.yml")
    assert generate_diff(file1, file2, "plain") == read_file(
        "result3-4-plain.txt"
    )


def test1_gendiff_to_json_format():
    file1 = get_test_data_pathlib("file3.json")
    file2 = get_test_data_pathlib("file4.json")
    assert generate_diff(file1, file2, "json") == read_file(
        "result3-4-json.txt"
    )


def test2_gendiff_to_json_format():
    file1 = get_test_data_pathlib("file3.yml")
    file2 = get_test_data_pathlib("file4.yml")
    assert generate_diff(file1, file2, "json") == read_file(
        "result3-4-json.txt"
    )
def test_t1():
    file1 = get_test_data_pathlib("t1.json")
    file2 = get_test_data_pathlib("t2.json")
    assert generate_diff(file1, file2, "plain") == read_file(
        "result_plain"
    )


def test_t2():
    file1 = get_test_data_pathlib("t1.yml")
    file2 = get_test_data_pathlib("t2.yml")
    assert generate_diff(file1, file2, ) == read_file(
        "result_stylish"
    )