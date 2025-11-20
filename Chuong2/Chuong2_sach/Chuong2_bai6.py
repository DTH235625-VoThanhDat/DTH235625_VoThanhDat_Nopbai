# 6_giai_pt_bac2.py
import math
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    if a == 0:
        if b == 0:
            print("Vô số nghiệm" if c == 0 else "Vô nghiệm")
        else:
            x = -c / b
            print("Phương trình bậc nhất, nghiệm x =", x)
    else:
        D = b*b - 4*a*c
        if D < 0:
            print("Vô nghiệm thực")
        elif D == 0:
            x = -b / (2*a)
            print("Nghiệm kép x =", x)
        else:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print("x1 =", x1)
            print("x2 =", x2)
except Exception as e:
    print("Lỗi nhập:", e)
