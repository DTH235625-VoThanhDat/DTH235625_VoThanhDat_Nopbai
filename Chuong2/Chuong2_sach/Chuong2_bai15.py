# Nhập 3 số trên 1 dòng, cách nhau bởi dấu phẩy
a, b, c = map(float, input("Nhập 3 số dương a,b,c (cách nhau bởi dấu phẩy): ").split(","))

# Kiểm tra điều kiện tạo thành tam giác
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("Có thể tạo thành một tam giác")
else:
    print("Không thể tạo thành một tam giác")
