def format(data: list, depth: int = 0):
    def format_value(d, depth=0):
        indent_size = depth * 4
        indent = " " * indent_size
        key_indent = " " * (indent_size + 4)
        if isinstance(d, dict):
            result = ["{"]
            for k, v in d.items():
                result.append(f"{key_indent}{k}: {format_value(v, depth + 1)}")
        elif d is None:
            return "null"
        elif isinstance(d, bool):
            return "true" if d else "false"
        else:
            return d
        result.append(f"{indent}}}")
        return "\n".join(result)

    indent_size = depth * 4
    child_indent = " " * (indent_size + 2)
    closing_indent = " " * indent_size
    lines = ["{"]
    for child in data:
        if child["type"] == "added":
            formatted_value = format_value(child["value"], depth + 1)
            lines.append(f"{child_indent}+ {child['key']}: {formatted_value}")
        elif child["type"] == "removed":
            formatted_value = format_value(child["value"], depth + 1)
            lines.append(f"{child_indent}- {child['key']}: {formatted_value}")
        elif child["type"] == "changed":
            formatted_value_old = format_value(child["old_value"], depth + 1)
            formatted_value_new = format_value(child["new_value"], depth + 1)
            lines.append(f"{child_indent}- {child['key']}: {formatted_value_old}")
            lines.append(f"{child_indent}+ {child['key']}: {formatted_value_new}")
        elif child["type"] == "nested":
            nested_str = format(child["children"], depth + 1)
            lines.append(f"{child_indent}  {child['key']}: {nested_str}")
        elif child["type"] == "unchanged":
            formatted_value = format_value(child["value"], depth + 1)
            lines.append(f"{child_indent}  {child['key']}: {formatted_value}")
    lines.append(f"{closing_indent}}}")
    return f"{'\n'.join(lines)}\n" if depth == 0 else "\n".join(lines)
