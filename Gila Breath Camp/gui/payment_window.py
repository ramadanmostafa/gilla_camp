from Tkinter import *
import tkMessageBox

root = None
payment_id_tb = None

def cancel_main_bt_handler():
    root.grab_release()
    root.destroy()

def browse_payment_bt_handler():
    from browse_payments import start_browse_payments
    root.grab_release()
    start_browse_payments()

def add_payment_bt_handler():
    from payments_forum import start_payments_forum
    root.grab_release()
    start_payments_forum()

def req_cancel_payment_bt_handler():
    try:
        payment_id = int(payment_id_tb.get())
    except:
        tkMessageBox.showinfo(title="message",message="camp ID must be a number")
    else:
        from controller.payment import Payment
        from controller.camp import Camp
        from datetime import date
        myPayment = Payment(payment_id)
        data = myPayment.select_payment()
        camp_id = data[1]
        payment_date = data[2].split('-')
        amount_paid = data[3]
        myCamp = Camp(camp_id)
        data =  myCamp.select_camp()
        camp_start_date = data[0].split('-')
        delta = date(int(camp_start_date[0]), int(camp_start_date[1]), int(camp_start_date[2])) - date(int(payment_date[0]), int(payment_date[1]), int(payment_date[2]))
        if delta.days >= 42:
            #6weeks 90%
            amount_refund = .9 * amount_paid
        elif delta.days >= 21:
            #3weeks 45 %
            amount_refund = .45 * amount_paid
        else:
            #0%
            amount_refund = 0 * amount_paid

        myPayment.update_refund(amount_refund)
        tkMessageBox.showinfo(title="message",message="record Updated, amount_refund = " + str(amount_refund))
        cancel_main_bt_handler()

def start_payment_window():
    global root, payment_id_tb
    root = Tk()
    root.title("Payments")
    root.minsize(width=400, height=400)

    browse_payment_bt = Button(root, text="Browse Payments", width=30, command = browse_payment_bt_handler)
    browse_payment_bt.pack(expand=True)

    add_payment_bt = Button(root, text="ADD Payment", width=30, command = add_payment_bt_handler)
    add_payment_bt.pack(expand=True)

    payment_id_label = Label(root, text = "Enter Payment ID")
    payment_id_label.pack()

    payment_id_tb = Entry(root, width=20)
    payment_id_tb.pack(expand=True)

    req_cancel_payment_bt = Button(root, text="Requect Cancel Payment", width=30, command = req_cancel_payment_bt_handler)
    req_cancel_payment_bt.pack(expand=True)

    cancel_main_bt = Button(root, text="Cancel", width=30, command = cancel_main_bt_handler)
    cancel_main_bt.pack(expand=True)
    root.grab_set()
    root.mainloop()
