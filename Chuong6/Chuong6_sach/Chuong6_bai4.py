# Câu 4: Đọc n dòng cuối file

def doc_n_dong_cuoi(filename, n):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines[-n:]:
            print(line, end="")
