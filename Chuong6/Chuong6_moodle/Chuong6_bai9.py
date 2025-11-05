def Nhap(songuyen) ->list:
    n = int(input("Nhập số các phần tủ của danh sách: "))
    for i in range(n):
        print("Nhập phần tử thứ", i+1, ": ", end="")
        so = int(input())
        songuyen.append(so)

def MangLe(songuyen) -> list:
    Le = []
    for so in songuyen:
        if so % 2 != 0:
            Le.append(so)
    return Le

def MangChan(songuyen) -> list:
    Chan = []
    for so in songuyen:
        if so % 2 == 0:
            Chan.append(so)
    return Chan

def KiemTraSoNguyenTo(n):
    if n<2:
        return False
    for i in range(2, int(n*0.5) + 1):
        if n % i ==0:
            return False
    return True

def MangNguyenTo(songuyen) -> list:
    NguyenTo = []
    for so in songuyen:
        if KiemTraSoNguyenTo(so):
            NguyenTo.append(so)
    return NguyenTo

def MangKhongNguyenTo(songuyen) -> list:
    KhongNguyenTo = []
    for so in songuyen:
        if KiemTraSoNguyenTo(so) == False:
            KhongNguyenTo.append(so)
    return KhongNguyenTo

SoNguyen = []
Nhap(SoNguyen)
print("Danh sách các số nguyên đã nhập: ", SoNguyen)
SoLe = MangLe(SoNguyen)
print("Danh sách các số lẻ: ", SoLe, "- Có tổng số lẻ là: ", len(SoLe))

SoChan = MangChan(SoNguyen)
print("Danh sách các số chẵn: ", SoChan, "- Có tổng số chẵn là: ", len(SoChan))

print("Danh sách các số nguyên tố: ", MangNguyenTo(SoNguyen))
print("Danh sách các số không phải nguyên tố: ", MangKhongNguyenTo(SoNguyen))