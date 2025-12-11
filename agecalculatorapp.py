from tkinter import *
from datetime import datetime

window = Tk()
window.title('Age Calculator App')
window.geometry('500x400')

frame = Frame(master=window,height=500,width=400,bg="#d0efff")
lbl = Label(frame, text="Enter your date of birth to see your current age (dd/mm/yyyy) : ", bg="#3895D3", fg='white', width=50)
input = Entry(frame)
textbox = Text(frame, height=1, width=21)
textbox.pack(pady=10)

def age():
    birth = input.get()
    birth_date = datetime.strptime(birth, "%d/%m/%Y" )
    today = datetime.today()
    age = today.year - birth_date.year
    textbox.insert(END, f"Your current age = {age}\n")


btn = Button(frame,text='Age',command=age,bg='brown',fg='white')

frame.place(x=60,y=0)
lbl.place(x=20,y=20)
input.place(x=120,y=90)
btn.place(x=160,y=140)
textbox.place(x=95,y=200)

window.mainloop()