class ToanHoc:
    def __init__(self, *so):
        self.ds = list(so)

    def tinhTong(self):
        return sum(self.ds)

    def tinhTrungBinh(self):
        return sum(self.ds) / len(self.ds)

    def tinhMax(self):
        return max(self.ds)

    def tinhMin(self):
        return min(self.ds)

    def hienThi(self):
        print("Danh sách số:", self.ds)
        print("Tổng:", self.tinhTong())
        print("Trung bình:", self.tinhTrungBinh())
        print("Lớn nhất:", self.tinhMax())
        print("Nhỏ nhất:", self.tinhMin())


# ---- TEST ----
t = ToanHoc(1, 5, 7, 9, 3)
t.hienThi()
