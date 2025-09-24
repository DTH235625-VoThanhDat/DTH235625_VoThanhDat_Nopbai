import math
def KiemTraSoNguyenTo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)), 1):
        if n % i == 0:
            return False
    return True

while True:
    n = int(input("Nhập một số nguyên dương n: "))
    if KiemTraSoNguyenTo(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")

    hoi = input("Bạn có muốn tiếp tục không (c/k)? ")
    if hoi.lower() == 'k':
        break