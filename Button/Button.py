# The button in the Tkinter module can be placed or move to any position in two ways:

# By using the place method.
# And by using the pack method.


# Method 1: Using the place method

# This method is used to place a button at an absolute defined position.

# Syntax : button1.place(x=some_value, y=some_value) 


# Importing tkinter module 
from tkinter import *	

# Creating a tkinter window
root = Tk() 

# Initialize tkinter window with dimensions 300 x 250			 
root.geometry('300x250')	 

# Creating a Button
btn = Button(root, text = 'Click me !', command = root.destroy)

# Set the position of button to coordinate (100, 20)
# btn.place(x=100, y=20)\
btn.pack(side=RIGHT, padx=15, pady=20)

root.mainloop()


# ----------------------------------------------------------

# Method 2: Using the pack method
# Syntax : button1.pack(side=some_side, padx=some_value, pady=some_value)

# Parameters : 

# side : It defines the side where the button will be placed.
# padx : It defines the padding on x-axis from the defined side.
# pady : It defines the padding on y-axis from the defines side.

# Importing tkinter module 
from tkinter import *	

# Creating a tkinter window
root = Tk() 

# Initialize tkinter window with dimensions 300 x 250			 
root.geometry('300x250')	 

# Creating a Button
btn = Button(root, text = 'Click me !', command = root.destroy)

# Set a relative position of button
btn.pack(side=RIGHT, padx=15, pady=20)

root.mainloop()

# -------------------------------------------------------------------------

# Method 3: Using the grid method

# This method is used to grid a button at a relative position.

# Syntax : button.widget.grid( grid_options )

# Parameters : 

# column − The column to place widget in; default 0 (leftmost column).
# columnspan − How many columns widgetoccupies; default 1.
# ipadx, ipady − How many pixels to pad widget, horizontally and vertically, inside widget’s borders.
# padx, pady − How many pixels to pad widget, horizontally and vertically, outside v’s borders.

# Importing tkinter module 
from tkinter import *	

# Creating a tkinter window
root = Tk() 

# Initialize tkinter window 
# with dimensions 300 x 250			 
root.geometry('300x250')	 

# Creating a Button
btn1 = Button(root, text = 'btn1 !', 
			command = root.destroy)
btn1.grid(row = 0, column = 0)

# Creating a Button
btn2 = Button(root, text = 'btn2 !', command = root.destroy)
btn2.grid(row = 1, column = 1)

# Creating a Button
btn3 = Button(root, text = 'btn3 !', command = root.destroy)
btn3.grid(row = 2, column = 2)

# Creating a Button
btn3 = Button(root, text = 'btn4 !', command = root.destroy)
btn3.grid(row = 4, column = 4)

root.mainloop()

	 


