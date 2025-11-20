import math

class HinhTron:
    def __init__(self, r, color="Không màu"):
        self.r = r
        self.color = color

    def chu_vi(self):
        return 2 * math.pi * self.r

    def dien_tich(self):
        return math.pi * self.r * self.r

    def hien_thi(self):
        print("=== HÌNH TRÒN ===")
        print("Bán kính:", self.r)
        print("Màu sắc:", self.color)
        print("Chu vi:", round(self.chu_vi(), 3))
        print("Diện tích:", round(self.dien_tich(), 3))


# ---- Test ----
ht = HinhTron(4, "Vàng")
ht.hien_thi()
