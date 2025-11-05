def XuLyChuoi(s):
    s1 = s.title()
    s2 = s1
    s2 = s2.strip()
    arr = s2.split()
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s2 = s2 + word + " "
    return s2.strip()

s = input("Nhập vào một chuỗi: ")
print("Chuỗi sau khi xử lý:", XuLyChuoi(s))