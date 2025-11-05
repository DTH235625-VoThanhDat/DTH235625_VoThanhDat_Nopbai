def NhapMaTran()->list:
    m = int(input("Nhập số hàng của ma trận: "))
    n = int(input("Nhập số cột của ma trận: "))
    MaTran = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Nhập phần tử MaTran[{i}][{j}]: ")))
        MaTran.append(row)
    return MaTran

def XuatMaTran(MaTran):
    for row in MaTran:
        for val in row:
            print(val, end="\t")
        print()

def CongMaTran(MaTranA, MaTranB)->list:
    if len(MaTranA) != len(MaTranB) or len(MaTranA[0]) != len(MaTranB[0]):
        return None
    m = len(MaTranA)
    n = len(MaTranA[0])
    MaTranCong = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(MaTranA[i][j] + MaTranB[i][j])
        MaTranCong.append(row)
    return MaTranCong

def MaTranHoanVi(MaTran):
    m = len(MaTran)
    n = len(MaTran[0])
    MaTranHV = [[MaTran[j][i] for j in range(m)] for i in range(n)]
    return MaTranHV

print("Nhập ma trận A:")
MaTranA = NhapMaTran()
print("Ma trận A vừa tạo là:")
XuatMaTran(MaTranA)

print("Nhập ma trận B:")
MaTranB = NhapMaTran()
print("Ma trận B vừa tạo là:")
XuatMaTran(MaTranB)

MaTranCong = CongMaTran(MaTranA, MaTranB)
if MaTranCong:
    print("Ma trận A + B là:")
    XuatMaTran(MaTranCong)
else:
    print("Không thể cộng hai ma trận vì kích thước không khớp.")

MaTranHV = MaTranHoanVi(MaTranA)
print("Ma trận A sau khi hoán vị là:")
XuatMaTran(MaTranHV)

print("Ma trận B sau khi hoán vị là:")
MaTranHV_B = MaTranHoanVi(MaTranB)
XuatMaTran(MaTranHV_B)