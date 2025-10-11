# import necessary libraries
from tkinter import *

# create window
window = Tk()
window.title("Event Handler")
window.geometry("100x100")

# event handler for keypress
def handle_keypress(event):
    """Print the charater associated to the key pressed"""
    print(event.char)

# bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!")
button.pack() 

# bind click event to handle_click()
button.bind("<Button-1>", handle_click) # bind function is used to pass the value of that is pressed on the keyboard

# start the GUI event loop
window.mainloop()