# Import package and it's modules 
from tkinter import *

# create root window 
root = Tk() 

# root window title and dimension 
root.title("GeekForGeeks") 

# Set geometry (widthxheight) 
root.geometry('200x200') 

# Entry Box 
text = Entry(root, width = 30, bg = 'lightblue') 
text.pack(pady = 10) 

# Execute Tkinter 
root.mainloop() 
