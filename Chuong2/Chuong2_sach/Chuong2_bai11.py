# Cau_11.py
import math

x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(1, n+1):
    S += x**i / math.factorial(i)

print("S(x,n) =", S)
