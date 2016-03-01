"""
Hello World gui program in python.
"""
from Tkinter import *
window = Tk()
window.title("Label Example")
label = Label(window, text = "Hello World!")
label.pack(padx = 200, pady = 50)
window.configure(bg = 'blue')
# window.configure(activebackground = 'red')
window.mainloop( )
