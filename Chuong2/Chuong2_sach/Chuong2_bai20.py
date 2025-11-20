def f(m, n):
    import math
    uc = math.gcd(m, n)     # ước chung lớn nhất
    if uc == 0:
        return 0
    return uc

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
print("f(m, n) =", f(m, n))
