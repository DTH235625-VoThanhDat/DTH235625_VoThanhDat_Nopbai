# Nhập chuỗi từ bàn phím
s = input("Nhập câu: ")

# Tách chuỗi theo khoảng trắng hoặc tab, rồi viết hoa chữ cái đầu
words = s.split()  # split() tự tách theo space hoặc tab

# Viết hoa ký tự đầu mỗi từ
result = " ".join(word.capitalize() for word in words)

# In kết quả
print("Kết quả:", result)
