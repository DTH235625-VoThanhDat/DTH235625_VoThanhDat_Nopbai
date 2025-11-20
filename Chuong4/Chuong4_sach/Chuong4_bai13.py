def polynomial_value(coeffs, x):
    total = 0
    for i, a in enumerate(coeffs):
        total += a * (x ** i)
    return total

# Nhập dữ liệu
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))

coeffs = []
for i in range(n + 1):
    a = float(input(f"Nhập a{i}: "))
    coeffs.append(a)

Pn = polynomial_value(coeffs, x)
print("Giá trị đa thức Pn =", Pn)
