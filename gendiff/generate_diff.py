import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

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
