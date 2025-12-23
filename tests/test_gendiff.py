from gendiff import generate_diff


def test_extra_value_second():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1, "d": 2})
    expected = "{\n  a: 1\n  b: 1\n  c: 1\n+ d: 2\n}"
    assert result == expected


def test_not_all_keys_in_second():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1})
    expected = "{\n  a: 1\n  b: 1\n- c: 1\n}"
    assert result == expected


def test_all_diff_values():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 2, "b": 2, "c": 2})
    expected = "{\n- a: 1\n+ a: 2\n- b: 1\n+ b: 2\n- c: 1\n+ c: 2\n}"
    assert result == expected


def test_all_same_values():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1})
    expected = "{\n  a: 1\n  b: 1\n  c: 1\n}"
    assert result == expected


def test_empty_dicts():
    d = dict()
    result = generate_diff(d, d)
    expected = "{\n}"
    assert result == expected


def test_empty_dict():
    d = dict()
    result = generate_diff({"a": 1, "b": 1, "c": 1}, d)
    expected = "{\n- a: 1\n- b: 1\n- c: 1\n}"
    assert result == expected


def test_unique_value_in_second():
    result = generate_diff({"a": 2, "b": 2, "c": 2}, {"a": 2, "d": 2})
    exected = "{\n  a: 2\n- b: 2\n- c: 2\n+ d: 2\n}"
    assert result == exected


def test_boolean_values():
    result = generate_diff(
        {"a": True, "d": False, "e": False}, {"a": False, "d": True, "e": True}
    )
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
    result = generate_diff(
        {"a": True, "b": "abcd", "c": 1, "d": ["abc"], "e": None},
        {"a": False, "b": "abcdghjk", "c": 10, "d": ["abc", "new"], "f": {"g": 0}},
    )
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
    result = generate_diff(
        {"a": True, "b": "abcd", "c": 1, "d": ["abc"], "e": None},
        {"e": None, "c": 1, "a": True, "d": ["abc"], "b": "abcd"},
    )
    exected = "{\n  a: True\n  b: abcd\n  c: 1\n  d: ['abc']\n  e: None\n}"
    assert result == exected


def test_single_key():
    result = generate_diff({"z": 1}, {"z": 2})
    expected = "{\n- z: 1\n+ z: 2\n}"
    assert result == expected


def test_dict_value_as_plain_value():
    result = generate_diff({"a": {"b": 1}}, {"a": {"b": 2}})
    expected = "{\n- a: {'b': 1}\n+ a: {'b': 2}\n}"
    assert result == expected


def test_none_removed():
    result = generate_diff({"a": None}, {})
    expected = "{\n- a: None\n}"
    assert result == expected


def test_none_added():
    result = generate_diff({}, {"a": None})
    expected = "{\n+ a: None\n}"
    assert result == expected


def test_int_and_str_diff():
    result = generate_diff({"a": 1}, {"a": "1"})
    expected = "{\n- a: 1\n+ a: 1\n}"
    assert result == expected
