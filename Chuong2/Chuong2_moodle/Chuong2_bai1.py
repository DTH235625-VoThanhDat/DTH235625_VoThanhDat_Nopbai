#Tính chu vi và diện tích hình tròn
import math
try:
    r  = float(input("Nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    dt = math.pi * r * r
    print("Chu vi hình tròn là: ", cv)
    print("Diện tích hình tròn là: ", dt)
except:
    print("Lỗi rồi!")