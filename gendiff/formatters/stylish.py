def format_value(value, depth=0):
    indent_size = depth * 4
    indent = " " * indent_size
    key_indent = " " * (indent_size + 4)
    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{key_indent}{k}: {format_value(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)

    elif value is None:
        return "null"

    elif isinstance(value, bool):
        return "true" if value else "false"

    return value


def format_child(child: dict, depth):
    indent = " " * (depth * 4 + 2)
    key = child["key"]
    child_type = child["type"]

    if child_type == "added":
        formatted_value = format_value(child["value"], depth + 1)
        yield f"{indent}+ {key}: {formatted_value}"

    if child_type == "unchanged":
        formatted_value = format_value(child["value"], depth + 1)
        yield f"{indent}  {key}: {formatted_value}"

    if child_type == "removed":
        formatted_value = format_value(child["value"], depth + 1)
        yield f"{indent}- {key}: {formatted_value}"

    if child_type == "changed":
        formatted_value_old = format_value(child["old_value"], depth + 1)
        formatted_value_new = format_value(child["new_value"], depth + 1)
        yield f"{indent}- {key}: {formatted_value_old}"
        yield f"{indent}+ {key}: {formatted_value_new}"

    if child_type == "nested":
        nested_str = format_stylish(child["children"], depth + 1)
        yield f"{indent}  {key}: {nested_str}"


def format_stylish(data: list, depth: int = 0):
    indent = " " * depth * 4
    lines = ["{"]

    for child in data:
        lines.extend(format_child(child, depth))

    lines.append(f"{indent}}}")
    return "\n".join(lines)
