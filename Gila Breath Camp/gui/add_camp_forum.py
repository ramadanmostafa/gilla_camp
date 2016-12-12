from Tkinter import *
from controller.camp import Camp
import tkMessageBox
from datetime import date, datetime

root = None
start_date_label = None
start_date_tb = None
end_date_label = None
end_date_tb = None
bunk_houses_num_label = None
bunk_houses_num_tb = None
teams_num_label = None
teams_num_tb = None
global_camp_id = 0
cost_label = None
cost_tb = None


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

def validate_end_date_higher_than_start_date(start_date, end_date):
    start_date_lst = start_date.split('-')
    end_date_lst = end_date.split('-')
    start = date(int(start_date_lst[0]), int(start_date_lst[1]), int(start_date_lst[2]))
    end = date(int(end_date_lst[0]), int(end_date_lst[1]), int(end_date_lst[2]))

    return (end - start).days > 0



def update_camp_handler():
    if not is_valid_date(start_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong start date.")
        return
    if not is_valid_date(end_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong end date.")
        return
    
    if not validate_end_date_higher_than_start_date(start_date_tb.get(), end_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="start date can't be higher than end date.")
        return
    
    try:
        x = int(bunk_houses_num_tb.get())
        y = int(teams_num_tb.get())
        z = float(cost_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="wrong number(bunkhouse, team or cost)")
        return
    else:
        tmp_camp = Camp(global_camp_id, start_date_tb.get(), end_date_tb.get(), bunk_houses_num_tb.get(), teams_num_tb.get(), cost_tb.get())
        bunk_houses_num_old, teams_num_old = tmp_camp.get_camp_num_bunkhouse_team()
        tmp_camp.update_camp()
        tkMessageBox.showinfo(title="message",message="record updated")
        cancel_camp_bt_handler()

def submit_camp_handler():
    if not is_valid_date(start_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong start date.")
        return
    if not is_valid_date(end_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong end date.")
        return
    
    if not validate_end_date_higher_than_start_date(start_date_tb.get(), end_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="start date can't be higher than end date.")
        return
    
    try:
        bunk_houses_num = int(bunk_houses_num_tb.get())
        teams_num = int(teams_num_tb.get())
        cost = float(cost_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="wrong number(bunkhouse, team or cost)")
        return
    else:
        tmp_camp = Camp(0, start_date_tb.get(), end_date_tb.get(), bunk_houses_num, teams_num, cost)
        tmp_camp.insert_camp()
        camp_id = tmp_camp.get_camp_id()[0]
        from controller.bunkhouse import Bunkhouse
        for i in range(bunk_houses_num):
            if i % 2 == 0:
                b = Bunkhouse("Male", camp_id)
            else:
                b = Bunkhouse("Female", camp_id)
            b.insert_bunkhouse()

        from controller.team import Team
        for i in range(teams_num):
            team_name = "camp_" + str(camp_id) + "team" + str(i)
            t = Team(camp_id, team_name)
            t.insert_team()
        tkMessageBox.showinfo(title="message",message="record inserted")
        cancel_camp_bt_handler()

def cancel_camp_bt_handler():
    global root
    #root.grab_release()
    root.destroy()

def start_add_camp_forum():
    global root
    init_add_camp_forum()
    pack_elements()
    submit_camp = Button(root, text="submit", width=30, command = submit_camp_handler)
    submit_camp.pack(expand=True)
    cancel_camp_bt = Button(root, text="Cancel", width=30, command = cancel_camp_bt_handler)
    cancel_camp_bt.pack(expand=True)
    root.mainloop()

def init_add_camp_forum():
    global root, start_date_label, start_date_tb, end_date_label, end_date_tb, bunk_houses_num_label, bunk_houses_num_tb, teams_num_label, teams_num_tb
    global cost_label, cost_tb
    root = Tk()
    root.title("Add Camp Form")
    root.minsize(width=400, height=300)
    start_date_label = Label(root, text = "Start Date format(YYYY-MM-DD)")
    start_date_tb = Entry(root, width=20)
    end_date_label = Label(root, text = "End Date format(YYYY-MM-DD)")
    end_date_tb = Entry(root, width=20)
    cost_label = Label(root, text = "Cost in USD")
    cost_tb = Entry(root, width=20)
    cost_tb.delete(0,END)
    cost_tb.insert(0, "1000.0")
    bunk_houses_num_label = Label(root, text = "Number of Bunck Houses")
    bunk_houses_num_tb = Entry(root, width=20)
    bunk_houses_num_tb.insert(END, "6")
    teams_num_label = Label(root, text = "Number of Teams")
    teams_num_tb = Entry(root, width=20)
    teams_num_tb.insert(END, "4")

def pack_elements():
    start_date_label.pack()
    start_date_tb.pack(expand=True)
    end_date_label.pack()
    end_date_tb.pack(expand=True)
    cost_label.pack()
    cost_tb.pack(expand=True)
    bunk_houses_num_label.pack()
    bunk_houses_num_tb.pack(expand=True)
    teams_num_label.pack()
    teams_num_tb.pack(expand=True)

def update_camp_forum(camp_id):
    global root, start_date_tb, end_date_tb, bunk_houses_num_tb, teams_num_tb, global_camp_id, cost_tb
    global_camp_id = camp_id
    current_camp = Camp(camp_id)
    data = current_camp.select_camp()
    init_add_camp_forum()
    start_date_tb.delete(0,END)
    start_date_tb.insert(0, data[0])
    end_date_tb.delete(0,END)
    end_date_tb.insert(0, data[1])
    bunk_houses_num_tb.delete(0,END)
    bunk_houses_num_tb.insert(0, data[2])
    teams_num_tb.delete(0,END)
    teams_num_tb.insert(0, data[3])
    cost_tb.delete(0,END)
    cost_tb.insert(0, data[4])
    pack_elements()
    update_camp = Button(root, text="Update", width=30, command = update_camp_handler)
    update_camp.pack(expand=True)
    cancel_camp_bt = Button(root, text="Cancel", width=30, command = cancel_camp_bt_handler)
    cancel_camp_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
