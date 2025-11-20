# Cau_13.py
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("a phải khác 0!")
else:
    D = b*b - 4*a*c

    if D < 0:
        print("Phương trình vô nghiệm")
    elif D == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
