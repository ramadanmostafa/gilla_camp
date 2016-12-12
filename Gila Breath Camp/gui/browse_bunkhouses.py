from Tkinter import *
from ttk import Treeview
from controller.bunkhouse import Bunkhouse

root = None

def exit_browse_bunkhouses_bt_handler():
    global root
    #root.grab_release()
    root.destroy()


def start_browse_bunkhouses():
    global root
    root = Tk()
    root.title("Browse Bunkhouses")
    root.minsize(width=500, height=500)

    browse_bunkhouses_tree = Treeview(root)
    browse_bunkhouses_tree["columns"] = ("1", "2", "3", "4", "5")
    browse_bunkhouses_tree.column("1", width=100)
    browse_bunkhouses_tree.column("2", width=100)
    browse_bunkhouses_tree.column("3", width=100)
    browse_bunkhouses_tree.column("4", width=100)
    browse_bunkhouses_tree.column("5", width=100)
    browse_bunkhouses_tree.heading("1", text="Bunkhouse ID")
    browse_bunkhouses_tree.heading("2", text="Campers Gender")
    browse_bunkhouses_tree.heading("3", text="Camp ID")
    browse_bunkhouses_tree.heading("4", text="Max Number of Members")
    browse_bunkhouses_tree.heading("5", text="Number of Members")

    index = 0
    for bunkhouse_id in Bunkhouse.get_all_ids():
        current_bunkhouse = Bunkhouse.select_bunkhouse(bunkhouse_id[0])
        browse_bunkhouses_tree.insert('', index, text= "row" + str(index + 1), values = (bunkhouse_id[0], current_bunkhouse[0], current_bunkhouse[1], current_bunkhouse[2], current_bunkhouse[3]))
        index += 1

    browse_bunkhouses_tree.pack()

    exit_browse_bunkhouses_bt = Button(root, text="Exit", width=30, command = exit_browse_bunkhouses_bt_handler)
    exit_browse_bunkhouses_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
