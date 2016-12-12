from Tkinter import *
import tkMessageBox

root = None
update_camper_tb = None


def add_camper_bt_handler():
    #root.grab_set() # when you show the popup
    # do stuff ...
    #b.grab_release() # to return to normal
    from camper_forum import start_camper_forum
    root.grab_release()
    start_camper_forum()

def browse_camper_bt_handler():
    from browse_campers import start_browse_campers
    root.grab_release()
    start_browse_campers()

def update_camper_bt_handler():
    from camper_forum import update_camper
    root.grab_release()
    camper_id_update = update_camper_tb.get().strip()
    if camper_id_update.isdigit():
        update_camper(camper_id_update)
    else:
        tkMessageBox.showinfo(title="message",message="camper ID must be a number")

def delete_camper_bt_handler():
    try:
        camper_id = int(update_camper_tb.get().strip())
    except:
        tkMessageBox.showinfo(title="message",message="camper ID must be a number")
    else:
        from controller.camper import Camper
        mycamper = Camper(camper_id)
        mycamper.delete_camper()
        Camper.unregister_camper(camper_id)
        tkMessageBox.showinfo(title="message",message="record deleted")

def cancel_main_bt_handler():
    update_camper_tb.delete(0, 'end')
    root.grab_release()
    root.destroy()


def start_camper_window():
    global root, update_camper_tb
    root = Tk()
    root.title("Camper")
    root.minsize(width=400, height=400)

    browse_camper_bt = Button(root, text="Browse campers", width=30, command = browse_camper_bt_handler)
    browse_camper_bt.pack(expand=True)

    add_camper_bt = Button(root, text="ADD camper", width=30, command = add_camper_bt_handler)
    add_camper_bt.pack(expand=True)

    update_camper_label = Label(root, text = "Enter camper ID")
    update_camper_label.pack()

    update_camper_tb = Entry(root, width=20)
    update_camper_tb.pack(expand=True)

    update_camper_bt = Button(root, text="Update camper", width=30, command = update_camper_bt_handler)
    update_camper_bt.pack(expand=True)

    delete_camper_bt = Button(root, text="Delete camper", width=30, command = delete_camper_bt_handler)
    delete_camper_bt.pack(expand=True)

    cancel_main_bt = Button(root, text="Cancel", width=30, command = cancel_main_bt_handler)
    cancel_main_bt.pack(expand=True)

    root.grab_set()
    root.mainloop()
