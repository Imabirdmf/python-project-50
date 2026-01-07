import json


def format(data: list) -> str:
    lines = {}
    for child in data:
        if child["type"] == "added":
            lines.update({child["key"]: child["value"]})
        elif child["type"] == "changed":
            lines.update({child["key"]: child["new_value"]})
        elif child["type"] == "nested":
            nested_str = format(child["children"])
            lines.update({child["key"]: json.loads(nested_str)})
        elif child["type"] == "unchanged":
            lines.update({child["key"]: child["value"]})
    serialized_lines = json.dumps(lines, indent=4, sort_keys=True)
    return serialized_lines
