from Tkinter import *
import tkMessageBox
from datetime import datetime

top = None
camper_id_tb = None
camp_id_tb = None

def assign_to_camp_bt_handler():
    try:
        camper_id = int(camper_id_tb.get())
        camp_id = int(camp_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="camper and camp id must be nubmers")
        return
    from controller.camper import Camper
    from controller.camp import Camp
    from controller.bunkhouse import Bunkhouse
    from controller.team import Team
    checked_in_camper = Camper(camper_id)
    checked_in_camp = Camp(camp_id)
    if checked_in_camper.select_camper() == None:
        tkMessageBox.showinfo(title="message",message="camper not found")
        return
    tmp_camp_data = checked_in_camp.select_camp()
    if tmp_camp_data == None:
        tkMessageBox.showinfo(title="message",message="camp not found")
        return
    #check there is a room for this camper in bunkhouse gender?
    data_camper = checked_in_camper.select_camper()
    gender = data_camper[3]
    bunkhouses_ids = Bunkhouse.get_available_bunkgouses(gender, camp_id)
    if len(bunkhouses_ids) < 1:
        tkMessageBox.showinfo(title="message",message="Sorry, This camp is not available, Choose another one")
        return
    #check if this camper is already regestered in this camp
    data_camp = Bunkhouse.select_camp_team_bunkhouse(camper_id)
    if str(camp_id) in data_camp[0]:
        tkMessageBox.showinfo(title="message",message="Sorry, This camper is already registered in this camp")
        return
    teams_ids = Team.get_available_team(camp_id)
    #assign this camper to a team and a bunkhouse and get their ids(inc checked_in_num)
    Bunkhouse.increment_checked_in(bunkhouses_ids[0][0])
    Team.increment_checked_in(teams_ids[0][0])
    Camp.increment_registered(camp_id)
    #insert a record in Camper_Camp_Bunkouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
    Bunkhouse.insert_check_in(camper_id,camp_id,teams_ids[0][0],bunkhouses_ids[0][0])
    #show a message box saying, the camper checked in successfully
    tkMessageBox.showinfo(title="message",message="Camper Assigned successfully")
    

    mailing_date = str(datetime.now().date())
    first_name = data_camper[0]
    last_name = data_camper[1]
    address = data_camper[4]
    camp_start_date = tmp_camp_data[0]
    camp_end_date = tmp_camp_data[1]
    f1 = open("Mailing Label.txt", 'w')
    f1.write(mailing_date + "\n" + first_name + ' ' + last_name + "\n" + address)
    f1.close()
    import webbrowser
    webbrowser.open("Mailing Label.txt")

    f2 = open("acceptance letter.txt", 'w')
    f2.write("Congratulations " + first_name + ' ' + last_name +"! you have been accepted for the camp starting on " + camp_start_date + " and ending on " + camp_end_date + ".\nThanks")
    f2.close()
    webbrowser.open("acceptance letter.txt")

    
    cancel_bt_handler()

def cancel_bt_handler():
    top.destroy()

def start_assign_to_camp():

    global top, camper_id_tb, camp_id_tb

    top = Tk()
    top.title("Check-in Forum")
    top.minsize(width=400, height=400)

    camper_id_label = Label(top, text = "Enter camper ID")
    camper_id_tb = Entry(top, width=20)
    camp_id_label = Label(top, text = "Enter Camp ID")
    camp_id_tb = Entry(top, width=20)

    assign_to_camp_bt = Button(top, text="Assign to Camp", width=30, command = assign_to_camp_bt_handler)
    cancel_bt = Button(top, text="Cancel", width=30, command = cancel_bt_handler)

    camper_id_label.pack()
    camper_id_tb.pack(expand=True)
    camp_id_label.pack()
    camp_id_tb.pack(expand=True)
    assign_to_camp_bt.pack(expand=True)
    cancel_bt.pack(expand=True)

    top.grab_set()
    top.mainloop()
