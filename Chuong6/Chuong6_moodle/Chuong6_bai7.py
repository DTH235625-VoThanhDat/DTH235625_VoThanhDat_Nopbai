print("Chương trình nhập danh sách các số nguyên theo thứ tự không giảm.")
lst = []
print("Nhập số lượng các phần tử: ", end="")
n = int(input())

for i in range(n):
    print("Nhập phần tử thứ ", i + 1, ":", end="")
    so = int(input())
    lst.append(so)
    while True:
        if lst[i] < lst[i-1] and i > 0:
            print("Phần tử không hợp lệ, vui lòng nhập lại!")
            lst.remove(so)
            lst.append(int(input("Nhập phần tử thứ " + str(i + 1) + ": ")))
            so = lst[i]
        else: 
            break
print("Danh sách các phần tử đã nhập: ", lst)