import spinniaexperiment
from tkinter import *
from tkinter import messagebox
# setup
win = Tk()
win.title("Spinnia Calculator")
win.geometry('400x250')


def click():
    data_label = Label(win, text=spinniaexperiment.main())
    data_label.pack()

# widgets


button = Button(win, text="Calculate", width=25, command=click).pack()

# run
win.mainloop()
