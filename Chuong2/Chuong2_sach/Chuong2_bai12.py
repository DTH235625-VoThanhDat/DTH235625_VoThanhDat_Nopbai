# Cau_12.py
n = int(input("Nhập số nguyên thập phân: "))

if n == 0:
    print("0")
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
    print("Số nhị phân là:", binary)
