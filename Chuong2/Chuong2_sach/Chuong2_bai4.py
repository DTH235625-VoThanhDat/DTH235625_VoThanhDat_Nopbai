# 4_ngay_trong_thang.py
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

try:
    thang = int(input("Nhập số tháng (1-12): "))
    if thang < 1 or thang > 12:
        print("Tháng không hợp lệ")
    elif thang == 2:
        nam = int(input("Nhập năm: "))
        print("Số ngày:", 29 if is_leap(nam) else 28)
    elif thang in (1,3,5,7,8,10,12):
        print("Số ngày: 31")
    else:
        print("Số ngày: 30")
except Exception as e:
    print("Lỗi nhập:", e)
