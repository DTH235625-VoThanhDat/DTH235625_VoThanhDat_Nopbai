# Câu 11
s = input("Nhập chuỗi số (phân tách bằng ;): ")

lst = [int(x) for x in s.split(";")]

print("Các số trên từng dòng:")
for x in lst:
    print(x)

print("Có bao nhiêu chữ số chẵn:", sum(1 for x in lst if x % 2 == 0))
print("Có bao nhiêu số âm:", sum(1 for x in lst if x < 0))

# Kiểm tra số nguyên tố
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print("Có bao nhiêu số nguyên tố:", sum(1 for x in lst if is_prime(x)))
print("Giá trị trung bình:", sum(lst) / len(lst))
