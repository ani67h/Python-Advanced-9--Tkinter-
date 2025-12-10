from tkinter import *

root = Tk()
root.title("Here's the Product")
root.geometry('400x400')

lbl1 = Label(root,text='Enter the number 1 : ',fg='black',bg="#5F5007", height=1, width=20)
lbl2 = Label(root,text='Enter the number 2 : ',fg='black',bg="#365F07", height=1, width=20)

num1_input = Entry()
num2_input = Entry()
num1 = num1_input.get()
num2 = num2_input.get()

def product(num1,num2):
    return num1*num2

def calculate():
    num1 = int(num1_input.get())
    num2 = int(num2_input.get())
    result = product(num1,num2)
    text_box.insert("1.0", result)

text_box = Text(root,height=1,width=20)
btn = Button(text='Product',command=calculate,height=1,bg="#60A012", fg='white')

lbl1.place(x=20,y=20)
lbl2.place(x=20,y=60)
num1_input.place(x=150,y=20)
num2_input.place(x=150,y=60)
btn.place(x=20,y=100)
text_box.place(x=20,y=140)
root.mainloop()