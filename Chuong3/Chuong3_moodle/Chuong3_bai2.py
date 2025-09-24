#Đếm số ngày trong tháng
thang = 0
while True:
    thang = int(input("Nhập vào một tháng: "))
    if thang < 1 or thang > 12:
        print("Tháng không hợp lệ. Vui lòng nhập lại!")
    else:
        break
if thang in [1, 3, 5, 7, 8, 10, 12]:
    print(f"thang {thang} có 31 ngày")
elif thang in (4, 6, 9, 12):
    print(f"tháng {thang} có 30 ngày")
else:
    nam = int(input("Nhập vào năm: "))
    if(nam  % 4 == 0 and nam %100 != 0) or nam % 400 == 0:
        print("Tháng", thang, "có 29 ngày")
    else:
        print("Tháng", thang,"có 28 ngày")