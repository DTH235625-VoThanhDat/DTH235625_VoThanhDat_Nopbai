def KiemTraSoNguyenTo(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True

def Nhap(songuyen) -> list:
    n = int(input("Nhập số phần tử của danh sách: "))
    for i in range(n):
        print("Nhập phần tử thứ", i + 1, ": ", end="")
        so = int(input())
        songuyen.append(so)

def KiemTraK(songuyen, k):
    dem = 0
    if k in songuyen:
     dem = dem + 1
    print("Số k xuất hiện trong danh sách", dem, "lần")

def TongSoNguyenTo(songuyen):
    tong = 0
    for so in songuyen:
        if KiemTraSoNguyenTo(so):
            tong += so
    print("Tổng các số nguyên tố trong danh sách là:", tong)

songuyen = []
Nhap(songuyen) 
print("Danh sách các số nguyên đã nhập:", songuyen)

print("TÌM SỐ K XUẤT HIỆN TRONG DANH SÁCH")
k = int(input("Nhập sô k: "))
KiemTraK(songuyen, k)

print("TỔNG CÁC SỐ NGUYÊN TỐ TRONG DANH SÁCH:")
TongSoNguyenTo(songuyen)

print("SẮP XẾP DANH SÁCH TĂNG DẦN:")
songuyen.sort()
print("Danh sách sau khi sắp xếp:", songuyen)

songuyen.clear()
print("Danh sách sau khi xóa:", songuyen)