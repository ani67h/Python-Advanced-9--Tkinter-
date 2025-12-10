from tkinter import *
import random

window = Tk()

window.title('Rock Paper Scissor')
window.geometry('600x600')

frame = Frame(master=window,height=500,width=500,bg="#d0efff")

lb1 = Label(frame,text='Choose any : ROCK, PAPER or SCISSOR (Enter your option in block letters)',bg='#3895D3',fg='white',width=70)
user_input = Entry(frame)
textbox = Text(frame, height=5, width=30)

def run():
    user_choice = user_input.get()
    options = ['ROCK','PAPER','SCISSOR']
    pc_choice = random.choice(options)

    if user_choice==pc_choice:
        msg = 'draw'
    elif user_choice == 'ROCK' and pc_choice == 'SCISSOR':
        msg = 'You won!'
    elif user_choice == 'SCISSOR' and pc_choice == 'PAPER':
        msg = 'You won!'
    elif user_choice == 'PAPER' and pc_choice =='ROCK':
        msg = 'You won!'
    else:
        msg = 'You lose!'
    textbox.insert(END, msg)

Button(frame, text="Play", command=run).place(x=20, y=80)

frame.place(x=60, y=0)
lb1.place(x=20, y=20)
user_input.place(x=20, y=50)
textbox.place(x=20,y=110)

window.mainloop()