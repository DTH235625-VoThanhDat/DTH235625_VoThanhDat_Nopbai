import tkinter as tk

def cong():
    try:
        a = float(e1.get())
        b = float(e2.get())
        kq.set(a + b)
    except Exception:
        kq.set("Lỗi nhập!")

root = tk.Tk()
root.title("Cộng 2 số")

tk.Label(root, text="Số thứ 1:").grid(row=0, column=0)
tk.Label(root, text="Số thứ 2:").grid(row=1, column=0)

e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

kq = tk.StringVar()
tk.Label(root, text="Kết quả:").grid(row=3, column=0)
tk.Label(root, textvariable=kq).grid(row=3, column=1)

tk.Button(root, text="Cộng", command=cong).grid(row=2, column=0)
tk.Button(root, text="Thoát", command=root.quit).grid(row=2, column=1)

root.mainloop()
