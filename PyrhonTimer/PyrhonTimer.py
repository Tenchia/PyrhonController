import os
from tkinter import *
from tkinter import messagebox
from datetime import *
import win10toast as w10t

toaster = w10t.ToastNotifier()

##############################################################
root = Tk()
root.title("Power OS")
root.geometry("400x300")

type = IntVar()
timeout = StringVar()

Label1 = Label(text="Enter timeout value:")
Label1.pack()
Label1.place(x=0,y=0)

Label2 = Label(text="Test button:")
Label2.pack()
Label2.place(x=0,y=50)

timeout_entry = Entry(textvariable=timeout)
timeout_entry.place(x=120,y=0)

hour_checkbutton = Radiobutton(text = "Hours", value=1, variable=type)
hour_checkbutton.pack()
hour_checkbutton.place(x=120, y=160)

minute_checkbutton = Radiobutton(text = "Minutes", value=2, variable=type)
minute_checkbutton.pack()
minute_checkbutton.place(x=120, y=190)

seconds_checkbutton = Radiobutton(text = "Seconds", value=3, variable=type)
seconds_checkbutton.pack()
seconds_checkbutton.place(x=120, y=220)


def show_message():
    messagebox.showinfo("GUI Python", timeout.get())

def click_button():
    os.system("shutdown /s /t " + str(timeout.get()))
    toaster.show_toast("Shutdown", "Your system will be shut down in few minutes.", duration = 10, threaded = True)
def click_button1():
    os.system("shutdown /r /t " + str(timeout.get()))
    toaster.show_toast("Reboot", "Your system will be rebooted in few minutes.", duration = 10, threaded = True)
def click_button2():
    os.system("shutdown /h")
    toaster.show_toast("Sleep mode", "Your system will run sleep mode in few minutes.", duration = 10, threaded = True)
def click_button3():
    os.system("shutdown /a")
    toaster.show_toast("Decline", "You have declined operation.", duration = 10, threaded = True)

message_button = Button(text="Click Me", command=show_message)
message_button.pack()
message_button.place(x=70,y=50)

btn = Button(text="Shutdown", command=click_button)
btn.pack()
btn.place(x=20, y=160)

btn1 = Button(text="Reboot", command=click_button1)
btn1.pack()
btn1.place(x=20, y=190)

btn2 = Button(text="Sleep mode", command=click_button2)
btn2.pack()
btn2.place(x=20, y=220)

btn3 = Button(text="Decline", command=click_button3)
btn3.pack()
btn3.place(x=20, y=250)

root.mainloop()

##############################################################