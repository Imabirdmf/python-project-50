import json

import pytest

from gendiff import generate_diff


def test_extra_value_second():
    result = generate_diff("tests/test_data/1.0.json", "tests/test_data/1.1.json")
    expected = "{\n  a: 1\n  b: 1\n  c: 1\n+ d: 2\n}"
    assert result == expected


def test_not_all_keys_in_second():
    result = generate_diff("tests/test_data/1.0.json", "tests/test_data/1.2.json")
    expected = "{\n  a: 1\n  b: 1\n- c: 1\n}"
    assert result == expected


def test_all_diff_values():
    result = generate_diff("tests/test_data/1.0.json", "tests/test_data/2.0.json")
    expected = "{\n- a: 1\n+ a: 2\n- b: 1\n+ b: 2\n- c: 1\n+ c: 2\n}"
    assert result == expected


def test_all_same_values():
    result = generate_diff("tests/test_data/1.0.json", "tests/test_data/1.0.json")
    expected = "{\n  a: 1\n  b: 1\n  c: 1\n}"
    assert result == expected


def test_empty_files():
    result = generate_diff("tests/test_data/empty.json", "tests/test_data/empty.json")
    expected = "{\n}"
    assert result == expected


def test_unique_value_in_second():
    result = generate_diff("tests/test_data/2.0.json", "tests/test_data/2.1.json")
    exected = "{\n  a: 2\n- b: 2\n- c: 2\n+ d: 2\n}"
    assert result == exected


def test_boolean_values():
    result = generate_diff("tests/test_data/3.0.json", "tests/test_data/3.1.json")
    exected = (
        "{\n"
        "- a: True\n"
        "+ a: False\n"
        "- d: False\n"
        "+ d: True\n"
        "- e: False\n"
        "+ e: True\n}"
    )
    assert result == exected


def test_mixed_values():
    result = generate_diff("tests/test_data/4.0.json", "tests/test_data/4.1.json")
    exected = (
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
    assert result == exected


def test_sort_keys():
    result = generate_diff("tests/test_data/4.0.json", "tests/test_data/4.2.json")
    exected = "{\n  a: True\n  b: abcd\n  c: 1\n  d: ['abc']\n  e: None\n}"
    assert result == exected


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        generate_diff("non_existent.json", "tests/test_data/4.0.json")


def test_invalid_json():
    with pytest.raises(json.JSONDecodeError):
        generate_diff("tests/test_data/invalid.json", "tests/test_data/4.0.json")
