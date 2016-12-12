from Tkinter import *
from ttk import Treeview
from controller.team import Team

root = None

def exit_browse_teams_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

#select camper_id, first_name, last_name, date_of_birth, gender from Campers

def start_browse_teams():
    global root
    root = Tk()
    root.title("Browse Teams")
    root.minsize(width=500, height=500)

    browse_teams_tree = Treeview(root)
    browse_teams_tree["columns"] = ("1", "2", "4", "5")
    browse_teams_tree.column("1", width=100)
    browse_teams_tree.column("2", width=100)
    browse_teams_tree.column("4", width=100)
    browse_teams_tree.column("5", width=100)
    browse_teams_tree.heading("1", text="Team ID")
    browse_teams_tree.heading("2", text="Camp ID")
    browse_teams_tree.heading("4", text="Max Number of Members")
    browse_teams_tree.heading("5", text="Number of Members")

    index = 0
    for team_id in Team.get_all_ids():
        current_team = Team.select_team(team_id[0])
        browse_teams_tree.insert('', index, text= "row" + str(index + 1), values = (team_id[0], current_team[0], current_team[2], current_team[3]))
        index += 1

    browse_teams_tree.pack()

    exit_browse_teams_bt = Button(root, text="Exit", width=30, command = exit_browse_teams_bt_handler)
    exit_browse_teams_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
