# import tkinter

# m=tkinter.Tk()  # to create main window

# m.mainloop()    # used when application ready to run.


# GRID

from tkinter import *
root =Tk()
root.title("Practice")
Label(root, text="frist name").grid(row=0)
Label(root, text="last name").grid(row=1)

# Entry
entry = Entry(root)
entry1=Entry(root)
entry.grid(row=0, column=1)
entry1.grid(row=1, column=1)

# button
button=Button(root, text='stop' , width=25, command=root.destroy)
button.grid(row=2, columnspan=2)

# check button
var1=IntVar()
Checkbutton(root, text="women", variable=var1).grid(row=3,sticky=W)

v=IntVar()
Radiobutton(root, text="apple", variable=v, value=1).grid(row=4)
v=IntVar()
Radiobutton(root, text="banana", variable=v, value=2).grid(row=5)
v=IntVar()
Radiobutton(root, text="papaya", variable=v, value=3).grid(row=6)
root.mainloop()



# used for place()
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.place(x=50, y=50)

label2 = tk.Label(root, text="Label 2")
label2.place(x=100, y=100)

button = tk.Button(root, text="Button")
button.place(x=150, y=150)

root.mainloop()



#  PACK()
import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.pack()

label2 = tk.Label(root, text="Label 2")
label2.pack()

button = tk.Button(root, text="Button")
button.pack()

root.mainloop()

