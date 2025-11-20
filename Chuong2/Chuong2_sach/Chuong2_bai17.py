# Câu 17a: Tính 1 + 2 + ... + 2n
n = int(input("Nhập n: "))
tong_2n = sum(range(1, 2*n + 1))
print("Tổng 1 + ... + 2n =", tong_2n)

# Câu 17b: Tổng số lẻ < n
tong_le = sum(i for i in range(n) if i % 2 == 1)
print("Tổng số tự nhiên < n và là số lẻ:", tong_le)

# Câu 17c: Tổng số chẵn < n
tong_chan = sum(i for i in range(n) if i % 2 == 0)
print("Tổng số tự nhiên < n và là số chẵn:", tong_chan)
