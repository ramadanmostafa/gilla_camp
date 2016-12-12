from Tkinter import *
import tkMessageBox

root = None
camp_id_tb = None

def browse_camp_bt_handler():
    from browse_camps import start_browse_camps
    root.grab_release()
    start_browse_camps()

def add_camp_bt_handler():
    from add_camp_forum import start_add_camp_forum
    root.grab_release()
    start_add_camp_forum()

def update_camp_bt_handler():
    from add_camp_forum import update_camp_forum
    try:
        root.grab_release()
        update_camp_forum(int(camp_id_tb.get()))
    except:
        tkMessageBox.showinfo(title="message",message="camp ID must be a number")

def delete_camp_bt_handler():
    try:
        camp_id = int(camp_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="camp ID must be a number")
    else:
        from controller.camp import Camp
        myCamp = Camp(camp_id)
        myCamp.delete_camp()
        tkMessageBox.showinfo(title="message",message="record deleted")

def cancel_main_bt_handler():
    root.destroy()


def start_camp_window():
    global root, camp_id_tb
    root = Tk()
    root.title("Camp")
    root.minsize(width=400, height=400)

    browse_camp_bt = Button(root, text="Browse Camps", width=30, command = browse_camp_bt_handler)
    browse_camp_bt.pack(expand=True)

    add_camp_bt = Button(root, text="ADD Camp", width=30, command = add_camp_bt_handler)
    add_camp_bt.pack(expand=True)

    camp_id_label = Label(root, text = "Enter Camp ID")
    camp_id_label.pack()

    camp_id_tb = Entry(root, width=20)
    camp_id_tb.pack(expand=True)

    update_camp_bt = Button(root, text="Update Camp", width=30, command = update_camp_bt_handler)
    update_camp_bt.pack(expand=True)

    delete_camp_bt = Button(root, text="Delete Camp", width=30, command = delete_camp_bt_handler)
    delete_camp_bt.pack(expand=True)

    cancel_main_bt = Button(root, text="Cancel", width=30, command = cancel_main_bt_handler)
    cancel_main_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
