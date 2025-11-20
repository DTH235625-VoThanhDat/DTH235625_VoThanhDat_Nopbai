s = input("Nhập CCCD: ")

if s.isdigit() and len(s) in (12, 15):
    print("CCCD hợp lệ")
else:
    print("CCCD không hợp lệ")
