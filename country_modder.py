''' this program allows users to create their own country for Democracy 3 '''
from tkinter import *
from tkinter import messagebox

WIDTH = 1252
HEIGHT = 800

# formatting
BG_COLOUR = "light grey"
ENTRY_COLOUR = "white"
HEADING_1 = ("Arial",16)
HEADING_2 = ("Arial",12)
BODY = ("Arial",10)

INFO = {"country" : "The common name of your country.\nFor example, Australia.",
    "leader" : "The common title for the leader of the country.\nFor example, President.",
    "pop" : "The number of people residing in the country (in millions).",
    "currency" : "The symbol the country uses to denote currency.\n For example $.",
    "max_inc" : "The highest annual income in your country (in thousands).",
    "min_inc" : "The lowest annual income in your country (in thousands).",
    "max_gdp" : "The historical highest value of the country's\nGross Domestic Product (in millions).",
    "debt" : "The federal government's debt (in millions).",
    "name_file" : "The basis for the possilbe first and last names of the citizens of the country.",
    "economy" : "The global economic cycle works on a sine wave.\nAt 25 the world economy is at peak of growth,\nat 75 it is at the trough of growth.",
    "wealth" : "How wealthy is the country compared to other nations?\nFor example, USA would be 23, and Somalia would be 1",
    "description" : "A short paragraph describing the higlight of the country",
    "adult ed" : "Adult education subsidies are a way to encourage people to re-train and continue their education after they have joined the workforce. This includes evening classes and distance learning resources. These schemes help to raise the overall educational level of the workforce."
}

# sliders
DEFAULT_SLIDER = ("None", "Low", "Medium", "High", "Maximum")

# **** Functions ****
def help_message(info):
    messagebox.showinfo("More info", info)


# **** Create main window ****
root = Tk()
root.geometry(str(WIDTH)+"x"+str(HEIGHT))
root.title("Democracy 3 Country Generator")
root.config(bg=BG_COLOUR)


# **** Add content to window ****

# ** header frame
head_fr = Frame(root, bg=BG_COLOUR).grid(row=0, column=0) 
logo = PhotoImage(file="logo_small.png")
Label(head_fr, image= logo, bg=BG_COLOUR).grid(row=0, column=0, sticky=W)
Label(head_fr, text="Country Generator", font=("Arial", 22), anchor=E, bg=BG_COLOUR)\
    .grid(row=0, column=1, sticky=E, padx=5)

# ** country details frame
country_fr = LabelFrame(root, text="Country Details", font=HEADING_1, bg=BG_COLOUR)
country_fr.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# country name
Button(country_fr,text="Name", bg=BG_COLOUR, font=HEADING_2, width=9, anchor=W, relief=FLAT, command=lambda: help_message(INFO["country"]))\
    .grid(row=0, column=0, sticky=W)
name_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
name_ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# leader title
Button(country_fr,text="Leader Title", bg=BG_COLOUR, font=HEADING_2, width=9, anchor=W, relief=FLAT, command=lambda: help_message(INFO["leader"]))\
    .grid(row=1, column=0, sticky=W)
leader_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
leader_ent.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# population
Button(country_fr,text="Pop (million)", bg=BG_COLOUR, font=HEADING_2, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["pop"]))\
    .grid(row=0, column=2, sticky=W)
pop_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
pop_ent.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# currency symbol
Button(country_fr,text="Currency Symbol", bg=BG_COLOUR, font=HEADING_2, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["currency"]))\
    .grid(row=1, column=2, sticky=W)
currency_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
currency_ent.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# max income
Button(country_fr,text="Max Income ('000)", bg=BG_COLOUR, font=HEADING_2, width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_inc"]))\
    .grid(row=0, column=4, sticky=W)
max_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
max_inc_ent.grid(row=0, column=5, padx=5, pady=5)

# min income
Button(country_fr,text="Min Income ('000)", bg=BG_COLOUR, font=HEADING_2, width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["min_inc"]))\
    .grid(row=1, column=4, sticky=W)
min_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
min_inc_ent.grid(row=1, column=5, padx=5, pady=5)

# max gdp
Button(country_fr,text="Max GDP (millions)", bg=BG_COLOUR, font=HEADING_2, width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_gdp"]))\
    .grid(row=0, column=6, sticky=W)
max_gdp_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
max_gdp_ent.grid(row=0, column=7, padx=5, pady=5)

# min gdp
Button(country_fr,text="Debt (millions)", bg=BG_COLOUR, font=HEADING_2, width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["debt"]))\
    .grid(row=1, column=6, sticky=W)
debt_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
debt_ent.grid(row=1, column=7, padx=5, pady=5)

# name file
Button(country_fr,text="Citizen Names", bg=BG_COLOUR, font=HEADING_2, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["name_file"]))\
    .grid(row=0, column=8, sticky=W, padx=5)
names_file_lb = Listbox(country_fr, height=6, relief=FLAT, font=HEADING_2, width=12)
names_file_lb.insert(1,"Australia")
names_file_lb.insert(2,"Canada")
names_file_lb.insert(3,"France")
names_file_lb.insert(4,"Germany")
names_file_lb.insert(5,"UK")
names_file_lb.insert(6,"USA")
names_file_lb.grid(row=1, column=8, sticky=NW, padx=5, rowspan=4)

# Economic Cycle
Button(country_fr,text="Global Economy", bg=BG_COLOUR, font=HEADING_2, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["economy"]))\
    .grid(row=0, column=9, sticky=SW)
economic_control = IntVar()
Scale(country_fr, variable=economic_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=120, highlightbackground=BG_COLOUR)\
    .grid(row=1,column=9, sticky=NW)

# Wealth Indicator
Button(country_fr,text="Relavitve wealth", bg=BG_COLOUR, font=HEADING_2, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["wealth"]))\
    .grid(row=3, column=9, sticky=SW)
wealth_control = IntVar()
Scale(country_fr, variable=wealth_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=120, highlightbackground=BG_COLOUR, from_=1, to=25)\
    .grid(row=4, column=9, sticky=NW)

# Description
Button(country_fr,text="Country Description", bg=BG_COLOUR, font=HEADING_2, width=20, anchor=W, relief=FLAT, command=lambda: help_message(INFO["description"]))\
    .grid(row=3, column=0, columnspan=8, sticky=W)
description_tb = Text(country_fr,width=120, height=5)
description_tb.grid(row=4, column=0, columnspan=8, sticky=W, padx=5, pady=5)

# ** Policies Frame
policies_fr = LabelFrame(root,text="Policies", font=HEADING_1, bg= BG_COLOUR)
policies_fr.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Adult Education Subsidies
Button(policies_fr, text="Adult Education", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["adult ed"]))\
    .grid(row=0, column=0, sticky=W, padx=5)
adult_ed_control = StringVar()
adult_ed_control.set(DEFAULT_SLIDER[0])
adult_ed = OptionMenu(policies_fr, adult_ed_control,*DEFAULT_SLIDER)
adult_ed.config(bg=BG_COLOUR)
adult_ed["menu"].config(bg=BG_COLOUR)
adult_ed.grid(row=0, column=1, sticky=W, padx=5)


# **** run window loop ****
root.mainloop()