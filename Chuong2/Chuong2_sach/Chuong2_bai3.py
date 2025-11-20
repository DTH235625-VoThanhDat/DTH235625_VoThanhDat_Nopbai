# 3_dientich_tron.py
import math
try:
    r = float(input("Nhập bán kính r: "))
    if r < 0:
        print("Bán kính phải >= 0")
    else:
        area = math.pi * r * r
        print(f"Diện tích hình tròn: {area:.4f}")
except Exception as e:
    print("Lỗi nhập:", e)
