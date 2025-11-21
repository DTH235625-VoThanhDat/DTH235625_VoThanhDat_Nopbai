import tkinter as tk
from tkinter import messagebox

def kiem_tra():
    old = e1.get()
    new = e2.get()
    again = e3.get()

    if new == old:
        messagebox.showwarning("Lỗi", "Bạn không được dùng mật khẩu cũ!")
        return

    if new != again:
        messagebox.showerror("Sai", "Bạn phải nhập lại mật khẩu mới giống nhau")
    else:
        messagebox.showinfo("Thành công", "Đổi mật khẩu thành công!")

root = tk.Tk()
root.title("Đổi mật khẩu")

tk.Label(root, text="Old Password:").grid(row=0, column=0)
tk.Label(root, text="New Password:").grid(row=1, column=0)
tk.Label(root, text="Enter New Password Again:").grid(row=2, column=0)

e1 = tk.Entry(root, show="*")
e2 = tk.Entry(root, show="*")
e3 = tk.Entry(root, show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

tk.Button(root, text="OK", command=kiem_tra).grid(row=3, column=0)
tk.Button(root, text="Cancel", command=root.quit).grid(row=3, column=1)

root.mainloop()
