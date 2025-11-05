import math
def KiemTraSoNguyenTo(n):
    if n < 2:
        return False
    for i in range (2, n + 1, 1):
        if n%i==0:
            return False
    return True

s = input("Nhập một chuỗi: ")
arr = s.split(';')
sochan = 0
soam =0
sont =0 
sum=0
for x in arr:
    i = int(x)
    if i % 2 == 0:
        sochan = sochan + 1
    if i < 0:
        soam = soam + 1
    if KiemTraSoNguyenTo(i):
        sont = sont + 1
    sum = sum + i
print("Các chữ số trên dòng:", arr)
print("Tổng số chẵn:", sochan)
print("Tổng số âm:", soam)
print("Tống số nguyên tố:", sont)
print("Trung binh:", sum/len(arr))