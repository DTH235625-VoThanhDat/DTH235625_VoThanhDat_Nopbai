n = int(input("Nhập n: "))

# Câu a: số các ước số nguyên tố khác nhau của n
def is_prime(x):
    if x < 2: 
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

uoc_nt_khac = 0
for i in range(1, n+1):
    if n % i == 0 and is_prime(i):
        uoc_nt_khac += 1

print("Số lượng ước số nguyên tố khác nhau của n:", uoc_nt_khac)

# Câu b: các ước số thực sự của n (không tính n)
uoc_thuc = [i for i in range(1, n) if n % i == 0]
print("Các ước số thực sự của n:", uoc_thuc)

# Câu c: tính 12 + 22 + 32 + ... + n2
tong_binh_phuong = sum(i*i for i in range(1, n+1))
print("Tổng 1^2 + 2^2 + ... + n^2 =", tong_binh_phuong)
