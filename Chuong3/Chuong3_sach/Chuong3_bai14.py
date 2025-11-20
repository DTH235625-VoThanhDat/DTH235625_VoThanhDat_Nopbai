# Câu 14
s = input("Nhập họ tên: ")

# Xóa khoảng trắng thừa và chuẩn hóa
parts = s.strip().split()
parts = [p.capitalize() for p in parts]

result = " ".join(parts)
print("Chuẩn hóa:", result)
