class HinhChuNhat:
    def __init__(self, dai, rong, color="Không màu"):
        self.dai = dai
        self.rong = rong
        self.color = color

    def chu_vi(self):
        return 2 * (self.dai + self.rong)

    def dien_tich(self):
        return self.dai * self.rong

    def hien_thi(self):
        print("=== HÌNH CHỮ NHẬT ===")
        print("Dài:", self.dai)
        print("Rộng:", self.rong)
        print("Màu sắc:", self.color)
        print("Chu vi:", self.chu_vi())
        print("Diện tích:", self.dien_tich())


# ---- Test ----
hcn = HinhChuNhat(5, 3, "Xanh")
hcn.hien_thi()
