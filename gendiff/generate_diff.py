def generate_diff(data1, data2):
    result = ["{"]
    for k in sorted(data1.keys() | data2.keys()):
        if k in data2 and k not in data1:
            result.append(f"+ {k}: {data2.get(k)}")
        elif k in data1 and k not in data2:
            result.append(f"- {k}: {data1[k]}")
        elif data1.get(k) == data2.get(k):
            result.append(f"  {k}: {data1[k]}")
        elif data1.get(k) != data2.get(k):
            result.append(f"- {k}: {data1[k]}")
            result.append(f"+ {k}: {data2[k]}")
    result.append("}")
    return "\n".join(result)
