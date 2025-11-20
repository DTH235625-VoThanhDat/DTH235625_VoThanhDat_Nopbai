# 8_bang_cuu_chuong.py
try:
    n = int(input("Nhập n (1..9): "))
    if not (1 <= n <= 9):
        print("n ngoài phạm vi 1..9")
    else:
        for i in range(1, 11):
            print(f"{n} x {i} = {n*i}")
except Exception as e:
    print("Lỗi nhập:", e)
