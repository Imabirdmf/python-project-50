import json

import pytest
import yaml

from gendiff.run_diff import run_diff

EXPECTED = {
    ("test_data_json/4.0.json", "test_data_yaml/4.0.yaml"): {
        "stylish": "expected/no_diff_json_yaml_stylish.txt",
        "plain": "expected/no_diff_json_yaml_plain.txt",
    },
    ("test_data_yaml/1.0.yaml", "test_data_yaml/1.0.yml"): {
        "stylish": "expected/no_diff_yaml_stylish.txt",
        "plain": "expected/no_diff_json_yaml_plain.txt",
    },
    ("test_data_json/4.0.json", "test_data_json/4.1.json"): {
        "stylish": "expected/diff_json_json_stylish.txt",
        "plain": "expected/diff_json_json_plain.txt",
    },
    ("test_data_json/nested1.json", "test_data_json/nested2.json"): {
        "stylish": "expected/nested_stylish.txt",
        "plain": "expected/nested_plain.txt",
    },
}


@pytest.mark.parametrize("file1, file2", EXPECTED.keys())
@pytest.mark.parametrize("format_name", ["stylish", "plain"])
def test_diff_files(file1, file2, format_name):
    expected_file = EXPECTED[(file1, file2)][format_name]
    result = run_diff(f"tests/{file1}", f"tests/{file2}", format_name=format_name)

    with open(f"tests/{expected_file}", "r") as f:
        expected = f.read()
    assert result == expected


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        run_diff("non_existent.json", "tests/test_data/4.0.json")


def test_invalid_json():
    with pytest.raises(json.JSONDecodeError):
        run_diff("tests/test_data_json/invalid.json", "tests/test_data_json/4.0.json")


def test_invalid_yaml():
    with pytest.raises(yaml.YAMLError):
        run_diff("tests/test_data_yaml/invalid.yaml", "tests/test_data_yaml/4.0.yaml")


def test_invalid_file_type():
    with pytest.raises(ValueError):
        run_diff("tests/test_data_yaml/yaml.doc", "tests/test_data_json/json.xls")


def test_unknown_formatter():
    with pytest.raises(ValueError):
        run_diff(
            "tests/test_data_json/4.0.json",
            "tests/test_data_json/4.0.json",
            format_name="xml",
        )
