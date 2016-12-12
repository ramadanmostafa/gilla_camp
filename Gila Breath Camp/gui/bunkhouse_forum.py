from Tkinter import *
import tkMessageBox
from controller.bunkhouse import Bunkhouse
from controller.camper import Camper

root = None
camper_id_tb = None
camp_id_tb = None
bunkhouse_id_tb = None

def cancel_bunkhouse_forum_bt_handler():
    root.destroy()

def browse_bunkhouses_bt_handler():
    from gui.browse_bunkhouses import start_browse_bunkhouses
    root.grab_release()
    start_browse_bunkhouses()

def update_camper_bunkhouse_bt_handler():
    try:
        camper_id = int(camper_id_tb.get())
        camp_id = int(camp_id_tb.get())
        bunkhouse_id = int(bunkhouse_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="Camper ID, Camp ID and Bunkhouse ID must be numbers")
        return
    data = Bunkhouse.select_camp_team_bunkhouse(camper_id) #camps, teams, bunkhouses
    if str(camp_id) not in data[0]:
        tkMessageBox.showinfo(title="message",message="The Camper selected is not registered  in this camp")
        return
    bunkhouse_id_old = data[2][data[0].index(str(camp_id))]
    #check if the camper gender == bunkhouse gender
    myCamper = Camper(camper_id)
    camper_data = myCamper.select_camper()
    bunkhouse_data = Bunkhouse.select_bunkhouse(bunkhouse_id)
    if camper_data[3] != bunkhouse_data[0]:
        tmp = "Error:The Camper selected is " + str(camper_data[3]) + " and the bunkhouse selected if for " + str(bunkhouse_data[0]) + "s only." + bunkhouse_data[0]
        tkMessageBox.showinfo(title="message",message=tmp)
        return
    #check if there is a room available
    available_bunkhouses = Bunkhouse.get_available_bunkgouses(camper_data[3], camp_id)
    if (bunkhouse_id,) not in available_bunkhouses:
        tkMessageBox.showinfo(title="message",message="This bunkhouse is Full, choose another one.")
        return
    Bunkhouse.decrement_checked_in(bunkhouse_id_old)
    Bunkhouse.increment_checked_in(bunkhouse_id)
    Bunkhouse.update_bunkhouse_id(camper_id, camp_id, bunkhouse_id)
    tkMessageBox.showinfo(title="message",message="Bunkhouse is updated successfully")
    cancel_bunkhouse_forum_bt_handler()


def start_bunkhouse_forum():
    global root, camper_id_tb, camp_id_tb, bunkhouse_id_tb
    root = Tk()
    root.title("Bunkhouses Forum")
    root.minsize(width=400, height=500)

    browse_bunkhouses_bt = Button(root, text="Browse Bunkhouses", width=30, command = browse_bunkhouses_bt_handler)
    browse_bunkhouses_bt.pack(expand=True)

    camper_id_label = Label(root, text = "Enter Camper ID")
    camper_id_label.pack()

    camper_id_tb = Entry(root, width=20)
    camper_id_tb.pack(expand=True)

    camp_id_label = Label(root, text = "Enter Camp ID")
    camp_id_label.pack()

    camp_id_tb = Entry(root, width=20)
    camp_id_tb.pack(expand=True)

    bunkhouse_id_label = Label(root, text = "Enter Bunkhouse ID")
    bunkhouse_id_label.pack()

    bunkhouse_id_tb = Entry(root, width=20)
    bunkhouse_id_tb.pack(expand=True)

    update_camper_bunkhouse_bt = Button(root, text="Update Camper Bunkhouse", width=30, command = update_camper_bunkhouse_bt_handler)
    update_camper_bunkhouse_bt.pack(expand=True)


    cancel_bunkhouse_forum_bt = Button(root, text="Cancel", width=30, command = cancel_bunkhouse_forum_bt_handler)
    cancel_bunkhouse_forum_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
