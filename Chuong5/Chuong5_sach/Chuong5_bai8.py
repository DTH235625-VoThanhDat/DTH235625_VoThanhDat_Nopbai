class NhanVien:
    def __init__(self, name="", age=0, address="", salary=0, hours=0):
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
        self.hours = hours

    def inputInfo(self):
        self.name = input("Tên: ")
        self.age = int(input("Tuổi: "))
        self.address = input("Địa chỉ: ")
        self.salary = float(input("Tiền lương: "))
        self.hours = float(input("Số giờ làm: "))

    def printInfo(self):
        print("\n=== THÔNG TIN NHÂN VIÊN ===")
        print("Tên:", self.name)
        print("Tuổi:", self.age)
        print("Địa chỉ:", self.address)
        print("Lương:", self.salary)
        print("Giờ làm:", self.hours)

    def tinhThuong(self):
        if self.hours >= 200:
            return self.salary * 0.2
        elif self.hours >= 100:
            return self.salary * 0.1
        else:
            return 0


# ---- TEST ----
nv = NhanVien("An", 25, "HCM", 3000000, 210)
nv.printInfo()
print("Thưởng:", nv.tinhThuong())
