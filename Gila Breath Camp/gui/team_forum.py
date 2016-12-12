from Tkinter import *
import tkMessageBox
from controller.bunkhouse import Bunkhouse
from controller.team import Team
from controller.camper import Camper

root = None
camper_id_tb = None
camp_id_tb = None
team_id_tb = None

def cancel_team_forum_bt_handler():
    root.destroy()

def browse_teams_bt_handler():
    from gui.browse_teams import start_browse_teams
    root.grab_release()
    start_browse_teams()

def update_camper_team_bt_handler():
    try:
        camper_id = int(camper_id_tb.get())
        camp_id = int(camp_id_tb.get())
        team_id = int(team_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="Camper ID, Camp ID and Team ID must be numbers")
        return
    data = Bunkhouse.select_camp_team_bunkhouse(camper_id) #camps, tribes, bunkhouses
    if str(camp_id) not in data[0]:
        tkMessageBox.showinfo(title="message",message="The Camper selected is not registered in this camp")
        return
    team_id_old = data[1][data[0].index(str(camp_id))]
    #check if there is a room available
    available_teams = Team.get_available_team(camp_id)
    if (team_id,) not in available_teams:
        tkMessageBox.showinfo(title="message",message="This Tribe is Full, choose another one.")
        return
    Team.decrement_checked_in(team_id_old)
    Team.increment_checked_in(team_id)
    Team.update_team_id(camper_id, camp_id, team_id)
    tkMessageBox.showinfo(title="message",message="Tribe is updated successfully")
    cancel_team_forum_bt_handler()

def start_team_forum():
    global root, camper_id_tb, camp_id_tb, team_id_tb
    root = Tk()
    root.title("Tribe Form")
    root.minsize(width=400, height=500)

    browse_teams_bt = Button(root, text="Browse Tribes", width=30, command = browse_teams_bt_handler)
    browse_teams_bt.pack(expand=True)

    camper_id_label = Label(root, text = "Enter Camper ID")
    camper_id_label.pack()

    camper_id_tb = Entry(root, width=20)
    camper_id_tb.pack(expand=True)

    camp_id_label = Label(root, text = "Enter Camp ID")
    camp_id_label.pack()

    camp_id_tb = Entry(root, width=20)
    camp_id_tb.pack(expand=True)

    team_id_label = Label(root, text = "Enter Tribe ID")
    team_id_label.pack()

    team_id_tb = Entry(root, width=20)
    team_id_tb.pack(expand=True)

    update_camper_team_bt = Button(root, text="Update Camper Tribe", width=30, command = update_camper_team_bt_handler)
    update_camper_team_bt.pack(expand=True)


    cancel_team_forum_bt = Button(root, text="Cancel", width=30, command = cancel_team_forum_bt_handler)
    cancel_team_forum_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
