#implement treeview to view data
#view payments for a specific camper(identified by first and last name)(2 Entries)

##select Payments.payment_id, Payments.application_mail_date, Payments.paid, Payments.payment_status,Camps.start_date,Camps.end_date
##from Payments, Campers, Camps
##where Payments.camp_id = Camps.camp_id and Campers.camper_id = Payments.camper_id and Campers.first_name = "name" and Campers.last_name = "name"
from Tkinter import *
from ttk import Treeview
from controller.payment import Payment
from controller.camp import Camp

root = None

def exit_browse_payment_bt_handler():
    global root
    #root.grab_release()
    root.destroy()


def start_browse_payments():
    global root
    root = Tk()
    root.title("Browse Payments")
    root.minsize(width=600, height=500)

    browse_payments_tree = Treeview(root)
    browse_payments_tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8")
    browse_payments_tree.column("1", width=100)
    browse_payments_tree.column("2", width=100)
    browse_payments_tree.column("3", width=100)
    browse_payments_tree.column("4", width=100)
    browse_payments_tree.column("5", width=100)
    browse_payments_tree.column("6", width=100)
    browse_payments_tree.column("7", width=100)
    browse_payments_tree.column("8", width=100)
    browse_payments_tree.heading("1", text="Payment ID")
    browse_payments_tree.heading("2", text="Camper ID")
    browse_payments_tree.heading("3", text="Camp ID")
    browse_payments_tree.heading("4", text="Date of Payment")
    browse_payments_tree.heading("5", text="Amount Paid")
    browse_payments_tree.heading("6", text="Camp Start Date")
    browse_payments_tree.heading("7", text="Payment Status")
    browse_payments_tree.heading("8", text="Amount Refunded")

    index = 0
    for payment_id in Payment.get_all_ids():
        current_payment = Payment(payment_id[0])
        data = current_payment.select_payment()
        mycamp = Camp(data[1])
        camp_start = mycamp.select_camp()[0]
        browse_payments_tree.insert('', index, text= "row" + str(index + 1), values = (payment_id, data[0], data[1], data[2], data[3], camp_start, data[4], data[5]))
        index += 1

    browse_payments_tree.pack()

    exit_payments_camp_bt = Button(root, text="Exit", width=30, command = exit_browse_payment_bt_handler)
    exit_payments_camp_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
