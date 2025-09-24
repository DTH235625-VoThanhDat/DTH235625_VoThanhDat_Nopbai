import math

x = int(input("Nhập x: "))
n = int(input("Nhập n: "))

S = 0
for i in range(1, n+1, 1):
    S = S + x**(2*i+1) / math.factorial(2*i+i)

print("Kết quả là", S)