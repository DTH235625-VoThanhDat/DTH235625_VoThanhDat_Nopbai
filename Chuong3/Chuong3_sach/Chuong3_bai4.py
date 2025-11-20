s = input("Nhập chuỗi: ")

# Đảo ngược chuỗi
print("Chuỗi đảo ngược:", s[::-1])

# Đếm chữ cái, số
so_chu = sum(c.isalpha() for c in s)
so_so = sum(c.isdigit() for c in s)

print("Số chữ cái:", so_chu)
print("Số chữ số:", so_so)
