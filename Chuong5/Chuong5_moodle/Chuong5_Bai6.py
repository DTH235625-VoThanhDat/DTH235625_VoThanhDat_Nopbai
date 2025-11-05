import re

def NagativeNumberInString(s:str):
    numbers = re.findall(r'-\d+', s)
    return [int(num) for num in numbers]

s = input("Nhập chuỗi: ")
kq = NagativeNumberInString(s)
print("Các số nguyên âm trong chuỗi:", kq) 