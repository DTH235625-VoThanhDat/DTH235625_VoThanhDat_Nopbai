import math

class Diem:
    def __init__(self, x=0, y=0, color="Không màu"):
        self.x = x
        self.y = y
        self.color = color

    def hienThi(self):
        print(f"Điểm({self.x}, {self.y}), màu: {self.color}")

    def tinhTien_x(self, x):
        self.x += x

    def tinhTien_xy(self, x, y):
        self.x += x
        self.y += y

    def khoangCach(self):
        return math.sqrt(self.x**2 + self.y**2)


# ---- TEST ----
d = Diem(3, 4, "Đỏ")
d.hienThi()
d.tinhTien_x(2)
d.hienThi()
print("Khoảng cách đến O:", d.khoangCach())
