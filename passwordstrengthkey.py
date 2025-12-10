from tkinter import *
import random
from PIL import Image, ImageTk

# create window
root = Tk()
root.title('Password Strength Key')
root.geometry('400x300')

frame = Frame(master=root, height=200, width=360, bg="#d0efff")

upload = Image.open('vector-login-and-sign-in-user-interface-business-website-modern-ui-template.jpg')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

lbl1 = Label(frame, text="Enter your password to check it's strength", bg="#3895D3", fg='white', width=12)
pass_entry = Entry(frame)
password = pass_entry.get()
legth_entry = len(password)

num = False
cap_alpha = False
low_alpha = False
special_char = False


if CHAR in "0123456789":
    num = True
elif "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    cap_alpha = True
elif "abcdefghijklmnopqrstuvwxyz":
    low_alpha = True
elif "!@#$%^&*()-_=+-*/:;/.,<>":
    special_char = True

if num and cap_alpha and low_alpha and special_char and legth_entry >= 9:
    print('Your password is very strong')

frame.place(x=60,y=0)
lbl1.place(x=20,y=20)
pass_entry.place(x=20,y=40)

root.mainloop()