# importing tkinter module used for gui
from tkinter import *
from tkinter.ttk import *

# strftime  will import current time from your device
from time import strftime

# setting up a tkinter window
root = Tk()
root.title('Clock')

def time():
	string = strftime('%I:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

lbl = Label(root, font = ('Open sans', 200, 'bold'),
			background = 'black',
			foreground = 'white')

lbl.pack(anchor = 'center')
time()

mainloop()
