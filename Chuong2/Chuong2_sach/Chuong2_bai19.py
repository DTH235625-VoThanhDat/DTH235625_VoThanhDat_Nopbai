def in_tong(n):
    print("Tổng 1 + ... + n =", sum(range(1, n+1)))

n = int(input("Nhập n: "))
in_tong(n)

def nguyen_to_cung_nhau(m, n):
    import math
    if math.gcd(m, n) == 1:
        print("Hai số này nguyên tố cùng nhau")
    else:
        print("Hai số này KHÔNG nguyên tố cùng nhau")

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
nguyen_to_cung_nhau(m, n)

def doi_giay(s):
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    print(f"{h} giờ {m} phút {s} giây")

s = int(input("Nhập số giây: "))
doi_giay(s)

def hieu_tuyet_doi(a, b):
    return abs(a - b)

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
print("|a - b| =", hieu_tuyet_doi(a, b))
