import tkinter as tk
from tkinter import messagebox

def tinh(op):
    try:
        a = float(e1.get())
        b = float(e2.get())

        if op == '+':
            kq.set(a + b)
        elif op == '-':
            kq.set(a - b)
        elif op == '*':
            kq.set(a * b)
        elif op == '/':
            if b == 0:
                kq.set("Không chia được")
            else:
                kq.set(a / b)

    except Exception:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")

root = tk.Tk()
root.title("Cộng Trừ Nhân Chia")

tk.Label(root, text="Số thứ 1:").grid(row=0, column=0)
tk.Label(root, text="Số thứ 2:").grid(row=1, column=0)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

kq = tk.StringVar()
tk.Label(root, text="Kết quả:").grid(row=3, column=0)
tk.Label(root, textvariable=kq).grid(row=3, column=1)

tk.Button(root, text="Cộng", command=lambda: tinh('+')).grid(row=2, column=0)
tk.Button(root, text="Trừ", command=lambda: tinh('-')).grid(row=2, column=1)
tk.Button(root, text="Nhân", command=lambda: tinh('*')).grid(row=2, column=2)
tk.Button(root, text="Chia", command=lambda: tinh('/')).grid(row=2, column=3)
tk.Button(root, text="Thoát", command=root.quit).grid(row=4, column=1)

root.mainloop()
