# Câu 5: Đếm số dòng và số từ trong file

def dem_dong_tu(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    so_dong = len(lines)
    so_tu = sum(len(line.split()) for line in lines)

    print("Số dòng:", so_dong)
    print("Số từ:", so_tu)
