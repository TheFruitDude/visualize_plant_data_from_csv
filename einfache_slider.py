from tkinter import *
import inspect

master = Tk()

w1 = Scale(master, from_=1914, to=1959, orient=HORIZONTAL, troughcolor='#ADD8E6', length=300, label="Von Jahr:")
w1.pack()

w2 = Scale(master, from_=1914, to=1959, orient=HORIZONTAL, troughcolor='#ADD8E6', length=300, label="Bis Jahr:")
w2.pack()


mainloop()