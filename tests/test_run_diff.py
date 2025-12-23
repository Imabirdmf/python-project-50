import json

import pytest
import yaml

from gendiff.run_diff import run_diff


def test_diff_json_yaml():
    result = run_diff("tests/test_data_json/4.0.json", "tests/test_data_yaml/4.0.yaml")
    assert result == "{\n  a: True\n  b: abcd\n  c: 1\n  d: ['abc']\n  e: None\n}"


def test_diff_json_json():
    result = run_diff("tests/test_data_json/4.0.json", "tests/test_data_json/4.1.json")
    assert result == (
        "{\n"
        "- a: True\n"
        "+ a: False\n"
        "- b: abcd\n"
        "+ b: abcdghjk\n"
        "- c: 1\n"
        "+ c: 10\n"
        "- d: ['abc']\n"
        "+ d: ['abc', 'new']\n"
        "- e: None\n"
        "+ f: {'g': 0}\n}"
    )


def test_diff_yaml_yml():
    result = run_diff("tests/test_data_yaml/1.0.yaml", "tests/test_data_yaml/1.0.yml")
    assert result == "{\n  a: 1\n  b: 1\n  c: 1\n}"


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
