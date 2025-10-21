from random import randrange

# Khởi tạo danh sách rỗng
lst = []

# Nhập số phần tử
print("Nhập số phần tử:")
n = int(input())

# Sinh ngẫu nhiên n phần tử (0–99) và thêm vào list
for i in range(n):
    lst.append(randrange(0, 100))

print("List sau khi tạo ngẫu nhiên là:")
print(lst)

# Thêm 1 phần tử mới vào list
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:")
print(lst)

# Nhập giá trị cần xóa khỏi list
k = int(input("Mời nhập số để xóa: "))

# Xóa tất cả các phần tử có giá trị bằng k
while lst.count(k) > 0:
    lst.remove(k)

print("List sau khi xóa:")
print(lst)

# Hàm kiểm tra list có đối xứng không
def CheckDoiXung(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True

# Gọi hàm kiểm tra và in kết quả
kt = CheckDoiXung(lst)
if kt == True:
    print("List đối xứng")
else:
    print("List không đối xứng")
