from Tkinter import *
from ttk import Treeview
from controller.bunkhouse import Bunkhouse
from controller.camp import Camp

root = None

def exit_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

def start_query_browse():
    global root
    root = Tk()
    root.title("Browse Camps, Bunkhouse and Teams")
    root.minsize(width=800, height=500)

    browse_query_tree = Treeview(root)
    browse_query_tree["columns"] = ("2", "3", "4", "5", "6", "7", "8", "1", "9", "10")
    browse_query_tree.column("1", width=100)
    browse_query_tree.column("2", width=65)
    browse_query_tree.column("3", width=100)
    browse_query_tree.column("4", width=100)
    browse_query_tree.column("5", width=80)
    browse_query_tree.column("6", width=100)
    browse_query_tree.column("7", width=100)
    browse_query_tree.column("8", width=50)
    browse_query_tree.column("9", width=100)
    browse_query_tree.column("10", width=235)
    browse_query_tree.heading("2", text="Camp ID")
    browse_query_tree.heading("3", text="Camp Start Date")
    browse_query_tree.heading("4", text="Camp End Date")
    browse_query_tree.heading("5", text="Camper ID")
    browse_query_tree.heading("6", text="First Name")
    browse_query_tree.heading("7", text="Last Name")
    browse_query_tree.heading("8", text="Gender")
    browse_query_tree.heading("1", text="Bunkhous ID")
    browse_query_tree.heading("9", text="Tribe ID")
    browse_query_tree.heading("10", text="Number of Campers Registered")

    #data_new = current_camp.get_number_campers_registered()

    index = 0
    for row_data in Bunkhouse.get_all_query_data():
        mycamp = Camp(row_data[1])
        data_new = mycamp.get_number_campers_registered()
        browse_query_tree.insert('', index, text= "row" + str(index + 1), values = (
        row_data[1], row_data[2], row_data[3], row_data[4], row_data[5], row_data[6], row_data[7], row_data[0], row_data[8], data_new))
        index += 1

    browse_query_tree.pack()

    exit_bt = Button(root, text="Exit", width=30, command = exit_bt_handler)
    exit_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
