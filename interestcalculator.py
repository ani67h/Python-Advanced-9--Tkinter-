from tkinter import *

window = Tk()
window.title('Interest Calculator App')
window.geometry('500x400')

frame = Frame(master=window, height=500, width=400, bg="#d0efff")
lbl_p = Label(frame, text="Enter the principle value : ", bg="#3895D3", fg='white', width=25)
lbl_r = Label(frame, text="Enter the interest rate : ", bg="#3895D3", fg='white', width=25)
lbl_n = Label(frame, text="Enter the time : ", bg="#3895D3", fg='white', width=25)
p_entry = Entry(frame)
r_entry = Entry(frame)
n_entry = Entry(frame)
textbox = Text(frame, height=2, width=30)
textbox.pack(pady=10)

def interest():
    prin = float(p_entry.get())
    rate = float(r_entry.get())
    time = float(n_entry.get())

    simple = prin * time * (rate/100)
    textbox.insert(END, f"Simple Interest = {simple}\n")

    compound = (prin * (1+(rate/100))**time) - prin
    textbox.insert(END, f"Compound Interest = {compound}\n")

btn = Button(frame,text='Calculate',command=interest,bg='brown',fg='white')

frame.place(x=60,y=0)
lbl_p.place(x=30,y=10)
p_entry.place(x=210,y=10)
lbl_r.place(x=30,y=60)
r_entry.place(x=210,y=60)
lbl_n.place(x=30,y=110)
n_entry.place(x=210,y=110)
btn.place(x=150,y=170)
textbox.place(x=60,y=220)

window.mainloop()