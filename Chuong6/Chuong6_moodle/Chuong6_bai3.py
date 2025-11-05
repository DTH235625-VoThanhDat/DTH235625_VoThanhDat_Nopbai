def TaoMaTran(m,n)->list:
    MaTran = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Nhập phần tử MaTran[{i}][{j}]: ")))
        MaTran.append(row) 
    return MaTran

def InMaTran(MaTran):
    for row in MaTran:
        for val in row:
            print(val, end="\t")
        print()

def XuatDong(MaTran, dong):
    for val in MaTran[dong]:
        print(val, end="\t")
    print()

def XuatCot(MaTran, cot):
    for row in MaTran:
        print(row[cot], end="\n")
    print()


m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))
MaTran = TaoMaTran(m, n)
print("Ma trận vừa tạo là:")
InMaTran(MaTran)


dong = int(input("Nhập dòng cần xuất: "))
print(f"Dòng {dong} của ma trận là:")
XuatDong(MaTran, dong)

cot = int(input("Nhập cột cần xuất: "))
print(f"Cột {cot} của ma trận là:")
XuatCot(MaTran, cot)

print("Số max trong ma trận là:", max(max(row) for row in MaTran))