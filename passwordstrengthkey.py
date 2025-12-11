from tkinter import *
import random
from PIL import Image, ImageTk

# create window
root = Tk()
root.title('Password Strength Key')
root.geometry('400x300')

frame = Frame(master=root, height=400, width=300, bg="#d0efff")

upload = Image.open('vector-login-and-sign-in-user-interface-business-website-modern-ui-template.jpg')
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

lbl1 = Label(frame, text="Enter your password to check it's strength", bg="#3895D3", fg='white', width=35)
pass_entry = Entry(frame)

def check():
    num = False
    cap_alpha = False
    low_alpha = False
    special_char = False

    password = pass_entry.get()
    legth_entry = len(password)

    for ch in password:
        if ch in "0123456789":
            num = True
        elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            cap_alpha = True
        elif ch in "abcdefghijklmnopqrstuvwxyz":
            low_alpha = True
        elif ch in "!@#$%^&*()-_=+-*/:;/.,<>":
            special_char = True

    if num and cap_alpha and low_alpha and special_char and legth_entry >= 9:
        result = Label(root,text='Strong password✅', fg="green")
        result.pack()
    else:
        result = Label(root,text='Weak password❌', fg="red")
        result.pack()
    root.after(2000,result.destroy)

btn = Button(root,text='Check',command=check,bg='brown',fg='white')
frame.place(x=60,y=0)
lbl1.place(x=20,y=30)
pass_entry.place(x=70,y=70)
btn.place(x=165,y=110)

root.mainloop()