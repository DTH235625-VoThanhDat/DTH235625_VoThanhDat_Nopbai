# Câu 16: Kiểm tra ngày tháng năm hợp lệ

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

# Số ngày trong từng tháng
days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

# Kiểm tra năm nhuận
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    days_in_month[2] = 29

if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:
    print("Ngày tháng năm hợp lệ")
else:
    print("Ngày tháng năm không hợp lệ")
