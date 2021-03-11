import os
from tkinter import *
import win10toast as w10t

toaster = w10t.ToastNotifier()

##############################################################
def click_button(event):
    os.system("shutdown /s")
    toaster.show_toast("Shutdown", "Your system will be shut down in few minutes.", duration = 10, threaded = True)
def click_button1():
    os.system("shutdown /r")
    toaster.show_toast("Reboot", "Your system will be rebooted in few minutes.", duration = 10, threaded = True)
def click_button2():
    os.system("shutdown /h")
    toaster.show_toast("Sleep mode", "Your system will run sleep mode in few minutes.", duration = 10, threaded = True)
def click_button3():
    os.system("shutdown /a")
    toaster.show_toast("Decline", "You have declined operation.", duration = 10, threaded = True)

root = Tk()
root.title("Power OS")
root.geometry("400x300")


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