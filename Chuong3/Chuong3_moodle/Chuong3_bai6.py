n = 0
while True:
    n = int(input("Nhập số nguyên n có tối đa 2 chữ số: "))
    if n < 0 or n > 99:
        print("Nhập sai! Nhập lại")
    else:
        break
so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["","mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "súa mươi", "bảy mươi", "tám mươi", "chín mươi"]
if n < 10:
    print(so[n])
else:
    donvi = n % 10
    hangchuc = n // 10
    if donvi == 1:
        print(chuc[hangchuc], "mốt")
    elif donvi == 5:
        print(chuc[hangchuc], "lăm")
    elif donvi == 0:
        print(chuc[hangchuc])
    else:
        print(chuc[hangchuc], so[donvi])