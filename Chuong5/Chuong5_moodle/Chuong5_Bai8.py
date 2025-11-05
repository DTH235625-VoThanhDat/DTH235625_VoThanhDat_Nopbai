def LayBaiHatCoDuoi(s):
    s1 = s.rfind("\\")
    return s[s1+1:]

def LayTenBaiHat(s):
    s1 = LayBaiHatCoDuoi(s)
    s1 = s1.split('.')
    return s1[0]

s = input("Nhập vào đường link: ")
print("Bài hát có đuôi:", LayBaiHatCoDuoi(s))
print("Tên bài hát:", LayTenBaiHat(s))