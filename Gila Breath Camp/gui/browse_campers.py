from Tkinter import *
from ttk import Treeview
from controller.camper import Camper
from controller.bunkhouse import Bunkhouse

root = None

def exit_browse_camp_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

#select camper_id, first_name, last_name, date_of_birth, gender from Campers

def start_browse_campers():
    global root
    root = Tk()
    root.title("Browse Campers")
    root.minsize(width=500, height=500)

    browse_camps_tree = Treeview(root)
    browse_camps_tree["columns"] = ("Camper ID", "First Name", "Last Name", "Date of Birth", "Gender", "Address", "Camps IDs", "Bunkhouses IDs", "Teams IDs")
    browse_camps_tree.column("Camper ID", width=100)
    browse_camps_tree.column("First Name", width=100)
    browse_camps_tree.column("Last Name", width=100)
    browse_camps_tree.column("Date of Birth", width=100)
    browse_camps_tree.column("Gender", width=100)
    browse_camps_tree.column("Address", width=100)
    browse_camps_tree.column("Camps IDs", width=100)
    browse_camps_tree.column("Bunkhouses IDs", width=100)
    browse_camps_tree.column("Teams IDs", width=100)
    browse_camps_tree.heading("Camper ID", text="Camper ID")
    browse_camps_tree.heading("First Name", text="First Name")
    browse_camps_tree.heading("Last Name", text="Last Name")
    browse_camps_tree.heading("Date of Birth", text="Date of Birth")
    browse_camps_tree.heading("Gender", text="Gender")
    browse_camps_tree.heading("Address", text="Address")
    browse_camps_tree.heading("Camps IDs", text="Camp ID")
    browse_camps_tree.heading("Bunkhouses IDs", text="Bunkhouse ID")
    browse_camps_tree.heading("Teams IDs", text="Tribe ID")

    index = 0
    for camper_id in Camper.get_all_ids():
        current_camper = Camper(camper_id[0])
        data = current_camper.select_camper()
        data2 = Bunkhouse.select_camp_team_bunkhouse(camper_id[0])
        browse_camps_tree.insert('', index, text= "row" + str(index + 1), values = (camper_id, data[0], data[1], data[2], data[3], data[4], data2[0][:-2], data2[2][:-2], data2[1][:-2]))
        index += 1

    browse_camps_tree.pack()

    exit_browse_camp_bt = Button(root, text="Exit", width=30, command = exit_browse_camp_bt_handler)
    exit_browse_camp_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
