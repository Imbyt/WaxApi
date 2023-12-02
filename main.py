import spinnia_calc
from tkinter import *
from PIL import Image, ImageTk


def get_spinney_info():
    data_label = Label(win, text=spinnia_calc.main("spinney"))
    data_label.grid(row=1, column=2)


def get_rune_info():
    data_label = Label(win, text=spinnia_calc.main("rune"))
    data_label.grid(row=2, column=2)


def quit_window():
    win.destroy()


# setup
win = Tk()
win.title("Spinnia Calculator")
win.geometry('1200x500')

# widgets

calculate_spinney_button = Button(win, text="Calculate Spinnies!", width=25, command=get_spinney_info)
calculate_spinney_button.grid(row=1, column=1)

calculate_rune_button = Button(win, text="Calculate Runes!", width=25, command=get_rune_info)
calculate_rune_button.grid(row=2, column=1)

quit_button = Button(win, text="Quit", width=25, command=quit_window)
quit_button.grid(row=3, column=1)

spn_price_label = Label(win, text=("SPN/WAX:", spinnia_calc.get_spn_price(), ))
spn_price_label.grid(row=4, column=1)

common_spinney_image_file = Image.open("images\\common_spinney.png")
common_spinney_image_file = common_spinney_image_file.resize((100, 125))
img1 = ImageTk.PhotoImage(common_spinney_image_file)
img1_label = Label(image=img1)
img1_label.grid(row=5, column=1)

# run
win.mainloop()
