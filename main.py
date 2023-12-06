import spinnia_calc
from testing import price, pap, tickets
from tkinter import *
from PIL import Image, ImageTk

RARITIES = ['common', 'uncommon', 'rare', 'epic', 'legendary']

# setup

win = Tk()
win.title("Spinnia Calculator")
win.geometry('1200x500')

# frames
image_frame = Frame(win)
price_frame = Frame(win)
tickets_frame = Frame(win)
pap_frame = Frame(win)

# widgets

spn_price_label = Label(win, text=("SPN/WAX:", spinnia_calc.get_spn_price(), ))

common_spinney_image_file = Image.open("images\\common_spinney.png")
common_spinney_image_file = common_spinney_image_file.resize((100, 125))
img1 = ImageTk.PhotoImage(common_spinney_image_file)
img1_label = Label(image_frame, image=img1)

uncommon_spinney_image_file = Image.open("images\\uncommon_spinney.png")
uncommon_spinney_image_file = uncommon_spinney_image_file.resize((100, 125))
img2 = ImageTk.PhotoImage(uncommon_spinney_image_file)
img2_label = Label(image_frame, image=img2)

rare_spinney_image_file = Image.open("images\\rare_spinney.png")
rare_spinney_image_file = rare_spinney_image_file.resize((100, 125))
img3 = ImageTk.PhotoImage(rare_spinney_image_file)
img3_label = Label(image_frame, image=img3)

epic_spinney_image_file = Image.open("images\\epic_spinney.png")
epic_spinney_image_file = epic_spinney_image_file.resize((100, 125))
img4 = ImageTk.PhotoImage(epic_spinney_image_file)
img4_label = Label(image_frame, image=img4)

legendary_spinney_image_file = Image.open("images\\legendary_spinney.png")
legendary_spinney_image_file = legendary_spinney_image_file.resize((100, 125))
img5 = ImageTk.PhotoImage(legendary_spinney_image_file)
img5_label = Label(image_frame, image=img5)

img1_label.pack(side='left', padx=5)
img2_label.pack(side='left', padx=5)
img3_label.pack(side='left', padx=5)
img4_label.pack(side='left', padx=5)
img5_label.pack(side='left', padx=5)

for rarity in RARITIES:
    price_common = Label(price_frame, text=f'Cost: {price(rarity)} WAX')
    price_common.pack(side='left', padx=9)
    tickets_common = Label(tickets_frame, text=f'Ticket: {tickets(rarity)} WAX')
    tickets_common.pack(side='left', padx=10)
    pap_common = Label(pap_frame, text=f'PAP: {pap(rarity)} WAX')
    pap_common.pack(side='left', padx=17)

# pack order

spn_price_label.grid(row=1)
image_frame.grid(row=2)
price_frame.grid(row=3)
tickets_frame.grid(row=4)
pap_frame.grid(row=5)

# run
win.mainloop()
