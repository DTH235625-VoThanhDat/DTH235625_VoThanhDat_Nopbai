thang = int(input("Nhập vào một tháng: "))
if thang in (1,2,3):
    print("Quý 1 trong năm")
elif thang in (4,5,6):
    print("Quý 2 trong năm")
elif thang in (7,8,9):
    print("Quý 3 trong năm")
elif thang in (10,11,12):
    print("Quý 4 trong năm")
else:
    print("Tháng không hợp lệ!")