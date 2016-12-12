from Tkinter import *
import tkMessageBox
from controller.bunkhouse import Bunkhouse
from controller.team import Team
from controller.camp import Camp

root = None
teams_capacity_tb = None
bunkhouses_capacity_tb = None

def update_bt_handler():
    try:
        teams_capacity = int(teams_capacity_tb.get())
        bunkhouses_capacity = int(bunkhouses_capacity_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="Tribes and Bunkhouses Capacity must be numbers")
        return
    else:
        Bunkhouse.update_bunkhouses_num(bunkhouses_capacity)
        Team.update_teams_num(teams_capacity)
        Camp.update_max_capacity(bunkhouses_capacity)
        tkMessageBox.showinfo(title="message",message="Capacity of camps, tribes and bunkhouses have been updated")
        cancel_bt_handler()

def cancel_bt_handler():
    root.destroy()

def modify_bunkhouse_team_start():
    global root, teams_capacity_tb, bunkhouses_capacity_tb
    root = Tk()
    root.title("Modify bunkhouses and tribes capacity")
    root.minsize(width=400, height=400)

    teams_capacity_label = Label(root, text = "Tribes Capacity")
    teams_capacity_label.pack()

    teams_capacity_tb = Entry(root, width=20)
    teams_capacity_tb.pack(expand=True)

    bunkhouses_capacity_label = Label(root, text = "Bunkhouses Capacity")
    bunkhouses_capacity_label.pack()

    bunkhouses_capacity_tb = Entry(root, width=20)
    bunkhouses_capacity_tb.pack(expand=True)

    update_bt = Button(root, text="Update", width=30, command = update_bt_handler)
    update_bt.pack(expand=True)

    cancel_bt = Button(root, text="Cancel", width=30, command = cancel_bt_handler)
    cancel_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
