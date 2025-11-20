def nhap_sbd():
    while True:
        sbd = input("Nhập số báo danh (5 ký số): ")
        if sbd.isdigit() and len(sbd) == 5:
            return sbd
        print("❌ SBD không hợp lệ! Hãy nhập lại.")

def nhap_hoten():
    while True:
        hoten = input("Nhập họ và tên (≤ 25 ký tự): ")
        if len(hoten) <= 25:
            return hoten
        print("❌ Tên quá dài!")

def nhap_diem_toan():
    while True:
        try:
            diem = float(input("Nhập điểm Toán (0–10): "))
            if 0 <= diem <= 10:
                return diem
        except ValueError:
            print("❌ Vui lòng nhập số!")
        print("❌ Điểm không hợp lệ!")

def nhap_diem_tv():
    while True:
        try:
            diem = float(input("Nhập điểm Tiếng Việt (0–10): "))
            if 0 <= diem <= 10:
                return diem
        except ValueError:
            print("❌ Vui lòng nhập số!")
        print("❌ Điểm không hợp lệ!")

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng thí sinh: "))
    for i in range(n):
        print(f"\n--- Thí sinh {i+1} ---")
        sbd = nhap_sbd()
        hoten = nhap_hoten()
        toan = nhap_diem_toan()
        tv = nhap_diem_tv()
        ds.append({
            "sbd": sbd,
            "hoten": hoten,
            "toan": toan,
            "tv": tv,
            "tong": toan + tv
        })
    return ds

def hien_thi(ds):
    print("\n=== DANH SÁCH THÍ SINH ===")
    for ts in ds:
        print(ts)

def tong_lon_hon_10(ds):
    print("\n=== THÍ SINH CÓ TỔNG ĐIỂM > 10 ===")
    for ts in ds:
        if ts["tong"] > 10:
            print(ts)

def diem_liet(ds):
    print("\n=== THÍ SINH CÓ ĐIỂM LIỆT (>= 1 điểm bằng 0) ===")
    for ts in ds:
        if ts["toan"] == 0 or ts["tv"] == 0:
            print(ts)

# Chương trình chính
ds = nhap_danh_sach()
hien_thi(ds)
tong_lon_hon_10(ds)
diem_liet(ds)
