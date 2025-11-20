# 5_doc_hai_chu_so.py
digits = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]

def read_two_digits(n):
    if n < 0 or n > 99:
        return "Ngoài phạm vi (0..99)"
    if n < 10:
        return digits[n].capitalize()
    tens = n // 10
    ones = n % 10
    if tens == 1:
        tens_part = "Mười"
    else:
        tens_part = digits[tens].capitalize() + " mươi"
    if ones == 0:
        return tens_part
    # xử lý các cách đọc thông dụng cho 1 và 5 ở hàng đơn vị
    if ones == 1:
        ones_part = "mốt" if tens >= 2 else "một"
    elif ones == 5:
        ones_part = "lăm" if tens >= 1 else "năm"
    else:
        ones_part = digits[ones]
    return f"{tens_part} {ones_part}"

try:
    n = int(input("Nhập số n (0..99): "))
    print(read_two_digits(n))
except Exception as e:
    print("Lỗi nhập:", e)
