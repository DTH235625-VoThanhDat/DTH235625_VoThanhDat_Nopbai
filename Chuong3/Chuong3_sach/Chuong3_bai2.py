s = input("Nhập chuỗi: ")
i = int(input("Nhập vị trí i: "))
j = int(input("Nhập vị trí j: "))

print("Chiều dài chuỗi:", len(s))
print("Ký tự đầu:", s[0])
print("Ký tự cuối:", s[-1])

if 0 <= i < len(s):
    print("Ký tự tại vị trí i:", s[i])
else:
    print("Vị trí i không hợp lệ")

if 0 <= j < len(s):
    print("Ký tự tại vị trí j:", s[j])
else:
    print("Vị trí j không hợp lệ")
