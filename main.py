from twilio.rest import Client #pip install twilio
from tkinter import *
from tkinter import messagebox
import random

# Creating GUI
root = Tk()
root.title("OTP Verification System")
root.geometry("300x200")

# Generating OTP
otp = random.randint(1000, 10000)
otp = str(otp)

label = Label(root, text="Enter your mobile number with country code",  font=("Montserrat", 9, 'bold')).place(x=10, y=5)
x = StringVar()
entry = Entry(root, textvariable=x).place(x=10, y=30, height=30, width=250)
button = Button(root, text="Send OTP", font=("Montserrat", 9, 'bold'), command=lambda:sms()).place(x=10, y=70)

# Creating function for sending SMS
def sms():
    phone = x.get()
    client = Client("AC665cfce2bab08f04c8157c44add85e6c", "3189f11fba9e1f8ce5468c0b60a747d0")
    client.messages.create(from_="+12023352003", to=phone,
                                     body="Your One Time Password to login is "+otp)
    messagebox.showinfo("OTP Verification System", "OTP sent!!")
    root.destroy()
    # New window
    win = Tk()
    win.title("OTP Verification System")
    win.geometry("300x200")

    lbl = Label(win, text="Enter the OTP sent to your mobile number",  font=("Montserrat", 9, 'bold')).place(x=10, y=5)
    y = StringVar()
    ENtry = Entry(win, textvariable=y).place(x=20, y=30,  height=30, width=250)
    btn = Button(win, text="Login", font=("Montserrat", 9, 'bold'), command=lambda:login()).place(x=10, y=70)

    # Creating function for login
    def login():
        messagebox.showinfo("OTP Verification System", "Login Successful")
        win.destroy()

root.mainloop()
