# Câu 15a

def nhap_ho_gd():
    phong = input("Số phòng: ")
    toa = input("Tòa nhà: ")
    ten = input("Tên chủ hộ: ")
    kw = int(input("Số kW tiêu thụ: "))
    return phong, toa, ten, kw

# Câu 15b

def tinh_tien_dien(kw):
    if kw <= 100:
        tien = kw * 1450
    elif kw <= 150:
        tien = 100*1450 + (kw-100)*1750
    elif kw <= 250:
        tien = 100*1450 + 50*1750 + (kw-150)*2000
    else:
        tien = 100*1450 + 50*1750 + 100*2000 + (kw-250)*2500
    
    return tien * 1.1    # VAT 10%

# Câu 15c

def hien_thi(ds):
    print("Tòa nhà | Phòng | Số kW | Tiền phải trả")
    for ho in ds:
        phong, toa, ten, kw = ho
        print(toa, phong, kw, tinh_tien_dien(kw))

# Câu 15d

def luu_theo_toa(ds):
    dict_toa = {}

    for ho in ds:
        phong, toa, ten, kw = ho
        if toa not in dict_toa:
            dict_toa[toa] = []
        dict_toa[toa].append(ho)

    for toa, items in dict_toa.items():
        with open(f"{toa}.txt", "w", encoding="utf-8") as f:
            for ho in items:
                f.write(";".join(map(str, ho)) + "\n")
