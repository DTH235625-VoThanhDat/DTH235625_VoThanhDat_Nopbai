from tkinter import *
import math 

root = Tk()
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

def GiaiTiep():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

def GiaiPT():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())
    if(a==0):
        if(b==0):
            if(c==0):
                stringKQ.set("Vô số nghiệm")
            else:
                stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set("x="+str((-c/b)))
    else:
        delta = b**2 - 4*a*c
        if(delta < 0):
            stringKQ.set("Vô nghiệm")
        elif(delta == 0):
            stringKQ.set("Nghiệm kép"+str((-b/2*a)))
        else:
            x1 = (-b - math.sqrt(delta))/ (2*a)
            x2 = (-b + math.sqrt(delta)) /(2*a)
            stringKQ.set("x1="+str(x1) + ", x2="+str(x2))

root.title("PTB2")
root.minsize(height=150, width=250)
root.resizable(height=True, width=250)

lblTieuDe = Label(root, text="Phương Trình Bậc 2", fg = "blue", font=("Tohama", 16), justify = CENTER).grid(row=0, columnspan=2)

lblHeSoA = Label(root, text="Hệ số a").grid(row=1, column=0)
lblHeSoB = Label(root, text="Hệ số b").grid(row=2, column=0)
lblHeSoC = Label(root, text="Hệ số c").grid(row=3, column=0)

entHeSoA = Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)
entHeSoB = Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)
entHeSoC = Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame()
btnGiai = Button(frameButton, text="Giải", command=GiaiPT).pack(side=LEFT)
btnThiep=Button(frameButton, text="Tiếp", command=GiaiTiep).pack(side=LEFT)
btnThoat=Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=4, columnspan=2)

lblKetQua = Label(root, text = "Kết quả").grid(row=5, column=0)
entKQ = Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()