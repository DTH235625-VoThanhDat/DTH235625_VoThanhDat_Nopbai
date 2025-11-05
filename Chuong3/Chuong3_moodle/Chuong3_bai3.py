import math
def TinhPhuongTrinhBacHai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm!")
            else:
                print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x =", -c/b)
    else:
        delta = b*b - 4 * a * c 
        if delta < 0:
            print("Phương trình vô nghiệm!")
        elif delta == 0:
            print("Phương trình có nghiệm kép: x1 = x2 =", -b/(2*a))
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Phương trình có hai nghiệm phân biệt: x1 =", x1," x2 =", x2)

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
print("Kết quả chương tình:")
TinhPhuongTrinhBacHai(a, b, c)