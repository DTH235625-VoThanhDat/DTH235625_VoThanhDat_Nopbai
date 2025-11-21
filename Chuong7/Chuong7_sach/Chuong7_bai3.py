import tkinter as tk
from tkinter import messagebox
import math

def giai_ptb2():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            ket_qua.set("Không phải PT bậc 2")
            return

        delta = b*b - 4*a*c

        if delta < 0:
            ket_qua.set("Vô nghiệm")
        elif delta == 0:
            x = -b / (2*a)
            ket_qua.set(f"x1 = x2 = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            ket_qua.set(f"x1={x1}, x2={x2}")
    except Exception:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")

root = tk.Tk()
root.title("Phương Trình Bậc 2")

tk.Label(root, text="Hệ số a:").grid(row=0, column=0)
tk.Label(root, text="Hệ số b:").grid(row=1, column=0)
tk.Label(root, text="Hệ số c:").grid(row=2, column=0)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)

entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)

ket_qua = tk.StringVar()
tk.Label(root, text="Kết quả:").grid(row=4, column=0)
tk.Label(root, textvariable=ket_qua).grid(row=4, column=1)

tk.Button(root, text="Giải", command=giai_ptb2).grid(row=3, column=0)
tk.Button(root, text="Thoát", command=root.quit).grid(row=3, column=1)

root.mainloop()
