from tkinter import *

root = Tk()

def TinhCong():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a+b))

def TinhTru():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a-b))

def TinhNhan():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a*b))

def TinhChia():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a/b))

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

root.title("Cộng trừ nhân chia")
root.minsize(height=150, width=260)
root.resizable(height=True, width=True)

lblTieuDe = Label(root, text="CỘNG TRỪ NHÂN CHIA", font=("Tohama", 16)).grid(row=0, columnspan=3)

frameButton=Frame()
btnCong = Button(frameButton, text="Cộng", width=10, command=TinhCong).pack(side=TOP, fill=X)
btnTru = Button(frameButton, text="Trừ", width=10, command=TinhTru).pack(side=TOP, fill=X)
btnNhan = Button(frameButton, text="Nhân", width=10, command=TinhNhan).pack(side=TOP, fill=X)
btnChia = Button(frameButton, text="Chia", width=10, command=TinhChia).pack(side=TOP, fill=X)
frameButton.grid(row=1, column=0, rowspan=4)

lblSoA = Label(root, text="sô a").grid(row=1, column=1)
lblSoB = Label(root, text="số b").grid(row=2, column=1)
lblKetQua = Label(root, text="kết quả").grid(row=3, column=1)

entSoA = Entry(root, textvariable = stringA, width=20).grid(row=1, column=2)
entSoB = Entry(root, textvariable=stringB, width=20).grid(row=2, column=2)
entKQ = Entry(root, textvariable=stringKQ, width=20).grid(row=3, column=2)

btnThoat = Button(root, text="Thoát", command = root.quit).grid(row=4, column=2)

root.mainloop()