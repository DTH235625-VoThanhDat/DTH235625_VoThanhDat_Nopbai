# a) Nhập doanh số
sales = []
for i in range(1, 11):
    value = float(input(f"Nhập doanh số cửa hàng {i}: "))
    sales.append(value)

# b) Sắp xếp tăng dần
sorted_sales = sorted(sales)
print("\nDoanh số sau khi sắp xếp tăng dần:", sorted_sales)

# c) Tính trung bình
average_sales = sum(sales) / len(sales)
print("Doanh số trung bình:", average_sales)

# d) Doanh số lớn nhất
max_sales = max(sales)
index_max = sales.index(max_sales) + 1
print("Doanh số lớn nhất:", max_sales)
print("Cửa hàng có doanh số cao nhất: cửa hàng số", index_max)
