ngay = 0
thang =0
nam = 0
while True:
    ngay = int(input("Nhập vào ngày: "))
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ. Vui lòng nhập lại!")
    else:
        break

while True:
    thang = int(input("Nhập vào tháng: "))
    if (thang < 1 or thang > 12):
        print("Tháng không hợp lệ. Vui lòng nhập lại!")
    elif (ngay == 31 and thang in [4, 6, 9, 11]):
        print(f"Tháng {thang} không có 31 ngày. Vui lòng nhập lại!")
    elif (thang == 2 and ngay > 29):
        print("Tháng 2 không có quá 29 ngày. Vui lòng nhập lại!")
    else:
        break

while True:
    nam = int(input("Nhập vào năm: "))
    if(thang == 2 and ngay == 29):
        if (nam % 4 != 0 or (nam % 100 == 0 and nam % 400 != 0)):
            print(f"Năm {nam} không phải năm nhuần. Vui lòng nhập lại!")
        else:
            break
    else:
        break

print(f"Ngày tháng năm vừa nhập là: ({ngay}/{thang}/{nam})")

print("Ngày kế tiếp là: ", end="")
if (thang == 12 and ngay == 31):
    print(f"01/01/{nam + 1}")
elif (thang == 2 and ngay == 28) or (thang == 2 and ngay == 29):
    print(f"01/03/{nam}")
elif (ngay == 30 and thang in [4, 6, 9, 11]):
    print(f"01/{thang + 1}/{nam}")
elif (ngay == 31 and thang in [1, 3, 5, 7, 8, 10]):
    print(f"01/{thang + 1}/{nam}")
else:
    print(f"{ngay + 1}/{thang}/{nam}")