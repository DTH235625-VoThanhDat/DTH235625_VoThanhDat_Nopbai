import tkinter as tk
from tkinter import messagebox

def giai():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if a == 0:
            if b == 0:
                ket_qua.set("Vô số nghiệm")
            else:
                ket_qua.set("Vô nghiệm")
        else:
            x = -b / a
            ket_qua.set(f"x = {x}")
    except Exception:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")

root = tk.Tk()
root.title("Phương Trình Bậc 1")

tk.Label(root, text="Hệ số a:").grid(row=0, column=0)
tk.Label(root, text="Hệ số b:").grid(row=1, column=0)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)

ket_qua = tk.StringVar()
tk.Label(root, text="Kết quả:").grid(row=3, column=0)
tk.Label(root, textvariable=ket_qua).grid(row=3, column=1)

tk.Button(root, text="Giải", command=giai).grid(row=2, column=0)
tk.Button(root, text="Thoát", command=root.quit).grid(row=2, column=1)

root.mainloop()
