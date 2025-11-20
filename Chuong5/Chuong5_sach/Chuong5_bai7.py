class SoHoc:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

    def inputInfo(self):
        self.number1 = float(input("Nhập số thứ nhất: "))
        self.number2 = float(input("Nhập số thứ hai: "))

    def printInfo(self):
        print("Number1:", self.number1)
        print("Number2:", self.number2)

    def addition(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multi(self):
        return self.number1 * self.number2

    def division(self):
        if self.number2 == 0:
            return "Không thể chia cho 0"
        return self.number1 / self.number2


# ---- TEST ----
s = SoHoc(10, 5)
print("Tổng:", s.addition())
print("Hiệu:", s.subtract())
print("Nhân:", s.multi())
print("Chia:", s.division())
