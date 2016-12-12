from Tkinter import *
import tkMessageBox
import webbrowser
from datetime import date, datetime
from controller.camper import Camper
from controller.camp import Camp
from controller.bunkhouse import Bunkhouse
from controller.team import Team
from controller.payment import Payment


root = None
name1_label = None
name1_tb = None
name2_label = None
name2_tb = None
date_of_birth_label = None
date_of_birth_tb = None
gender_label = None
gender_lb = None
address_label = None
address_lb = None
camper_id_global = 0
guardian_name_lb = None
guardian_name_tb = None
choose_camp_label = None
choose_camp_listbox = None

def is_valid_date(s):
    """
    take a string and check if this string follows this format(YYYY-MM-DD) or not, return bool
    """
    lst = s.split("-")
    if len(lst) != 3 or len(lst[0]) != 4 or len(lst[1]) > 2 or len(lst[1]) < 1 or len(lst[2]) > 2 or len(lst[2]) < 1:
        return False
    try:
        year = int(lst[0])
        month = int(lst[1])
        day = int(lst[2])
    except:
        return False
    if month < 1 or month > 12 or day < 1 or day > 31:
        return False
    return True

def validate_age_9_18(birth_date):
    tmp_lst = birth_date.split('-')
    date_of_birth = date(int(tmp_lst[0]), int(tmp_lst[1]), int(tmp_lst[2]))
    now = datetime.now()
    date_now = date(now.year, now.month, now.day)
    camper_age = (date_now - date_of_birth).days / 365
    return camper_age > 9 and camper_age < 18

