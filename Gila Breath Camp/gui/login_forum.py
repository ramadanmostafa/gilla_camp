from Tkinter import *
import tkMessageBox
from controller.authenticate import AuthUser
from gui.main_window import start_main_window, start_main_window_admin

root = None
username_tb = None
password_tb = None

def login_bt_handler():
    user = AuthUser(username_tb.get(), password_tb.get())
    if user.authenticate():
        root.destroy()
        if user.is_admin():
            start_main_window_admin()
        else:
            start_main_window()
    else:
        tkMessageBox.showinfo(title="message",message="username or password are wrong, try again")

def cancel_bt_handler():
    root.destroy()

def start_login_forum():
    global root, username_tb, password_tb
    root = Tk()
    root.title("Login Form")
    root.minsize(width=400, height=200)

    username_label = Label(root, text = "User Name")
    username_label.pack()

    username_tb = Entry(root, width=20)
    username_tb.pack(expand=True)

    password_label = Label(root, text = "Password")
    password_label.pack()

    password_tb = Entry(root, show="*", width=20)
    password_tb.pack(expand=True)

    login_bt = Button(root, text="Login", width=30, command = login_bt_handler)
    login_bt.pack(expand=True)

    cancel_bt = Button(root, text="Cancel", width=30, command = cancel_bt_handler)
    cancel_bt.pack(expand=True)

    root.grab_set()
    root.mainloop()
