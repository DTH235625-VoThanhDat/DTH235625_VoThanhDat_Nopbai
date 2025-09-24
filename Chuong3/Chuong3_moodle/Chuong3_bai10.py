#Tính S(x,n) = x + x^2/2! + x^3/3! + ... + x^n/n!
def GiaiThua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * GiaiThua(n - 1)

def S(x, n):
    Sum = 0
    for i in range(1, n + 1, 1):
        Sum = Sum + (x**i /GiaiThua(i) )
    return Sum

x = int(input("Nhập số nguyên x: "))
n = int(input("Nhập số nguyên n: "))
print("Kết quả S(x,n) =", S(x, n)) 