from tkinter import *

root = Tk()
stringKQ = StringVar()


def click_button(value):
    current = stringKQ.get()
    stringKQ.set(current + value)

def clear():
    stringKQ.set("")

def TinhToan():
    try:
        result = str(eval(stringKQ.get()))
        stringKQ.set(result)
    except:
        stringKQ.set("Lỗi")

#root.minsize(height = 180, width= 30)
root.resizable(height=True, width=True)

entKQ = Entry(root, textvariable=stringKQ, width=40).grid(row=0, columnspan=3, padx=10, pady=10)

frameButton1 = Frame()
btn1 = Button(frameButton1, text="1", width=10, command= lambda: click_button("1")).pack(side=LEFT)
btn2 = Button(frameButton1, text="2", width=10, command= lambda: click_button("2")).pack(side=LEFT)
btn3 = Button(frameButton1, text="3", width=10, command= lambda: click_button("3")).pack(side=LEFT)
frameButton1.grid(row=1, columnspan=3)

frameButton2 = Frame()
btn4 = Button(frameButton2, text="4", width=10, command= lambda: click_button("4")).pack(side=LEFT)
btn5 = Button(frameButton2, text="5", width=10, command= lambda: click_button("5")).pack(side=LEFT)
btn6 = Button(frameButton2, text="6", width=10, command= lambda: click_button("6")).pack(side=LEFT)
frameButton2.grid(row=2, columnspan=3)

frameButton3 = Frame()
btn7 = Button(frameButton3, text="7", width=10, command= lambda: click_button("7")).pack(side=LEFT)
btn8 = Button(frameButton3, text="8", width=10, command= lambda: click_button("8")).pack(side=LEFT)
btn9 = Button(frameButton3, text="9", width=10, command= lambda: click_button("9")).pack(side=LEFT)
frameButton3.grid(row=3, columnspan=3)

frameButton4 = Frame()
btngach = Button(frameButton4, text="_", width=10, command= lambda: click_button("_")).pack(side=LEFT)
btn0 = Button(frameButton4, text="0", width=10, command= lambda: click_button("0")).pack(side=LEFT)
btncham = Button(frameButton4, text=".", width=10, command= lambda: click_button(".")).pack(side=LEFT)
frameButton4.grid(row=4, columnspan=3)

frameButton5 = Frame()
btncong = Button(frameButton5, text="+", width=5, command= lambda: click_button("+")).pack(side=LEFT)
btntru = Button(frameButton5, text="-", width=5, command= lambda: click_button("-")).pack(side=LEFT)
btnnhan = Button(frameButton5, text="*", width=5, command= lambda: click_button("*")).pack(side=LEFT)
btnchia = Button(frameButton5, text="/", width=5, command= lambda: click_button("/")).pack(side=LEFT)
btnbang = Button(frameButton5, text="=", width=7, command=TinhToan).pack(side=LEFT)
frameButton5.grid(row=5, columnspan=3)

btnhuy = Button(root, text="Clr", width=33, command=clear).grid(row=6, columnspan=3)

root.mainloop()