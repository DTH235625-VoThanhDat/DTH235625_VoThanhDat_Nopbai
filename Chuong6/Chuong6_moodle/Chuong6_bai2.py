from random import randrange

def TaoMang(SoNguyen)->list:
    n = randrange(1, 100)
    for i in range(0, n, 1):
        SoNguyen.append(randrange(-100, 100))

def Xoak(SoNguyen, k):
    SoNguyen.remove(k)

def KiemTraDoiXung(SoNguyen):
    flag = True
    for i in range(len(SoNguyen)):
        if SoNguyen[i] != SoNguyen[len(SoNguyen) - i - 1]:
            flag = False
            break
    return flag


SoNguyen = []
TaoMang(SoNguyen)
print("Mảng ban đầu:", SoNguyen)
k = int(input("Nhập số k cần xóa: "))
if k in SoNguyen:
    Xoak(SoNguyen, k)
    print("Mảng sau khi xóa số k:", SoNguyen)
else:
    print("Số k không có trong mảng.")
if KiemTraDoiXung(SoNguyen):
    print("Mảng đối xứng")
else:
    print("Mảng không đối xứng")