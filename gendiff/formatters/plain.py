def format(data, path=None):
    def format_value(d):
        if type(d) in (dict, list):
            return "[complex value]"
        elif d is None:
            return "null"
        elif isinstance(d, bool):
            return "true" if d else "false"
        else:
            return repr(d)

    path = path or []
    lines = []
    for child in data:
        path.append(child["key"])
        if child["type"] == "added":
            formatted_value = format_value(child["value"])
            lines.append(
                f"Property {repr('.'.join(path))} was added with value: {formatted_value}"
            )
        elif child["type"] == "removed":
            lines.append(f"Property {repr('.'.join(path))} was removed")
        elif child["type"] == "changed":
            formatted_value_old = format_value(child["old_value"])
            formatted_value_new = format_value(child["new_value"])
            lines.append(
                f"Property {repr('.'.join(path))} was updated. "
                f"From {formatted_value_old} to {formatted_value_new}"
            )
        elif child["type"] == "nested":
            nested_str = format(child["children"], path)
            lines.append(nested_str)
        path.pop()
    return f"{'\n'.join(lines)}\n" if not path else "\n".join(lines)
