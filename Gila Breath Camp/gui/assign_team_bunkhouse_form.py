from Tkinter import *
import tkMessageBox
from datetime import date, datetime
from controller.camper import Camper
from controller.camp import Camp
from controller.bunkhouse import Bunkhouse
from controller.team import Team

top = None
camp_id_tb = None

def increment_index(current_value, max_value):
    next_index = current_value + 1
    if next_index < max_value:
        return next_index
    else:
        return 0

def assign_campers_bt_handler():
    camp_id = camp_id_tb.get()
    if not camp_id.isdigit():
        tkMessageBox.showinfo(title="ERROR",message="Camp ID must be a number not text")
        return
    camp_id = int(camp_id)
    if (camp_id,) not in Camp.get_all_ids():
        tkMessageBox.showinfo(title="ERROR",message="Camp Not Found")
        return
    #get all campers registered in this camp ordered by date of birth
    all_campers_ids = Camper.get_all_ids_assigned_camp(camp_id)
    all_campers_male = []
    all_campers_female = []
    for camper in all_campers_ids:
        if camper[1] == "Male":
            all_campers_male.append(camper[0])
        else:
            all_campers_female.append(camper[0])

    teams_ids = Team.get_available_team(camp_id)
    bunkhouses_ids_male = Bunkhouse.get_available_bunkgouses("Male", camp_id)
    bunkhouses_ids_female = Bunkhouse.get_available_bunkgouses("Female", camp_id)

    ###############################################################################
    # Bunkhouse.increment_checked_in(bunkhouses_id)
    # Team.increment_checked_in(teams_id)
    # #update a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
    # Bunkhouse.update_check_in(camper_id,camp_id,teams_ids[team_index][0],bunkhouses_ids[bunkhouse_index][0])

    index_bunkhouse = 0
    index_team = 0
    for camper in all_campers_male:
        Bunkhouse.increment_checked_in(bunkhouses_ids_male[index_bunkhouse][0])
        Team.increment_checked_in(teams_ids[index_team][0])
        #update a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
        Bunkhouse.update_check_in(camper, camp_id, teams_ids[index_team][0], bunkhouses_ids_male[index_bunkhouse][0])
        index_team = increment_index(index_team, len(teams_ids))
        index_bunkhouse = increment_index(index_bunkhouse, len(bunkhouses_ids_male))
    index_bunkhouse = 0
    index_team = 0
    for camper in all_campers_female:
        Bunkhouse.increment_checked_in(bunkhouses_ids_female[index_bunkhouse][0])
        Team.increment_checked_in(teams_ids[index_team][0])
        #update a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
        Bunkhouse.update_check_in(camper, camp_id, teams_ids[index_team][0], bunkhouses_ids_female[index_bunkhouse][0])
        index_team = increment_index(index_team, len(teams_ids))
        index_bunkhouse = increment_index(index_bunkhouse, len(bunkhouses_ids_female))

    #process special options for teams and bunkhouses
    options_data = Bunkhouse.get_special_options()
    for row in options_data:
        #row = camper_id, bunk_house_id, team_id, bunkhouse_options, team_options
        current_camper = Camper(row[0])
        camper_id = row[0]
        gender = current_camper.select_camper()[3]
        if row[1] is not None:
            #camp_id, team_id, bunk_house_id
            target = Bunkhouse.select_camp_team_bunkhouse_simple_db(row[3].split()[-1])[0]
            if row[3].split()[0] == "Yes":
                if row[1] != target[2]:
                    Bunkhouse.update_bunkhouse_id(camper_id, camp_id, target[2])
                    Bunkhouse.increment_checked_in(target[2])
                    Bunkhouse.decrement_checked_in(row[1])
            elif row[3].split()[0] == "No":
                if row[1] == target[2]:
                    available = Bunkhouse.get_available_bunkgouses(gender, camp_id)
                    tmp = (row[1],)
                    if tmp in available:
                        available.remove(tmp)
                    Bunkhouse.update_bunkhouse_id(camper_id, camp_id, available[0][0])
                    Bunkhouse.increment_checked_in(available[0][0])
                    Bunkhouse.decrement_checked_in(row[1])
        if row[2] is not None:
            #camp_id, team_id, bunk_house_id
            target = Bunkhouse.select_camp_team_bunkhouse_simple_db(row[4].split()[-1])[0]
            if row[4].split()[0] == "Yes":
                if row[2] != target[1]:
                    Team.update_team_id(camper_id, camp_id, target[1])
                    Team.increment_checked_in(target[1])
                    Team.decrement_checked_in(row[2])
            elif row[4].split()[0] == "No":
                if row[2] == target[1]:
                    available = Team.get_available_team(camp_id)
                    tmp = (row[2],)
                    if tmp in available:
                        available.remove(tmp)
                    Team.update_team_id(camper_id, camp_id, available[0][0])
                    Team.increment_checked_in(available[0][0])
                    Team.decrement_checked_in(row[2])
    tkMessageBox.showinfo(title="OK",message="All Assigned Successfully")
    cancel_bt_handler()


def cancel_bt_handler():
    top.destroy()

def start_assign_team_bunkhouse_form():
    global top, camp_id_tb
    top = Tk()
    top.title("Assign Campers to teams and bunkhouses")
    top.minsize(width=400, height=300)

    assign_campers_bt = Button(top, text="Assign Campers", width=30, command = assign_campers_bt_handler)
    cancel_bt = Button(top, text="Cancel", width=30, command = cancel_bt_handler)

    camp_id_label = Label(top, text = "Enter Camp ID")
    camp_id_tb = Entry(top, width=20)

    camp_id_label.pack()
    camp_id_tb.pack(expand=True)

    assign_campers_bt.pack(expand=True)
    cancel_bt.pack(expand=True)

    top.grab_set()
    top.mainloop()
