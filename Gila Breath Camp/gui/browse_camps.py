from Tkinter import *
from ttk import Treeview
from controller.camp import Camp

root = None

def exit_browse_camp_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

#select camper_id, first_name, last_name, date_of_birth, gender from Campers

def start_browse_camps():
    global root
    root = Tk()
    root.title("Browse Camps")
    root.minsize(width=500, height=500)

    browse_camps_tree = Treeview(root)
    browse_camps_tree["columns"] = ("Camp ID", "Start Date", "End Date", "Number of Bunckhouses", "Number of Teams", "Cost", "number of campers registered")
    browse_camps_tree.column("Camp ID", width=100)
    browse_camps_tree.column("Start Date", width=100)
    browse_camps_tree.column("End Date", width=100)
    browse_camps_tree.column("Number of Bunckhouses", width=100)
    browse_camps_tree.column("Number of Teams", width=100)
    browse_camps_tree.column("Cost", width=100)
    browse_camps_tree.column("number of campers registered", width=100)
    browse_camps_tree.heading("Camp ID", text="Camp ID")
    browse_camps_tree.heading("Start Date", text="Start Date")
    browse_camps_tree.heading("End Date", text="End Date")
    browse_camps_tree.heading("Number of Bunckhouses", text="Number of Bunkhouses")
    browse_camps_tree.heading("Number of Teams", text="Number of Tribes")
    browse_camps_tree.heading("Cost", text = "Cost")
    browse_camps_tree.heading("number of campers registered", text = "number of campers registered")


    index = 0
    for camp_id in Camp.get_all_ids():
        current_camp = Camp(camp_id[0])
        data = current_camp.select_camp()
        data_new = current_camp.get_number_campers_registered()
        browse_camps_tree.insert('', index, text= "row" + str(index + 1), values = (camp_id, data[0], data[1], data[2], data[3], data[4], data_new))
        index += 1

    browse_camps_tree.pack()


    exit_browse_camp_bt = Button(root, text="Exit", width=30, command = exit_browse_camp_bt_handler)
    exit_browse_camp_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
