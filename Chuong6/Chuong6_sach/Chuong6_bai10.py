# Câu 10

def nhap_nguoi(filename="data72.txt"):
    ho = input("Nhập họ: ")
    ten = input("Nhập tên: ")
    tuoi = input("Nhập tuổi: ")

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{ho};{ten};{tuoi}\n")

    print("Đã lưu.")
