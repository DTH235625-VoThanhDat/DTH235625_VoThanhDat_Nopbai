from random import randrange

# Hàm tạo ma trận ngẫu nhiên MxN
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

# Hàm xuất ma trận
def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# Hàm lấy dòng thứ r
def LayDong(r):
    R = D[r]
    return R

# Hàm xuất 1 danh sách trên 1 dòng
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# Hàm lấy cột thứ c
def LayCot(c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

# Hàm tìm số lớn nhất trong ma trận
def MAX(D):
    max_val = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if max_val < D[i][j]:
                max_val = D[i][j]
    return max_val


# ==============================
# CHƯƠNG TRÌNH CHÍNH
# ==============================

print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

# Tạo và xuất ma trận
D = TaoMaTran(m, n)
print("Ma trận ngẫu nhiên là:")
XuatMaTran(D)

# Xuất dòng theo yêu cầu
print("Mời bạn nhập dòng muốn xuất:")
r = int(input())
XuatList1Chieu(LayDong(r))

# Xuất cột theo yêu cầu
print("Mời bạn nhập cột muốn xuất:")
c = int(input())
XuatList1Chieu(LayCot(c))

# Xuất số lớn nhất trong ma trận
max_val = MAX(D)
print("Số lớn nhất trong ma trận =", max_val)
