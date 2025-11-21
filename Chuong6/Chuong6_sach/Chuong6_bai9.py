# Câu 9

def tinh_tong_va_noi_vao_cuoi(filename="data71.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        nums = f.read().split()

    nums = list(map(int, nums))
    tong = sum(nums)

    with open(filename, 'a', encoding='utf-8') as f:
        f.write("\nTổng = " + str(tong))

    print("Đã ghi tổng vào cuối file.")
