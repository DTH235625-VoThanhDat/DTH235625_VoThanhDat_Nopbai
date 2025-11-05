print("Chương trình nhập danh sách các số thực")
ds_thuc = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ ", i + 1, ": ", end="")
    so = float(input())
    ds_thuc.append(so)

print("Danh sách các phần tử đã nhập: ", ds_thuc)
ds_thuc.sort(reverse=True)
print("Dánh sách sau khi sắp xếp giảm dần: ", ds_thuc)