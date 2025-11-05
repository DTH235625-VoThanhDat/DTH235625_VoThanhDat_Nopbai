from tkinter import *

frmLogin = Tk()
frmLogin.title("Enter New Password")
frmLogin.minsize(height=50, width=70)
frmLogin.resizable(False, False)


Label(frmLogin, text="Old Password:", anchor="w", width=22).grid(row=0, column=0, padx=10, pady=5, sticky="w")
Label(frmLogin, text="New Password:", anchor="w", width=22).grid(row=1, column=0, padx=10, pady=5, sticky="w")
Label(frmLogin, text="Enter New Password Again:", anchor="w", width=22).grid(row=2, column=0, padx=10, pady=5, sticky="w")

Entry(frmLogin, show="*", width=25).grid(row=0, column=1, padx=5, pady=5)
Entry(frmLogin, show="*", width=25).grid(row=1, column=1, padx=5, pady=5)
Entry(frmLogin, show="*", width=25).grid(row=2, column=1, padx=5, pady=5)


frameButton = Frame()
Button(frameButton, text="OK", width=10).pack(side=LEFT, padx=5)
Button(frameButton, text="Cancel", width=10).pack(side=LEFT, padx=5)
frameButton.grid(row=3, column=0, columnspan=2, pady=10)

frmLogin.mainloop()