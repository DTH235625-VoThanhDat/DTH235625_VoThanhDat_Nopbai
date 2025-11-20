s1 = input("Nhập chuỗi 1: ")
s2 = input("Nhập chuỗi 2: ")

# Tập ký tự chung
chung = set(s1) & set(s2)

print("Các ký tự xuất hiện ở cả hai chuỗi:", "".join(chung))
