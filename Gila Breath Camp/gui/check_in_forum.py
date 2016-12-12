from Tkinter import *
import tkMessageBox
import webbrowser
from datetime import date, datetime
from controller.camper import Camper
from controller.camp import Camp
from controller.bunkhouse import Bunkhouse
from controller.team import Team

top = None
slepping_bag_CheckVar = None
pillow_CheckVar = None
blanket_CheckVar = None
spray_CheckVar = None
bathing_suit_CheckVar = None
sun_block_CheckVar = None
rain_coat_CheckVar = None
flashlight_CheckVar = None
camper_id_tb = None
camp_id_tb = None
campers_name_variable = None
bunkhouse_variable = None
team_variable = None

def get_all_campers_names():
    names = []
    for camper_id in Camper.get_all_ids():
        current_camper = Camper(camper_id[0])
        data = current_camper.select_camper()
        name = data[0] + " " + data[1]
        names.append(name)
    return names


def check_in_bt_handler():

    try:
        camper_id = int(camper_id_tb.get())
        #camp_id = int(camp_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="camper and camp id must be nubmers")
        return
    checked_in_camper = Camper(camper_id)
    #checked_in_camp = Camp(camp_id)
    if checked_in_camper.select_camper() == None:
        tkMessageBox.showinfo(title="message",message="camper not found")
        return
    # if checked_in_camp.select_camp() == None:
    #     tkMessageBox.showinfo(title="message",message="camp not found")
    #     return
    #check if this camper is regestered in this camp
    data = Bunkhouse.select_camp_team_bunkhouse(camper_id)
    # if not str(camp_id) in data[0]:
    #     tkMessageBox.showinfo(title="message",message="Sorry, You need to register in this camp before Check-in.")
    #     return
    #########################################################################
    str_buffer = ""
    if slepping_bag_CheckVar.get() == 0:
        str_buffer += "Slepping Bag, "
    if pillow_CheckVar.get() == 0:
        str_buffer += "Pillow, "
    if blanket_CheckVar.get() == 0:
        str_buffer += "Blanket, "
    if spray_CheckVar.get() == 0:
        str_buffer += "Insect Repellent Spray, "
    if bathing_suit_CheckVar.get() == 0:
        str_buffer += "Bathing Suit, "
    if sun_block_CheckVar.get() == 0:
        str_buffer += "Sun Blocking Lotion, "
    if rain_coat_CheckVar.get() == 0:
        str_buffer += "Raincoat, "
    if flashlight_CheckVar.get() == 0:
        str_buffer += "Flashlight, "
    if str_buffer != "":
        f = open("checkin.txt", 'w')
        f.write("Please bring in (" + str_buffer[:-2] + ")")
        f.close()

        webbrowser.open("checkin.txt")
        return
    ##################################################################################################
    camp_id = Bunkhouse.select_camp_team_bunkhouse(camper_id)[0][:-2]
    #check if this camper is already checked-in
    if Bunkhouse.already_checked_in(camp_id, camper_id):
        tkMessageBox.showinfo(title="message",message="You are already Checked in")
        return
    ###################################################################################################
    #If any check-in attempt is made after the camp start date 1:00 pm generate a text file saying sorry too late.

    now = datetime.now()
    checked_in_camp = Camp(camp_id)
    tmp_camp_data = checked_in_camp.select_camp()
    camp_start_date = date(int(tmp_camp_data[0].split("-")[0]), int(tmp_camp_data[0].split("-")[1]), int(tmp_camp_data[0].split("-")[2]))
    date_now = date(now.year, now.month, now.day)
    if (camp_start_date - date_now).days < 1:
        tkMessageBox.showinfo(title="message",message="Sorry, You checked_in too late")
        f1 = open("rejection check-in.txt", 'w')
        f1.write('Sorry too late')
        f1.close()
        webbrowser.open("rejection check-in.txt")
        return

    #Assigning to bunkhouses and tribes should occur only after check in

    checked_in_camper = Camper(camper_id)
    data_camper = checked_in_camper.select_camper()
    gender = data_camper[3]
    teams_ids = Team.get_available_team(camp_id)
    bunkhouses_ids = Bunkhouse.get_available_bunkgouses(gender, camp_id)
    ####################################################################################
    #option menus
    # campers_name_variable
    # bunkhouse_variable
    # tribe_variable
    print campers_name_variable.get()
    print bunkhouse_variable.get()
    print team_variable.get()
    if campers_name_variable.get() == "Select camper":
        bunkhouse_index = 0
        team_index = 0
    else:
        camper_id_selected = Camper.get_camper_id_by_name(campers_name_variable.get())[0]
        camper_bunkhouse_id = Camper.get_camper_bunkhouse(camper_id_selected)
        camper_team_id = Camper.get_camper_team(camper_id_selected)
        if bunkhouse_variable.get() == "default bunkhouse settings":
            bunkhouse_index = 0
        elif bunkhouse_variable.get() == "same bunkhouse":
            Bunkhouse.update_bunkhouse_options(camper_id, "Yes " + str(camper_id_selected))
            # if camper_bunkhouse_id is not None and camper_bunkhouse_id in bunkhouses_ids:
            #     bunkhouse_index = bunkhouses_ids.index(camper_bunkhouse_id)
            #     #same bunkhouse with camper_id_selected
            #     Bunkhouse.update_bunkhouse_options(camper_id, "Yes " + str(camper_id_selected))
            # else:
            #     tkMessageBox.showinfo(title="message",message="Camper selected is not checked in yet or his bunkhouse is Full")
            #     return
        else:#different bunkhouse
            Bunkhouse.update_bunkhouse_options(camper_id, "No " + str(camper_id_selected))
            # if camper_bunkhouse_id is not None:
            #     if camper_bunkhouse_id in bunkhouses_ids:
            #         bunkhouse_index = bunkhouses_ids.index(camper_bunkhouse_id) - 1
            #         #different bunkhouse not with camper_id_selected
            #         Bunkhouse.update_bunkhouse_options(camper_id, "No " + str(camper_id_selected))
            #     else:
            #         bunkhouse_index = 0
            # else:
            #     tkMessageBox.showinfo(title="message",message="Camper selected is not checked in yet")
            #     return
        if team_variable.get() == "default team settings":
            team_index = 0
        elif team_variable.get() == "same team":
            Team.update_team_options(camper_id, "Yes " + str(camper_id_selected))
            # if camper_team_id is not None and camper_team_id in teams_ids:
            #     team_index = teams_ids.index(camper_team_id)
            #     #same team with camper_id_selected
            #     Team.update_team_options(camper_id, "Yes " + str(camper_id_selected))
            # else:
            #     tkMessageBox.showinfo(title="message",message="Camper selected is not checked in yet or his team is Full")
            #     return
        else:#different tribe
            Team.update_team_options(camper_id, "No " + str(camper_id_selected))
            # if camper_team_id is not None :
            #     if camper_team_id in teams_ids:
            #         team_index = teams_ids.index(camper_team_id) - 1
            #         #different team not with camper_id_selected
            #         Team.update_team_options(camper_id, "No " + str(camper_id_selected))
            #     else:
            #         team_index = 0
            # else:
            #     tkMessageBox.showinfo(title="message",message="Camper selected is not checked in yet")
            #     return

    #########################################################################################
    # Bunkhouse.increment_checked_in(bunkhouses_ids[bunkhouse_index][0])
    # Team.increment_checked_in(teams_ids[team_index][0])
    #update a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
    # Bunkhouse.update_check_in(camper_id,camp_id,teams_ids[team_index][0],bunkhouses_ids[bunkhouse_index][0])

    Camp.camper_check_in(camper_id)
    tkMessageBox.showinfo(title="message", message="you have checked_in")
    cancel_check_in_bt_handler()


