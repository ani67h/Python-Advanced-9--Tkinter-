# import necessary libraries
from tkinter import * 

# create window
root = Tk()
root.title('Login App')
root.geometry('500x400')

# create a frame to organise elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# add widgets
# add label
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email ID", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)

# use entry widget to create a text box for user to enter deatils
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# function to display message
def display():
    name = name_entry.get()
    greet = "Hey " + name
    message = "\nCongratulations, we have successfully hacked your account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

# textbox to display messaeg
textbox = Text(bg="#BEBEBE", fg="black")

# add button, when pressed, messgae will be displayed
btn = Button(text="Create Account", command=display, bg="red")

# arrange all widgets
frame.place(x=60, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()