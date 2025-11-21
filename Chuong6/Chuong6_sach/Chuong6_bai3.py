# Câu 3: Nối thêm 1 chuỗi vào cuối file

def noi_chuoi_vao_file(filename, text):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text + "\n")
    print("Đã ghi vào cuối file.")
