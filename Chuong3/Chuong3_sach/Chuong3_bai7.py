s = input("Nhập chuỗi S: ")

def min_them(s):
    for i in range(len(s)):
        if s[i:] == s[i:][::-1]:
            return i
    return len(s)

kq = min_them(s)
print("Cần thêm", kq, "ký tự để chuỗi đối xứng.")
