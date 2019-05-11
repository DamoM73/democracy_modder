''' this program allows users to create their own country for Democracy 3 '''
from tkinter import *
from tkinter import messagebox

WIDTH = 1000
HEIGHT = 800
BG_COLOUR = "light grey"
ENTRY_COLOUR = "white"
INFO = {"country" : "The common name of your country.\nFor example, Australia.",
    "leader" : "The common title for the leader of the country.\nFor example, President.",
    "pop" : "The number of people residing in the country (in millions).",
    "currency" : "The symbol the country uses to denote currency.\n For example $.",
    "max_inc" : "The highest annual income in your country (in thousands).",
    "min_inc" : "The lowest annual income in your country (in thousands).",
    "max_gdp" : "The historical highest value of the country's\nGross Domestic Product (in millions).",
    "debt" : "The federal government's debt (in millions)."}

# **** Functions ****
def help_message(info):
    messagebox.showinfo("More info", info)


# **** Create main window ****
root = Tk()
#root.geometry("1200x800")
root.title("Democracy 3 Country Generator")
root.config(bg=BG_COLOUR)


# **** Add content to window ****

# ** header frame
head_fr = Frame(root, bg=BG_COLOUR, width=WIDTH).grid(row=0, column=0) 
logo = PhotoImage(file="logo_small.png")
Label(head_fr, image= logo, bg=BG_COLOUR).grid(row=0, column=0, sticky=W)
Label(head_fr, text="Country Generator ", font=("Arial", 22), justify=RIGHT, bg=BG_COLOUR)\
    .grid(row=0, column=1, sticky=E)

# ** country details frame
country_fr = LabelFrame(root, text="Country Details", font=("Arial",16), bg=BG_COLOUR)
country_fr.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# country name

Button(country_fr,text="Name", bg=BG_COLOUR, font=("Arial",12), width=9, anchor=W, relief=FLAT, command=lambda: help_message(INFO["country"]))\
    .grid(row=0, column=0, sticky=W)
name_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
name_ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# leader title
Button(country_fr,text="Leader Title", bg=BG_COLOUR, font=("Arial", 12), width=9, anchor=W, relief=FLAT, command=lambda: help_message(INFO["leader"]))\
    .grid(row=1, column=0, sticky=W)
leader_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
leader_ent.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# population
Button(country_fr,text="Pop (million)", bg=BG_COLOUR, font=("Arial", 12), width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["pop"]))\
    .grid(row=0, column=2, sticky=W)
pop_ent = Entry(country_fr, width=5, relief = FLAT, bg=ENTRY_COLOUR)
pop_ent.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# currency symbol
Button(country_fr,text="Currency Symbol", bg=BG_COLOUR, font=("Arial", 12), width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["currency"]))\
    .grid(row=1, column=2, sticky=W)
currency_ent = Entry(country_fr, width=5, relief = FLAT, bg=ENTRY_COLOUR)
currency_ent.grid(row=1, column=3, padx=5, pady=5)

# max income
Button(country_fr,text="Max Income ('000)", bg=BG_COLOUR, font=("Arial", 12), width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_inc"]))\
    .grid(row=0, column=4, sticky=W)
max_inc_ent = Entry(country_fr, width=9, relief = FLAT, bg=ENTRY_COLOUR)
max_inc_ent.grid(row=0, column=5, padx=5, pady=5)

# min income
Button(country_fr,text="Min Income ('000)", bg=BG_COLOUR, font=("Arial", 12), width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["min_inc"]))\
    .grid(row=1, column=4, sticky=W)
min_inc_ent = Entry(country_fr, width=9, relief = FLAT, bg=ENTRY_COLOUR)
min_inc_ent.grid(row=1, column=5, padx=5, pady=5)

# max gdp
Button(country_fr,text="Max GDP (millions)", bg=BG_COLOUR, font=("Arial", 12), width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_gdp"]))\
    .grid(row=0, column=6, sticky=W)
max_gdp_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
max_gdp_ent.grid(row=0, column=7, padx=5, pady=5)

# min gdp
Button(country_fr,text="Debt (millions)", bg=BG_COLOUR, font=("Arial", 12), width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["debt"]))\
    .grid(row=1, column=6, sticky=W)
debt_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
debt_ent.grid(row=1, column=7, padx=5, pady=5)

# **** run window loop ****
root.mainloop()