from gendiff import generate_diff


def test_diff_values():
    result = generate_diff("files/file1.json", "files/file2.json")
    expected = (
        "{\n"
        "- follow: False\n"
        "  host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50\n"
        "+ timeout: 20\n}"
    )
    assert result == expected

def test_all_diff_values_first():
    result = generate_diff("tests/test_data/empty.json", "tests/test_data/full.json")
    expected = (
        "{\n"
        "+ follow: False\n"
        "+ host: hexlet.io\n"
        "+ proxy: 123.234.53.22\n"
        "+ timeout: 50\n}"
    )
    assert result == expected

def test_all_diff_values_second():
    result = generate_diff("tests/test_data/full.json", "tests/test_data/empty.json")
    expected = (
        "{\n"
        "- follow: False\n"
        "- host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50\n}"
    )
    assert result == expected

def test_all_diff_values():
    result = generate_diff("tests/test_data/full.json", "tests/test_data/full_with_diff_values.json")
    expected = (
        "{\n"
        "- follow: False\n"
        "+ follow: True\n"
        "- host: hexlet.io\n"
        "+ host: google.com\n"
        "- proxy: 123.234.53.22\n"
        "+ proxy: 125.534.23.52\n"
        "- timeout: 50\n"
        "+ timeout: 40\n}"
    )
    assert result == expected

def test_all_same_values():
    result = generate_diff("tests/test_data/full.json", "tests/test_data/full.json")
    expected = (
        "{\n"
        "  follow: False\n"
        "  host: hexlet.io\n"
        "  proxy: 123.234.53.22\n"
        "  timeout: 50\n}"
    )
    assert result == expected