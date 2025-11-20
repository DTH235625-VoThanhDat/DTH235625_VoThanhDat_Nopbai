# 7_tong_luy_thua.py
try:
    n = int(input("Nhập số nguyên n: "))
    result = n + n**2 + n**3
    print(f"{n} + {n}^2 + {n}^3 = {result}")
except Exception as e:
    print("Lỗi nhập:", e)
