class MonHoc:
    def __init__(self, ma, ten, tc):
        self.ma = ma
        self.ten = ten
        self.tc = tc

    def hienThi(self):
        print(f"{self.ma} - {self.ten} - {self.tc} tín chỉ")


class QuanLyMonHoc:
    def __init__(self):
        self.ds = []

    def themMon(self, mon):
        self.ds.append(mon)

    def xoaMon(self, ma_xoa):
        self.ds = [m for m in self.ds if m.ma != ma_xoa]

    def hienThi(self):
        print("\n=== DANH SÁCH MÔN HỌC ===")
        for m in self.ds:
            m.hienThi()

    def timKiem(self, keyword):
        return [m for m in self.ds if keyword.lower() in m.ten.lower() 
                                   or keyword.lower() in m.ma.lower()]

    def ghiFile(self, file="monhoc.txt"):
        with open(file, "w", encoding="utf-8") as f:
            for m in self.ds:
                f.write(f"{m.ma},{m.ten},{m.tc}\n")

    def docFile(self, file="monhoc.txt"):
        self.ds = []
        with open(file, "r", encoding="utf-8") as f:
            for line in f:
                ma, ten, tc = line.strip().split(",")
                self.ds.append(MonHoc(ma, ten, int(tc)))


# ---- TEST ----
ql = QuanLyMonHoc()
ql.themMon(MonHoc("IT01", "Lập trình Python", 3))
ql.themMon(MonHoc("IT02", "Cấu trúc dữ liệu", 4))
ql.hienThi()

ql.ghiFile()
ql.docFile()
print("\nSau khi đọc file:")
ql.hienThi()
