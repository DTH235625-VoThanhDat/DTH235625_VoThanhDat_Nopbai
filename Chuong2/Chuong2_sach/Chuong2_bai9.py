# Cau_9.py
n = int(input("Nhập n (n > 0): "))

S  = sum(range(1, n+1))
S1 = sum(2*i - 1 for i in range(1, n+1))       # 1 + 3 + ... + (2n-1)
S2 = sum(2*i     for i in range(1, n+1))       # 2 + 4 + ... + 2n
S3 = sum(i*i     for i in range(1, n+1))       # 1^2 + 2^2 + ... + n^2
S4 = sum(1/i     for i in range(1, n+1))       # 1 + 1/2 + ... + 1/n

print("S  =", S)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
