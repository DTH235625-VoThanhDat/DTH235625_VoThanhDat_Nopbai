class DaGiac:
    def __init__(self, so_canh, ds_canh):
        self.so_canh = so_canh
        self.ds_canh = ds_canh

    def chu_vi(self):
        return sum(self.ds_canh)


class HinhBinhHanh(DaGiac):
    def __init__(self, a, b, h):
        super().__init__(4, [a, b, a, b])
        self.a = a
        self.b = b
        self.h = h

    def dien_tich(self):
        return self.a * self.h


class HinhChuNhat2(HinhBinhHanh):   # kế thừa từ hình bình hành
    def __init__(self, dai, rong):
        super().__init__(dai, rong, h=rong)
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        return self.dai * self.rong


class HinhVuong(HinhChuNhat2):      # kế thừa từ hình chữ nhật
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh


# ---- Test ----
print("=== HÌNH BÌNH HÀNH ===")
hb = HinhBinhHanh(5, 3, 4)
print("Chu vi:", hb.chu_vi())
print("Diện tích:", hb.dien_tich())

print("\n=== HÌNH CHỮ NHẬT ===")
hcn = HinhChuNhat2(6, 4)
print("Chu vi:", hcn.chu_vi())
print("Diện tích:", hcn.dien_tich())

print("\n=== HÌNH VUÔNG ===")
hv = HinhVuong(5)
print("Chu vi:", hv.chu_vi())
print("Diện tích:", hv.dien_tich())
