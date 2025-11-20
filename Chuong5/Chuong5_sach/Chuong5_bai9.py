class Student:
    def __init__(self, ma="", name="", dtb=0, lop=""):
        self.ma = ma
        self.name = name
        self.dtb = dtb
        self.lop = lop

    def inputInfo(self):
        self.ma = input("Mã sinh viên: ")
        self.name = input("Tên sinh viên: ")
        self.dtb = float(input("Điểm trung bình: "))
        self.lop = input("Lớp: ")

    def showInfo(self):
        print("\n=== THÔNG TIN SINH VIÊN ===")
        print("Mã:", self.ma)
        print("Tên:", self.name)
        print("Điểm TB:", self.dtb)
        print("Lớp:", self.lop)

    def hocBong(self):
        return self.dtb >= 8.0


# ---- TEST ----
sv = Student("SV01", "Đạt", 8.5, "12A1")
sv.showInfo()
print("Có học bổng:", sv.hocBong())
