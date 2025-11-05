print("Chương trình nhập danh sách các số nguyên không trùng nhau.")
lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ ", i +1, ": ", end="")
    so = int(input())
    lst.append(so)
    while True:
        if lst[i] in lst[0:i]:
            print("Phần tử đã tồn tại, vui lòng nhập lại!")
            lst.remove(so)
            lst.append(int(input("Nhập phần tử thứ " + str(i + 1) + ": ")))
        else:
            break
print("Danh sách các phần tử đã nhập: ", lst)
    