def update_camper_bt_handler():
    try:
        x = gender_lb.get(gender_lb.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="Gender is required.")
        return
    try:
        x = choose_camp_listbox.get(choose_camp_listbox.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="You must choose a camp.")
        return

    if name1_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="First Name is required.")
    elif name2_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Last Name is required.")
    elif address_lb.get() == '':
        tkMessageBox.showinfo(title="message",message="Address is required.")
    elif gender_lb.get(gender_lb.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="Gender is required.")
    elif not is_valid_date(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong date of birth.")
    elif not validate_age_9_18(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="Camper age must be between 9-18")
    elif choose_camp_listbox.get(choose_camp_listbox.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="You must choose a camp")
    elif guardian_name_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Guardian Name is required.")
    else:
        tmp_camper = Camper(camper_id_global, name1_tb.get(), name2_tb.get(), date_of_birth_tb.get(), gender_lb.get(gender_lb.curselection()), address_lb.get())

        tmp_camper = Camper(camper_id_global, name1_tb.get(), name2_tb.get(), date_of_birth_tb.get(), gender_lb.get(gender_lb.curselection()), address_lb.get(), guardian_name_tb.get())
        tmp_camper.update_camper()
        camper_id = camper_id_global
        ############################################################
        camp_selected = choose_camp_listbox.get(choose_camp_listbox.curselection()).split(' ')[0]
        all_camps = Camp.get_all_ids()
        try:
            if camp_selected == "1st":
                camp_id = all_camps[0][0]
            elif camp_selected == "2nd":
                camp_id = all_camps[1][0]
            elif camp_selected == "3rd":
                camp_id = all_camps[2][0]
        except:
            tkMessageBox.showinfo(title="message",message="camp Not found")
            return
        ##############################################################################################
        Camper.unregister_camper(camper_id)

        checked_in_camper = Camper(camper_id)
        checked_in_camp = Camp(camp_id)
        tmp_camp_data = checked_in_camp.select_camp()
        if tmp_camp_data == None:
            tkMessageBox.showinfo(title="message",message="camp not found")
            return
        #check if there's a room for this camper in bunkhouse with notice to gender
        data_camper = checked_in_camper.select_camper()
        gender = data_camper[3]
        bunkhouses_ids = Bunkhouse.get_available_bunkgouses(gender, camp_id)
        if len(bunkhouses_ids) < 1:
            tkMessageBox.showinfo(title="message",message="Sorry, This camp is not available, Choose another one")
            return
        #check if this camper is already registered in this camp
        data_camp = Bunkhouse.select_camp_team_bunkhouse(camper_id)
        if str(camp_id) in data_camp[0]:
            tkMessageBox.showinfo(title="message",message="Sorry, This camper is already registered in this camp")
            return
        teams_ids = Team.get_available_team(camp_id)
        #assign this camper to a team and a bunkhouse and get their ids(inc checked_in_num)
        # Bunkhouse.increment_checked_in(bunkhouses_ids[0][0])
        # Team.increment_checked_in(teams_ids[0][0])
        Camp.increment_registered(camp_id)
        #insert a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
        Bunkhouse.insert_check_in(camper_id,camp_id)#,teams_ids[0][0],bunkhouses_ids[0][0])
        #show a message box saying, the camper checked in successfully
        #tkMessageBox.showinfo(title="message",message="Camper Added successfully")
        ##############################################################################################
        tkMessageBox.showinfo(title="message",message="record updated")
        cancel_camper_bt_handler()

def cancel_camper_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

def submit_camper_bt_handler():
    try:
        x = gender_lb.get(gender_lb.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="Gender is required.")
        return
    try:
        x = choose_camp_listbox.get(choose_camp_listbox.curselection())
    except:
        tkMessageBox.showinfo(title="message",message="You must choose a camp.")
        return

    if name1_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="First Name is required.")
    elif name2_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Last Name is required.")
    elif address_lb.get() == '':
        tkMessageBox.showinfo(title="message",message="Address is required.")
    elif gender_lb.get(gender_lb.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="Gender is required.")
    elif not is_valid_date(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong date of birth.")
    elif not validate_age_9_18(date_of_birth_tb.get()):
        tkMessageBox.showinfo(title="message",message="Camper age must be between 9-18")
        f1 = open("rejection letter.txt", 'w')
        f1.write('Sorry your application was rejected.\n\nReason: Camper age must be between 9-18')
        f1.close()
        webbrowser.open("rejection letter.txt")
        return
    elif choose_camp_listbox.get(choose_camp_listbox.curselection()) == '':
        tkMessageBox.showinfo(title="message",message="You must choose a camp")
    elif guardian_name_tb.get() == '':
        tkMessageBox.showinfo(title="message",message="Guardian Name is required.")
    else:
        tmp_camper = Camper(0, name1_tb.get(), name2_tb.get(), date_of_birth_tb.get(), gender_lb.get(gender_lb.curselection()), address_lb.get(), guardian_name_tb.get())
        camper_id = tmp_camper.insert_camper()
        ############################################################
        camp_selected = choose_camp_listbox.get(choose_camp_listbox.curselection())[0]
        all_camps = Camp.get_all_ids()
        try:
            camp_id = all_camps[int(camp_selected) - 1][0]
        except:
            tkMessageBox.showinfo(title="message",message="camp Not found")
            return

        checked_in_camper = Camper(camper_id)
        checked_in_camp = Camp(camp_id)
        tmp_camp_data = checked_in_camp.select_camp()
        if tmp_camp_data == None:
            tkMessageBox.showinfo(title="message",message="camp not found")
            return
        #check if there's a room for this camper in bunkhouse with regard to gender
        data_camper = checked_in_camper.select_camper()
        gender = data_camper[3]
        bunkhouses_ids = Bunkhouse.get_available_bunkgouses(gender, camp_id)
        if len(bunkhouses_ids) < 1:
            tkMessageBox.showinfo(title="message",message="Sorry, This camp is not available, Choose another one")
            return
        #check if this camper is already registered in this camp
        data_camp = Bunkhouse.select_camp_team_bunkhouse(camper_id)
        if str(camp_id) in data_camp[0]:
            tkMessageBox.showinfo(title="message",message="Sorry, This camper is already registered in this camp")
            return
        #rejection letter check
        #########################################################################################################
        now = datetime.now()
        camp_start_date = date(int(tmp_camp_data[0].split("-")[0]), int(tmp_camp_data[0].split("-")[1]), int(tmp_camp_data[0].split("-")[2]))
        camp_end_date = date(int(tmp_camp_data[1].split("-")[0]), int(tmp_camp_data[1].split("-")[1]), int(tmp_camp_data[1].split("-")[2]))
        date_now = date(now.year, now.month, now.day)
        if (camp_start_date - date_now).days / 30.0 > 8:
            tkMessageBox.showinfo(title="message",message="Sorry, You applied too early")
            f1 = open("rejection letter.txt", 'w')
            f1.write('Sorry your application was rejected.\n\nReason: You applied too early')
            f1.close()
            webbrowser.open("rejection letter.txt")
            return
        elif (camp_start_date - date_now).days / 30.0 < 2:
            tkMessageBox.showinfo(title="message",message="Sorry, You applied too late")
            f1 = open("rejection letter.txt", 'w')
            f1.write('Sorry your application was rejected.\n\nReason: You applied too late')
            f1.close()
            webbrowser.open("rejection letter.txt")
            return
        #########################################################################################################
        teams_ids = Team.get_available_team(camp_id)
        #assign this camper to a tribe and a bunkhouse and get their ids(inc checked_in_num)
        #Bunkhouse.increment_checked_in(bunkhouses_ids[0][0])
        #########################################################################################################################
        #should be deleted
        # Team.increment_checked_in(teams_ids[0][0])
        # Camp.increment_registered(camp_id)
        #########################################################################################################################
        #insert a record in Camper_Camp_BunckHouse_Team(camper_id,camp_id,team_id,bunk_house_id,student_checked_in)
        #Bunkhouse.insert_check_in(camper_id,camp_id,teams_ids[0][0],bunkhouses_ids[0][0])
        Bunkhouse.insert_check_in(camper_id,camp_id)
        #update camps.campers_registered_count
        Camp.increment_registered(camp_id)
        #show a message box saying, the camper added in successfully
        tkMessageBox.showinfo(title="message",message="Camper added successfully")
        

        mailing_date = str(datetime.now().date())
        first_name = data_camper[0]
        last_name = data_camper[1]
        address = data_camper[4]
        camp_start_date = tmp_camp_data[0]
        camp_end_date = tmp_camp_data[1]
        f1 = open("Mailing Label.txt", 'w')
        f1.write(mailing_date + "\n" + first_name + ' ' + last_name + "\n" + address)
        f1.close()

        webbrowser.open("Mailing Label.txt")

        #get payment status for camp_id and camper_id
        data_payment = Payment.get_payment_status_by_camp_camper_id(camper_id, camp_id)
        if data_payment == None:
            payment_status = "Not Paid"
            amount_paid = 0
        else:
            payment_status = data_payment[0]
            amount_paid = data_payment[1]

        if payment_status == "Fully Paid":
            thanks = ".\nThank you for your payment"
        else:
            thanks = ".\nPlease bring the amount of $%s" % str(1000 - int(amount_paid))
        f2 = open("acceptance letter.txt", 'w')

        f2.write("Congratulations " + first_name + ' ' + last_name +"! you have been accepted for the camp starting on " + camp_start_date + " and ending on " + camp_end_date + thanks)
        f2.close()
        webbrowser.open("acceptance letter.txt")

        ########################################################################

        cancel_camper_bt_handler()

def init_camper_forum():
    global root, name1_label, name1_tb, name2_label, name2_tb, date_of_birth_label, date_of_birth_tb, gender_label, gender_lb, address_lb, address_label
    global guardian_name_lb, guardian_name_tb,choose_camp_label, choose_camp_listbox
    root = Tk()
    root.title("Add Camper")
    root.minsize(width=600, height=600)
    name1_label = Label(root, text = "First Name")
    name1_tb = Entry(root, width=20)
    name2_label = Label(root, text = "Last Name")
    name2_tb = Entry(root, width=20)
    date_of_birth_label = Label(root, text = "Date of Birth format(YYYY-MM-DD)")
    date_of_birth_tb = Entry(root, width=20)
    gender_label = Label(root, text = "Gender")
    gender_lb = Listbox(root, height=2, width=10, exportselection = 0)
    address_label = Label(root, text = "Address")
    address_lb = Entry(root, width=20)
    gender_lb.insert(1, "Male")
    gender_lb.insert(2, "Female")
    guardian_name_lb = Label(root, text = "Guardian Name")
    guardian_name_tb = Entry(root, width=20)
    #########################################################################################
    camps_data = []
    for camp_id in Camp.get_all_ids():
        current_camp = Camp(camp_id[0])
        #select start_date, end_date, bunkhouses_number, tribes_numbers, cost, campers_registered_count, max_capacity
        camps_data.append(current_camp.select_camp())
    choose_camp_label = Label(root, text = "Choose Camp")
    choose_camp_listbox = Listbox(root, height=len(camps_data), width=50, exportselection = 0)
    index = 1
    for camp_data in camps_data:
        capacity = str(camp_data[5]) + '/' + str(camp_data[6])
        if index == 1:
            camp_index = str(index) + "st Camp: "
        elif index == 2:
            camp_index = str(index) + "nd Camp: "
        elif index == 3:
            camp_index = str(index) + "rd Camp: "
        else:
            camp_index = str(index) + "th Camp: "
        choose_camp_listbox.insert(index, camp_index + camp_data[0] + " - " + camp_data[1] + " (" + capacity +")")
        index += 1




def pack_elements():
    name1_label.pack()
    name1_tb.pack(expand=True)
    name2_label.pack()
    name2_tb.pack(expand=True)
    date_of_birth_label.pack()
    date_of_birth_tb.pack(expand=True)
    gender_label.pack()
    gender_lb.pack(expand=True)
    address_label.pack()
    address_lb.pack(expand=True)
    guardian_name_lb.pack()
    guardian_name_tb.pack(expand=True)
    choose_camp_label.pack()
    choose_camp_listbox.pack(expand=True)


def start_camper_forum():
    global root
    init_camper_forum()
    pack_elements()
    submit_camper = Button(root, text="submit", width=30, command = submit_camper_bt_handler)
    submit_camper.pack(expand=True)
    cancel_camper_bt = Button(root, text="Cancel", width=30, command = cancel_camper_bt_handler)
    cancel_camper_bt.pack(expand=True)
    root.mainloop()

def update_camper(camper_id):
    global root
    global name1_tb
    global name2_tb
    global date_of_birth_tb
    global gender_lb
    global camper_id_global, address_lb, guardian_name_tb
    camper_id_global = camper_id
    current_camper = Camper(camper_id)
    data = current_camper.select_camper()
    if data == None:
        tkMessageBox.showinfo(title="message",message="Camper Not Found")
        return
    init_camper_forum()
    #init text boxes with data
    name1_tb.delete(0,END)
    name1_tb.insert(0, data[0])
    name2_tb.delete(0,END)
    name2_tb.insert(0, data[1])
    date_of_birth_tb.delete(0,END)
    date_of_birth_tb.insert(0, data[2])
    tmp = 0
    if data[3] == "Female":
        tmp =  1
    gender_lb.select_set(tmp)
    address_lb.delete(0,END)
    address_lb.insert(0, data[4])
    guardian_name_tb.delete(0,END)
    guardian_name_tb.insert(0, data[5])
    pack_elements()
    submit_camper = Button(root, text="update", width=30, command = update_camper_bt_handler)
    submit_camper.pack(expand=True)
    cancel_camper_bt = Button(root, text="Cancel", width=30, command = cancel_camper_bt_handler)
    cancel_camper_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
