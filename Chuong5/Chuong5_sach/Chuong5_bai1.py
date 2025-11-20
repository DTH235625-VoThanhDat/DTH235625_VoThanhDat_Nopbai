import math

class TamGiac:
    def __init__(self, a, b, c, color="Không màu"):
        self.a = a
        self.b = b
        self.c = c
        self.color = color

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def loai_tam_giac(self):
        a, b, c = self.a, self.b, self.c
        if a == b == c:
            return "Tam giác đều"
        if a == b or b == c or a == c:
            if self._la_vuong():
                return "Tam giác vuông cân"
            return "Tam giác cân"
        if self._la_vuong():
            return "Tam giác vuông"
        return "Tam giác thường"

    def _la_vuong(self):
        a, b, c = sorted([self.a, self.b, self.c])
        return abs(a*a + b*b - c*c) < 1e-6

    def hien_thi(self):
        print("=== THÔNG TIN TAM GIÁC ===")
        print("Cạnh:", self.a, self.b, self.c)
        print("Màu sắc:", self.color)
        print("Chu vi:", self.chu_vi())
        print("Diện tích:", round(self.dien_tich(), 3))
        print("Loại:", self.loai_tam_giac())


# ---- Test ----
tg = TamGiac(3, 4, 5, "Đỏ")
tg.hien_thi()
