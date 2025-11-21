# Câu 11

def nhap_san_pham(filename="sanpham.txt"):
    ma = input("Mã SP: ")
    ten = input("Tên SP: ")
    gia = float(input("Đơn giá: "))

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"{ma};{ten};{gia}\n")

    print("Đã lưu sản phẩm!")

def xuat_san_pham(filename="sanpham.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())

def sap_xep_giam(filename="sanpham.txt"):
    with open(filename, 'r', encoding='utf-8') as f:
        items = []
        for line in f:
            ma, ten, gia = line.strip().split(";")
            items.append((ma, ten, float(gia)))

    items.sort(key=lambda x: x[2], reverse=True)

    for sp in items:
        print(sp)

