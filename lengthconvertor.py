from tkinter import *

window = Tk()

window.title('Length Convertor')
window.geometry('500x500')

frame = Frame(master=window, height=400, width=400, bg="#d0efff")

lbl1 = Label(frame, text="Input a length", bg="#3895D3", fg='white', width=12)

length_entry = Entry(frame)

def display():
    length = float(length_entry.get())
    output = 100 * length
    textbox.insert(END, output)

textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text="Convert", command=display, bg='blue')

frame.place(x=60, y=0)
lbl1.place(x=20, y=20)
length_entry.place(x=150, y=20)
btn.place(x=130, y=80)
textbox.place(y=250)

window.mainloop()