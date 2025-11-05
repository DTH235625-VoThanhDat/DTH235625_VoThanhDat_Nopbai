from tkinter import *

root = Tk()

def GiaiTiep():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def GiaiPhuongTrinh():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    if a == 0 and b==0:
        stringKQ.set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x="+str((-b/a)))

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

root.title("PTB1")
root.minsize(height = 130, width = 250)
root.resizable(height = True, width = True)
lblTieuDe = Label(root, text = "Phương trinh bậc nhất", fg="red", font=("Tohama", 16), justify = CENTER). grid(row=0, column=0, columnspan=2)
lblHeSoA = Label(root, text = "Hệ số a").grid(row=1, column=0)
lblHeSoB = Label(root, text="Hệ số b").grid(row=2, column=0)

entHeSoA = Entry(root, width=30, textvariable = stringHSA).grid(row=1, column=1)
entHeSoB = Entry(root, width =30, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame()
btnGiai = Button(frameButton, text="Giải", command=GiaiPhuongTrinh).pack(side=LEFT)
btnTiep = Button(frameButton, text="Tiếp", command=GiaiTiep).pack(side=LEFT)
btnThoat = Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, columnspan = 2)

lblKq = Label(root, text="Kết quả").grid(row=4, column=0)
txtKq = Entry(root, width =30, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()