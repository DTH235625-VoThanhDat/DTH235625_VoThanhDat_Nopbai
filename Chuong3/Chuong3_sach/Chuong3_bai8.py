s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")

pos = s1.find(s2)

if pos != -1:
    print("s2 xuất hiện lần đầu tại vị trí:", pos)
else:
    print("Không tìm thấy s2 trong s1")
