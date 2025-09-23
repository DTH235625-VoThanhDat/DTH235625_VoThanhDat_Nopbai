# Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím.
# input() luôn trả về kiểu str, cần ép kiểu nếu cần số.
name = input("Nhập tên: ")
age = int(input("Nhập tuổi: "))
score = float(input("Nhập điểm: "))
print("Tên:", name, "- Tuổi:", age, "- Điểm:", score)