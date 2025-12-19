import json

def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)


        result = '{\n'
        for k in sorted(max(data1, data2, key=len)):
            if data1.get(k) is None:
                result += f'+ {k}: {data2[k]}\n'
            elif data2.get(k) is None:
                result += f'- {k}: {data1[k]}\n'
            elif data1.get(k) == data2.get(k):
                result += f'  {k}: {data1[k]}\n'
            elif data1.get(k) != data2.get(k):
                result += f'- {k}: {data1[k]}\n'\
                      f'+ {k}: {data2[k]}\n'
        result += '}'
        return result