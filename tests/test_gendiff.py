from gendiff import generate_diff


def test_extra_value_second():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1, "d": 2})
    expected = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                {'key': 'b', 'type': 'unchanged', 'value': 1},
                {'key': 'c', 'type': 'unchanged', 'value': 1},
                {'key': 'd', 'type': 'added', 'value': 2}]
    assert result == expected


def test_not_all_keys_in_second():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1})
    expected = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                {'key': 'b', 'type': 'unchanged', 'value': 1},
                {'key': 'c', 'type': 'removed', 'value': 1}]
    assert result == expected


def test_all_diff_values():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 2, "b": 2, "c": 2})
    expected = [{'key': 'a', 'type': 'changed', 'old_value': 1, 'new_value': 2},
                {'key': 'b', 'type': 'changed', 'old_value': 1, 'new_value': 2},
                {'key': 'c', 'type': 'changed', 'old_value': 1, 'new_value': 2}]
    assert result == expected


def test_all_same_values():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {"a": 1, "b": 1, "c": 1})
    expected = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                {'key': 'b', 'type': 'unchanged', 'value': 1},
                {'key': 'c', 'type': 'unchanged', 'value': 1}]
    assert result == expected


def test_empty_dicts():
    result = generate_diff({}, {})
    expected = []
    assert result == expected


def test_empty_dict():
    result = generate_diff({"a": 1, "b": 1, "c": 1}, {})
    expected = [{'key': 'a', 'type': 'removed', 'value': 1},
                {'key': 'b', 'type': 'removed', 'value': 1},
                {'key': 'c', 'type': 'removed', 'value': 1}]
    assert result == expected


def test_unique_value_in_second():
    result = generate_diff({"a": 2, "b": 2, "c": 2}, {"a": 2, "d": 2})
    exected = [{'key': 'a', 'type': 'unchanged', 'value': 2},
               {'key': 'b', 'type': 'removed', 'value': 2},
               {'key': 'c', 'type': 'removed', 'value': 2},
               {'key': 'd', 'type': 'added', 'value': 2}]
    assert result == exected


def test_boolean_values():
    result = generate_diff(
        {"a": True, "d": False, "e": False}, {"a": False, "d": True, "e": True}
    )
    exected = [{'key': 'a', 'type': 'changed', 'old_value': True, 'new_value': False},
               {'key': 'd', 'type': 'changed', 'old_value': False, 'new_value': True},
               {'key': 'e', 'type': 'changed', 'old_value': False, 'new_value': True}]
    assert result == exected


def test_mixed_values():
    result = generate_diff(
        {"a": True, "b": "abcd", "c": 1, "d": ["abc"], "e": None},
        {"a": False, "b": "abcdghjk", "c": 10, "d": ["abc", "new"], "f": {"g": 0}},
    )
    exected = [{'key': 'a', 'type': 'changed', 'old_value': True, 'new_value': False},
               {'key': 'b', 'type': 'changed', 'old_value': 'abcd', 'new_value': 'abcdghjk'},
               {'key': 'c', 'type': 'changed', 'old_value': 1, 'new_value': 10},
               {'key': 'd', 'type': 'changed', 'old_value': ['abc'], 'new_value': ['abc', 'new']},
               {'key': 'e', 'type': 'removed', 'value': None},
               {'key': 'f', 'type': 'added', 'value': {'g': 0}}]
    assert result == exected


def test_sort_keys():
    result = generate_diff(
        {"a": True, "b": "abcd", "c": 1, "d": ["abc"], "e": None},
        {"e": None, "c": 1, "a": True, "d": ["abc"], "b": "abcd"},
    )
    exected = [{'key': 'a', 'type': 'unchanged', 'value': True},
               {'key': 'b', 'type': 'unchanged', 'value': 'abcd'},
               {'key': 'c', 'type': 'unchanged', 'value': 1},
               {'key': 'd', 'type': 'unchanged', 'value': ['abc']},
               {'key': 'e', 'type': 'unchanged', 'value': None}]
    assert result == exected


def test_single_key():
    result = generate_diff({"z": 1}, {"z": 2})
    expected = [{'key': 'z', 'type': 'changed', 'old_value': 1, 'new_value': 2}]
    assert result == expected


def test_dict_value_as_plain_value():
    result = generate_diff({"a": {"b": 1}}, {"a": {"b": 2}})
    expected = [{'key': 'a', 'type': 'nested', 'children':
        [{'key': 'b', 'type': 'changed', 'old_value': 1, 'new_value': 2}]
                 }]
    assert result == expected


def test_none_removed():
    result = generate_diff({"a": None}, {})
    expected = [{'key': 'a', 'type': 'removed', 'value': None}]
    assert result == expected


def test_none_added():
    result = generate_diff({}, {"a": None})
    expected = [{'key': 'a', 'type': 'added', 'value': None}]
    assert result == expected


def test_int_and_str_diff():
    result = generate_diff({"a": 1}, {"a": "1"})
    expected = [{'key': 'a', 'type': 'changed', 'old_value': 1, 'new_value': '1'}]
    assert result == expected
