from Tkinter import *
import datetime
from controller.payment import Payment
import tkMessageBox


root = None
camper_id_tb = None
camp_id_tb = None
payment_date_tb = None
paid_tb = None

def is_valid_date(s):
    """
    take a string and check if this string follows this format(YYYY-MM-DD) or not, return bool
    """
    lst = s.split("-")
    if len(lst) != 3 or len(lst[0]) != 4 or len(lst[1]) != 2 or len(lst[2]) != 2:
        return False
    try:
        year = int(lst[0])
        month = int(lst[1])
        day = int(lst[2])
    except:
        return False
    return True

def get_today_date():
    """
    returns the date of today in format (YYYY-MM-DD)
    """
    now = datetime.datetime.now()
    return str(now.year) + "-" + str(now.month) + "-" + str(now.day)

def cancel_payment_bt_handler():
        root.destroy()

def submit_payment_handler():
    try:
        x = int(camper_id_tb.get())
        y = int(camp_id_tb.get())
        z = float(paid_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="wrong camper id, camp id or paid amount")
        return
    if not is_valid_date(payment_date_tb.get()):
        tkMessageBox.showinfo(title="message",message="wrong payment date")
        return
    myPayment = Payment(0, camper_id_tb.get(), camp_id_tb.get(), payment_date_tb.get(), paid_tb.get())
    myPayment.insert_payment()
    tkMessageBox.showinfo(title="message",message="record inserted")
    cancel_payment_bt_handler()


def start_payments_forum():
    global root, camper_id_tb, camp_id_tb, payment_date_tb, paid_tb
    root = Tk()
    root.title("Add Payment")
    root.minsize(width=400, height=300)
    camper_id_label = Label(root, text = "camper ID")
    camper_id_label.pack()
    camper_id_tb = Entry(root, width=20)
    camper_id_tb.pack(expand=True)
    camp_id_label = Label(root, text = "Camp ID")
    camp_id_label.pack()
    camp_id_tb = Entry(root, width=20)
    camp_id_tb.pack(expand=True)
    payment_date_label = Label(root, text = "Date format(YYYY-MM-DD)")
    payment_date_label.pack()
    payment_date_tb = Entry(root, width=20)
    payment_date_tb.insert(END, get_today_date())
    payment_date_tb.pack(expand=True)
    paid_label = Label(root, text = "Paid money in USD")
    paid_label.pack()
    paid_tb = Entry(root, width=20)
    paid_tb.insert(END, "1000")
    paid_tb.pack(expand=True)
    submit_payment = Button(root, text="submit", width=30, command = submit_payment_handler)
    submit_payment.pack(expand=True)
    cancel_payment_bt = Button(root, text="Cancel", width=30, command = cancel_payment_bt_handler)
    cancel_payment_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
