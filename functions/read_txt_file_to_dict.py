from collections import OrderedDict

def read_txt_file_to_dict(filename):
    data_dict = OrderedDict()
    with open(filename) as textfile:
        while True:
            col_name = textfile.readline().strip()
            if col_name == "\n" or col_name.startswith("//"):
                continue
            col_name = col_name.replace('\n', '').replace("\"","").strip()
            if not col_name:
                break
            data_type = textfile.readline().strip()
            if data_type == "\n" or data_type.startswith("//"):
                while data_type == "\n" or data_type.startswith("//"):
                    data_type = textfile.readline().strip()
            data_type = data_type.replace('\n', '').replace("\"","").strip()
            if not data_type:
                raise ValueError("エラー：入力ファイルはコラムの数と定義の数が違います。")
            data_dict[col_name] = data_type
    return data_dict