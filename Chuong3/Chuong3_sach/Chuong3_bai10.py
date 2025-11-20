s = input("Nhập email: ")

# Email hợp lệ nếu chứa đúng 1 '@' và có dạng x@y.z
if s.count("@") == 1 and "." in s.split("@")[1]:
    x, temp = s.split("@")
    y, *z = temp.split(".")
    if x != "" and y != "" and all(part != "" for part in z):
        print("Email hợp lệ")
    else:
        print("Email không hợp lệ")
else:
    print("Email không hợp lệ")