def cancel_check_in_bt_handler():
    top.destroy()

def slepping_bag_CheckButton_handler():
    global slepping_bag_CheckVar
    if slepping_bag_CheckVar.get() == 0:
        slepping_bag_CheckVar.set(1)
    else:
        slepping_bag_CheckVar.set(0)

def pillow_CheckButton_handler():
    global pillow_CheckVar
    if pillow_CheckVar.get() == 0:
        pillow_CheckVar.set(1)
    else:
        pillow_CheckVar.set(0)

def blanket_CheckButton_handler():
    global blanket_CheckVar
    if blanket_CheckVar.get() == 0:
        blanket_CheckVar.set(1)
    else:
        blanket_CheckVar.set(0)

def spray_CheckButton_handler():
    global spray_CheckVar
    if spray_CheckVar.get() == 0:
        spray_CheckVar.set(1)
    else:
        spray_CheckVar.set(0)

def bathing_suit_CheckButton_handler():
    global bathing_suit_CheckVar
    if bathing_suit_CheckVar.get() == 0:
        bathing_suit_CheckVar.set(1)
    else:
        bathing_suit_CheckVar.set(0)

def sun_block_CheckButton_handler():
    global sun_block_CheckVar
    if sun_block_CheckVar.get() == 0:
        sun_block_CheckVar.set(1)
    else:
        sun_block_CheckVar.set(0)

def rain_coat_CheckButton_handler():
    global rain_coat_CheckVar
    if rain_coat_CheckVar.get() == 0:
        rain_coat_CheckVar.set(1)
    else:
        rain_coat_CheckVar.set(0)

def flashlight_CheckButton_handler():
    global flashlight_CheckVar
    if flashlight_CheckVar.get() == 0:
        flashlight_CheckVar.set(1)
    else:
        flashlight_CheckVar.set(0)

