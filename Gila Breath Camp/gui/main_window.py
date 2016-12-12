from Tkinter import *
import tkMessageBox

root = None

def camper_window_bt_handler():
    from camper_window import start_camper_window
    root.grab_release()
    start_camper_window()

def camp_window_bt_handler():
    from camp_window import start_camp_window
    root.grab_release()
    start_camp_window()

def payment_window_bt_handler():
    from payment_window import start_payment_window
    root.grab_release()
    start_payment_window()

def check_in_bt_handler():
    from check_in_forum import start_check_in_forum
    root.grab_release()
    start_check_in_forum()

def bunkhouse_bt_handler():
    from gui.bunkhouse_forum import start_bunkhouse_forum
    root.grab_release()
    start_bunkhouse_forum()

def team_bt_handler():
    from gui.team_forum import start_team_forum
    root.grab_release()
    start_team_forum()

def modify_bunkhouse_team_capacity_handler():
    from modify_bunkhouse_team import modify_bunkhouse_team_start
    root.grab_release()
    modify_bunkhouse_team_start()

def assign_to_camp_bt_handler():
    from gui.assign_to_camp import start_assign_to_camp
    root.grab_release()
    start_assign_to_camp()

###################updated 11-10-2016
def query_bt_handler():
    from gui.query_browse import start_query_browse
    root.grab_release()
    start_query_browse()

def assign_team_bunkhouse_bt_handler():
    from gui.assign_team_bunkhouse_form import start_assign_team_bunkhouse_form
    root.grab_release()
    start_assign_team_bunkhouse_form()
####################################


def start_main_window():
    global root
    root = Tk()
    root.title("Main Window(Clerk)")
    root.minsize(width=400, height=500)

    ###################updated 11-10-2016
    query_bt = Button(root, text="Browse Camps, Bunkhouses and Tribes", width=30, command = query_bt_handler)
    query_bt.pack(expand=True)
    #########################################

    camper_window_bt = Button(root, text="Camper", width=30, command = camper_window_bt_handler)
    camper_window_bt.pack(expand=True)

    payment_window_bt = Button(root, text="Payments", width=30, command = payment_window_bt_handler)
    payment_window_bt.pack(expand=True)

    bunkhouse_bt = Button(root, text="Bunkhouses", width=30, command = bunkhouse_bt_handler)
    bunkhouse_bt.pack(expand=True)

    team_bt = Button(root, text="Tribes", width=30, command = team_bt_handler)
    team_bt.pack(expand=True)

    check_in_bt = Button(root, text="Check-in Form", width=30, command = check_in_bt_handler)
    check_in_bt.pack(expand=True)

    assign_team_bunkhouse_bt = Button(root, text="Assign To Teams And Bunkhouses", width=30, command = assign_team_bunkhouse_bt_handler)
    assign_team_bunkhouse_bt.pack(expand=True)

    exit_main_bt = Button(root, text="Exit", width=30, command = exit)
    exit_main_bt.pack(expand=True)

    root.grab_set()
    root.mainloop()

def start_main_window_admin():
    global root
    root = Tk()
    root.title("Main Window(Admin)")
    root.minsize(width=400, height=500)

    ###################updated 11-10-2016
    query_bt = Button(root, text="Browse Camps, Bunkhouses and Tribes", width=30, command = query_bt_handler)
    query_bt.pack(expand=True)
    #########################################

    camper_window_bt = Button(root, text="Camper", width=30, command = camper_window_bt_handler)
    camper_window_bt.pack(expand=True)

    camp_window_bt = Button(root, text="Camp", width=30, command = camp_window_bt_handler)
    camp_window_bt.pack(expand=True)

    payment_window_bt = Button(root, text="Payments", width=30, command = payment_window_bt_handler)
    payment_window_bt.pack(expand=True)

    bunkhouse_bt = Button(root, text="Bunkhouses", width=30, command = bunkhouse_bt_handler)
    bunkhouse_bt.pack(expand=True)

    team_bt = Button(root, text="Tribes", width=30, command = team_bt_handler)
    team_bt.pack(expand=True)

    check_in_bt = Button(root, text="Check-in Form", width=30, command = check_in_bt_handler)
    check_in_bt.pack(expand=True)

    assign_team_bunkhouse_bt = Button(root, text="Assign To Teams And Bunkhouses", width=30, command = assign_team_bunkhouse_bt_handler)
    assign_team_bunkhouse_bt.pack(expand=True)

    #label,entry,button,button
    modify_bunkhouse_team_capacity = Button(root, text="Modify Capacity", width=30, command = modify_bunkhouse_team_capacity_handler)
    modify_bunkhouse_team_capacity.pack(expand=True)

    exit_main_bt = Button(root, text="Exit", width=30, command = exit)
    exit_main_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
