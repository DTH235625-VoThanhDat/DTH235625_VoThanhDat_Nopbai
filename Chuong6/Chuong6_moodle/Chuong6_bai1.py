from random import randrange

print("CHƯƠNG TRÌNH XỬ LÝ LIST")

# --- Khởi tạo list ---
n = int(input("Nhập số phần tử: "))
lst = []

for i in range(n):
    lst.append(randrange(-100, 100))

print("List ngẫu nhiên là:")
print(lst)

# --- Thêm phần tử vào list ---
value = int(input("Mời bạn thêm số mới: "))
lst.append(value)
print("List sau khi thêm phần tử:")
print(lst)

# --- Đếm số lần xuất hiện của k ---
k = int(input("Bạn muốn đếm số nào: "))
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

# --- Hàm kiểm tra số nguyên tố ---
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- Tính tổng và đếm số nguyên tố ---
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng các số nguyên tố là:", tongnt)

# --- Sắp xếp list ---
lst.sort()
print("List sau khi sắp xếp:")
print(lst)

# --- Xóa list ---
del lst
print("List sau khi xóa:")
try:
    print(lst)
except:
    print("List đã bị xóa!")