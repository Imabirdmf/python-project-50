from gendiff import generate_diff


def test_diff_values():
    result = generate_diff("files/file1.json", "files/file2.json")
    expected = "{\n- follow: False\n  host: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n}"
    assert result == expected
