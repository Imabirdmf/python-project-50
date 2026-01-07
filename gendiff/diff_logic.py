def dict_diff(data1: dict, data2: dict) -> list:
    result = []
    all_keys = sorted(data1.keys() | data2.keys())
    for k in all_keys:
        if k not in data1:
            result.append({"key": k, "type": "added", "value": data2[k]})
        elif k not in data2:
            result.append({"key": k, "type": "removed", "value": data1[k]})
        elif isinstance(data1[k], dict) and isinstance(data2[k], dict):
            result.append(
                {
                    "key": k,
                    "type": "nested",
                    "children": dict_diff(data1[k], data2[k]),
                }
            )
        elif data1[k] == data2[k]:
            result.append({"key": k, "type": "unchanged", "value": data1[k]})
        else:
            result.append(
                {
                    "key": k,
                    "type": "changed",
                    "old_value": data1[k],
                    "new_value": data2[k],
                }
            )
    return result
