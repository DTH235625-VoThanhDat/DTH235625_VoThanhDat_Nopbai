# Câu 14a

def nhap_sv():
    ma = input("Mã SV: ")
    ten = input("Tên: ")
    lop = input("Lớp: ")
    que = input("Quê quán: ")
    return f"{ma};{ten};{lop};{que}"

# Câu 14b

def luu_sv(filename="svchung.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(nhap_sv() + "\n")