def start_check_in_forum():
    global top, slepping_bag_CheckVar, pillow_CheckVar, blanket_CheckVar, spray_CheckVar, bathing_suit_CheckVar, sun_block_CheckVar, rain_coat_CheckVar, flashlight_CheckVar
    global camper_id_tb, camp_id_tb, campers_name_variable, bunkhouse_variable, team_variable

    top = Tk()
    top.title("Check-in Form")
    top.minsize(width=400, height=600)

    slepping_bag_CheckVar = IntVar()
    pillow_CheckVar = IntVar()
    blanket_CheckVar = IntVar()
    spray_CheckVar = IntVar()
    bathing_suit_CheckVar = IntVar()
    sun_block_CheckVar = IntVar()
    rain_coat_CheckVar = IntVar()
    flashlight_CheckVar = IntVar()

    slepping_bag_CheckButton = Checkbutton(top, text = "Slepping Bag", variable  = slepping_bag_CheckVar, height=2, width = 20, command = slepping_bag_CheckButton_handler)
    pillow_CheckButton = Checkbutton(top, text = "Pillow", variable = pillow_CheckVar, height=2, width = 20, command = pillow_CheckButton_handler)
    blanket_CheckButton = Checkbutton(top, text = "Blanket", variable = blanket_CheckVar, height=2, width = 20, command = blanket_CheckButton_handler)
    spray_CheckButton = Checkbutton(top, text = "Insect Repellent Spray", variable = spray_CheckVar, height=2, width = 20, command = spray_CheckButton_handler)
    bathing_suit_CheckButton = Checkbutton(top, text = "Bathing Suit", variable = bathing_suit_CheckVar, height=2, width = 20, command = bathing_suit_CheckButton_handler)
    sun_block_CheckButton = Checkbutton(top, text = "Sun Blocking Lotion", variable = sun_block_CheckVar, height=2, width = 20, command = sun_block_CheckButton_handler)
    rain_coat_CheckButton = Checkbutton(top, text = "Raincoat", variable = rain_coat_CheckVar, height=2, width = 20, command = rain_coat_CheckButton_handler)
    flashlight_CheckButton = Checkbutton(top, text = "Flashlight", variable = flashlight_CheckVar, height=2, width = 20, command = flashlight_CheckButton_handler)

    check_in_bt = Button(top, text="Check-in Camper", width=30, command = check_in_bt_handler)
    cancel_check_in_bt = Button(top, text="Cancel", width=30, command = cancel_check_in_bt_handler)


    camper_id_label = Label(top, text = "Enter camper ID")
    camper_id_tb = Entry(top, width=20)
    camp_id_label = Label(top, text = "Enter Camp ID")
    camp_id_tb = Entry(top, width=20)

    camper_id_label.pack()
    camper_id_tb.pack(expand=True)
    #option menus
    campers_name_variable = StringVar(top)
    campers_name_variable.set("Select camper") # default value
    campers_name_optionMenu = OptionMenu(top, campers_name_variable, "Select camper", *get_all_campers_names())
    campers_name_optionMenu.config(font=('calibri',(10)),bg='gray',width=24)
    campers_name_optionMenu['menu'].config(font=('calibri',(10)),bg='white')

    bunkhouse_variable = StringVar(top)
    bunkhouse_variable.set('default bunkhouse settings') # default value
    bunkhouse_optionMenu = OptionMenu(top, bunkhouse_variable, 'default bunkhouse settings', 'same bunkhouse', 'different bunkhouse')
    bunkhouse_optionMenu.config(font=('calibri',(10)),bg='gray',width=24)
    bunkhouse_optionMenu['menu'].config(font=('calibri',(10)),bg='white')

    team_variable = StringVar(top)
    team_variable.set('default team settings') # default value
    team_optionMenu = OptionMenu(top, team_variable, 'default team settings', 'same team', 'different team')
    team_optionMenu.config(font=('calibri',(10)),bg='gray',width=24)
    team_optionMenu['menu'].config(font=('calibri',(10)),bg='white')
    #####################################

    slepping_bag_CheckButton.pack(expand=True)
    pillow_CheckButton.pack(expand=True)
    blanket_CheckButton.pack(expand=True)
    spray_CheckButton.pack(expand=True)
    bathing_suit_CheckButton.pack(expand=True)
    sun_block_CheckButton.pack(expand=True)
    rain_coat_CheckButton.pack(expand=True)
    flashlight_CheckButton.pack(expand=True)

    campers_name_optionMenu.pack(expand=True)
    bunkhouse_optionMenu.pack(expand=True)
    team_optionMenu.pack(expand=True)

    check_in_bt.pack(expand=True)
    cancel_check_in_bt.pack(expand=True)


    top.grab_set()
    top.mainloop()
