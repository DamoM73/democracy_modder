''' this program allows users to create their own country for Democracy 3 '''
from tkinter import *
from tkinter import messagebox
import csv


WIDTH = 1255
HEIGHT = 950

# formatting
BG_COLOUR = "light grey"
ENTRY_COLOUR = "white"
HEADING_1 = ("Arial",16)
BUTTON = ("Arial",12)
BODY = ("Arial",8)
SB_WIDTH = 17

# load policy info
# policy info explains each polic and is displayed in a messagase box when the policy button is pressed
file = open("policy_info.txt","r")
INFO = eval(file.read())
file.close()

# load slider values
# slider valuesa re the possible policy setting for each policy, as taken from the Democracy 3 game files
file = open("sliders.txt", "r")
SLIDERS = eval(file.read())
file.close()



# **** Functions ****
def help_message(key):
    '''
    This function displays a message box containing information about the policy.
    The information is retieved from the info dictionary using the passed key
    '''
    messagebox.showinfo(key+" Explanation", INFO[key])

def save():
    pass

def load():
    pass

def export():
    pass


# **** Create main window ****
root = Tk()
root.geometry(str(WIDTH)+"x"+str(HEIGHT))
root.title("Democracy 3 Country Generator")
root.config(bg=BG_COLOUR)


# **** Add content to window ****

# ** header frame
head_fr = Frame(root, bg=BG_COLOUR)
head_fr.grid(row=0, column=0, columnspan = 2, sticky=W+E) 
logo = PhotoImage(file="logo_small.png")
Label(head_fr, image= logo, bg=BG_COLOUR).grid(row=0, column=0, sticky=W)
Label(head_fr, text="Country Generator", font=("Arial", 22), anchor=E, bg=BG_COLOUR)\
    .grid(row=0, column=1, sticky=E, padx=5)


# ** country details frame
country_fr = LabelFrame(root, text="Country Details", font=HEADING_1, bg=BG_COLOUR)
country_fr.grid(row=1, column=0, columnspan=2, sticky=W, padx=5, pady=5)

# column 0
# country name
Button(country_fr,text="Country Name", bg=BG_COLOUR, font=BODY, width=11, anchor=W, relief=FLAT, command=lambda: help_message("Country Name"))\
    .grid(row=0, column=0, sticky=W)
name_ent = Entry(country_fr, width=35, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
name_ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# leader title
Button(country_fr,text="Leader Title", bg=BG_COLOUR, font=BODY, width=11, anchor=W, relief=FLAT, command=lambda: help_message("Leader Title"))\
    .grid(row=1, column=0, sticky=W)
leader_ent = Entry(country_fr, width=35, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
leader_ent.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# citizen names
Button(country_fr,text="Citizen Names", bg=BG_COLOUR, font=BODY, width=11, anchor=W, relief=FLAT, command=lambda: help_message("Citizen Names"))\
    .grid(row=2, column=0, sticky=W)
cit_name_sb = Spinbox(country_fr, values=SLIDERS["names list"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=33)
cit_name_sb.grid(row=2, column=1, sticky=W, padx=5)

# Economic Cycle
Button(country_fr,text="Global Economy", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Global Economy"))\
    .grid(row=3, column=0, sticky=W)
economic_control = IntVar()
Scale(country_fr, variable=economic_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=218, highlightbackground=BG_COLOUR)\
    .grid(row=3,column=1, sticky=NW)

# column 1
# population
Button(country_fr,text="Pop (million)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Population"))\
    .grid(row=0, column=2, sticky=W)
pop_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
pop_ent.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# currency symbol
Button(country_fr,text="Currency Symbol", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Currency Symbol"))\
    .grid(row=1, column=2, sticky=W)
currency_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
currency_ent.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# max gdp
Button(country_fr,text="Max GDP (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Max GDP"))\
    .grid(row=2, column=2, sticky=W)
max_gdp_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
max_gdp_ent.grid(row=2, column=3, padx=5, pady=5, sticky=W)

# column 2
# max income
Button(country_fr,text="Max Income ('000)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Max Income"))\
    .grid(row=0, column=4, sticky=W)
max_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
max_inc_ent.grid(row=0, column=5, padx=5, pady=5, sticky=W)

# min income
Button(country_fr,text="Min Income ('000)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Min Income"))\
    .grid(row=1, column=4, sticky=W)
min_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
min_inc_ent.grid(row=1, column=5, padx=5, pady=5, sticky=W)

# debt
Button(country_fr,text="Debt (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Debt"))\
    .grid(row=2, column=4, sticky=W)
debt_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
debt_ent.grid(row=2, column=5, padx=5, pady=5, sticky=W)

# Wealth Indicator
Button(country_fr,text="Relavitve wealth", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Relavitve wealth"))\
    .grid(row=3, column=2, sticky=W)
wealth_control = IntVar()
Scale(country_fr, variable=wealth_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=240, highlightbackground=BG_COLOUR, from_=1, to=25)\
    .grid(row=3, column=3, sticky=NW, columnspan=3)


# column 3
# Country Description
Button(country_fr,text="Country Description", bg=BG_COLOUR, font=BODY, relief=FLAT, width=20, anchor=W, command=lambda: help_message("Country Description"))\
    .grid(row=0, column=8, sticky=W)
description_tb = Text(country_fr,width=71, height=6)
description_tb.grid(row=1, column=8, rowspan=3, sticky=W, padx=5, pady=5)


# ** Policies Frame
policies_fr = LabelFrame(root,text="Policies", font=HEADING_1, bg= BG_COLOUR)
policies_fr.grid(row=2, column=0, columnspan = 2, sticky=W, padx=5, pady=5)

# Adult Education Subsidies
Button(policies_fr, text="Adult Education", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Adult Education"))\
    .grid(row=0, column=0, sticky=W, padx=5)
ad_ed_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
ad_ed_sb.grid(row=0, column=1, sticky=W, padx=5)

# Agriculture Subsidies
Button(policies_fr, text="Agriculture Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Agriculture Subsidies"))\
    .grid(row=1, column=0, sticky=W, padx=5)
agri_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
agri_sb.grid(row=1, column=1, sticky=W, padx=5)

# Airline Tax
Button(policies_fr, text="Airline Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Airline Tax"))\
    .grid(row=2, column=0, sticky=W, padx=5, )
airline_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
airline_tax_sb.grid(row=2, column=1, sticky=W, padx=5)

# AlcoholLaw
Button(policies_fr, text="Alcohol Law", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Alcohol Law"))\
    .grid(row=3, column=0, sticky=W, padx=5)
alco_sb = Spinbox(policies_fr, values=SLIDERS["alcohol"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
alco_sb.grid(row=3, column=1, sticky=W, padx=5)

# Alcohol Tax
Button(policies_fr, text="Alcohol Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Alcohol Tax"))\
    .grid(row=4, column=0, sticky=W, padx=5)
alco_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
alco_tax_sb.grid(row=4, column=1, sticky=W, padx=5)

# Armed Police
Button(policies_fr, text="Armed Police", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Armed Police"))\
    .grid(row=5, column=0, sticky=W, padx=5)
arm_pol_sb = Spinbox(policies_fr, values=SLIDERS["armed police"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
arm_pol_sb.grid(row=5, column=1, sticky=W, padx=5)

# Ban Sunday Shopping
Button(policies_fr, text="Sunday Shopping", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Ban Sunday Shopping"))\
    .grid(row=6, column=0, sticky=W, padx=5)
sun_trade_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sun_trade_sb.grid(row=6, column=1, sticky=W, padx=5)

# Biofuel Subsidies
Button(policies_fr, text="Biofuel Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Biofuel Subsidies"))\
    .grid(row=7, column=0, sticky=W, padx=5)
biofuel_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
biofuel_sb.grid(row=7, column=1, sticky=W, padx=5)

# Border Controls
Button(policies_fr, text="Border Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Border Controls"))\
    .grid(row=8, column=0, sticky=W, padx=5)
border_sb = Spinbox(policies_fr, values=SLIDERS["border"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
border_sb.grid(row=8, column=1, sticky=W, padx=5)

# Bus Lanes
Button(policies_fr, text="Bus Lanes", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Bus Lanes"))\
    .grid(row=9, column=0, sticky=W, padx=5)
bus_lane_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_lane_sb.grid(row=9, column=1, sticky=W, padx=5)

# Bus Subsidies
Button(policies_fr, text="Bus Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Bus Subsidies"))\
    .grid(row=10, column=0, sticky=W, padx=5)
bus_subs_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_subs_sb.grid(row=10, column=1, sticky=W, padx=5)

# Carbon Tax
Button(policies_fr, text="Carbon Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Carbon Tax"))\
    .grid(row=11, column=0, sticky=W, padx=5)
carbon_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
carbon_tax_sb.grid(row=11, column=1, sticky=W, padx=5)

# Car Emission Limits
Button(policies_fr, text="Car Emission Limits", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Car Emission Limits"))\
    .grid(row=12, column=0, sticky=W, padx=5)
car_emissions_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
car_emissions_sb.grid(row=12, column=1, sticky=W, padx=5)

# Car Tax
Button(policies_fr, text="Car Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Car Tax"))\
    .grid(row=13, column=0, sticky=W, padx=5)
car_tax_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
car_tax_sb.grid(row=13, column=1, sticky=W, padx=5)

# "CCTV" Cameras
Button(policies_fr, text="CCTV Cameras", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("CCTV Cameras"))\
    .grid(row=14, column=0, sticky=W, padx=5)
cctv_sb = Spinbox(policies_fr, values=SLIDERS["CCTV"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
cctv_sb.grid(row=14, column=1, sticky=W, padx=5)

# Child Benefit
Button(policies_fr, text="Child Benefit", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Child Benefit"))\
    .grid(row=15, column=0, sticky=W, padx=5)
child_benefit_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
child_benefit_sb.grid(row=15, column=1, sticky=W, padx=5)

# Childcare Provision
Button(policies_fr, text="Childcare Provision", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Childcare Provision"))\
    .grid(row=16, column=0, sticky=W, padx=5)
childcare_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
childcare_sb.grid(row=16, column=1, sticky=W, padx=5)

# Citizenship Tests
Button(policies_fr, text="Citizenship Tests", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Citizenship Tests"))\
    .grid(row=17, column=0, sticky=W, padx=5)
citizen_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
citizen_sb.grid(row=17, column=1, sticky=W, padx=5)

# Clean Energy Subsidies
Button(policies_fr, text="Clean Energy Sub", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Clean Energy Subsidies"))\
    .grid(row=18, column=0, sticky=W, padx=5)
clean_energy_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
clean_energy_sb.grid(row=18, column=1, sticky=W, padx=5)

# Clean Fuel Subsidy
Button(policies_fr, text="Clean Fuel Sub", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Clean Fuel Subsidy"))\
    .grid(row=19, column=0, sticky=W, padx=5)
clean_fuel_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
clean_fuel_sb.grid(row=19, column=1, sticky=W, padx=5)

# Community Policing
Button(policies_fr, text="Community Policing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Community Policing"))\
    .grid(row=20, column=0, sticky=W, padx=5)
com_pol_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
com_pol_sb.grid(row=20, column=1, sticky=W, padx=5)

# "Consumer"Rights
Button(policies_fr, text="Consumer Rights", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Consumer Rights"))\
   .grid(row=21, column=0, sticky=W, padx=5)
consumer_rts_sb = Spinbox(policies_fr, values=SLIDERS["consumer"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
consumer_rts_sb.grid(row=21, column=1, sticky=W, padx=5)

# Corporation Tax
Button(policies_fr, text="Corporation Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Corporation Tax"))\
    .grid(row=22, column=0, sticky=W, padx=5)
corp_tax_sb = Spinbox(policies_fr, from_=1, to=50, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
corp_tax_sb.grid(row=22, column=1, sticky=W, padx=5)

# Creation. v Evol
Button(policies_fr, text="Creation v Evol", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Creationism vs. Evolution"))\
    .grid(row=23, column=0, sticky=W, padx=5)
creationism_sb = Spinbox(policies_fr, values=SLIDERS["creation"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
creationism_sb.grid(row=23, column=1, sticky=W, padx=5)

# Curfews
Button(policies_fr, text="Curfews", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Curfews"))\
    .grid(row=24, column=0, sticky=W, padx=5)
curfews_sb = Spinbox(policies_fr, values=SLIDERS["curfews"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
curfews_sb.grid(row=24, column=1, sticky=W, padx=5)

# Death Penalty
Button(policies_fr, text="Death Penalty", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Death Penalty"))\
    .grid(row=0, column=2, sticky=W, padx=5)
death_pen_sb = Spinbox(policies_fr, values=SLIDERS["death"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
death_pen_sb.grid(row=0, column=3, sticky=W, padx=5)

# Detention Without Trial
Button(policies_fr, text="Detention Without Trial", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Detention Without Trial"))\
    .grid(row=1, column=2, sticky=W, padx=5)
detention_sb = Spinbox(policies_fr, values=SLIDERS["detention"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
detention_sb.grid(row=1, column=3, sticky=W, padx=5)

# Disability Benefit
Button(policies_fr, text="Disability Benefit", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Disability Benefit"))\
    .grid(row=2, column=2, sticky=W, padx=5)
disability_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
disability_sb.grid(row=2, column=3, sticky=W, padx=5)

# Faith School Subsidies
Button(policies_fr, text="Faith School Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Faith School Subsidies"))\
    .grid(row=3, column=2, sticky=W, padx=5)
faith_schools_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
faith_schools_sb.grid(row=3, column=3, sticky=W, padx=5)

# Foreign Aid
Button(policies_fr, text="Foreign Aid", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Foreign Aid"))\
    .grid(row=4, column=2, sticky=W, padx=5)
foreign_aid_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
foreign_aid_sb.grid(row=4, column=3, sticky=W, padx=5)

# Bus Passes
Button(policies_fr, text="Free Bus Passes", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free Bus Passes"))\
    .grid(row=5, column=2, sticky=W, padx=5)
bus_passes_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_passes_sb.grid(row=5, column=3, sticky=W, padx=5)

# Free Eye Tests
Button(policies_fr, text="Free Eye Tests", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free Eye Tests"))\
    .grid(row=6, column=2, sticky=W, padx=5)
eye_tests_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
eye_tests_sb.grid(row=6, column=3, sticky=W, padx=5)

# Free School Meals
Button(policies_fr, text="Free School Meals", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free School Meals"))\
    .grid(row=7, column=2, sticky=W, padx=5)
school_meals_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
school_meals_sb.grid(row=7, column=3, sticky=W, padx=5)

# Gambling
Button(policies_fr, text="Gambling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Gambling"))\
    .grid(row=8, column=2, sticky=W, padx=5)
gambling_sb = Spinbox(policies_fr, values=SLIDERS["gambling"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
gambling_sb.grid(row=8, column=3, sticky=W, padx=5)

# Graduate tax
Button(policies_fr, text="Graduate tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Graduate tax"))\
    .grid(row=9, column=2, sticky=W, padx=5)
grad_tax_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
grad_tax_sb.grid(row=9, column=3, sticky=W, padx=5)

# Handgun Laws
Button(policies_fr, text="Handgun Laws", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Handgun Laws"))\
    .grid(row=10, column=2, sticky=W, padx=5)
handgun_sb = Spinbox(policies_fr, values=SLIDERS["handguns"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
handgun_sb.grid(row=10, column=3, sticky=W, padx=5)

# Hybrid Cars Initiative
Button(policies_fr, text="Hybrid Cars", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Hybrid Cars"))\
    .grid(row=11, column=2, sticky=W, padx=5)
hybrid_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
hybrid_sb.grid(row=11, column=3, sticky=W, padx=5)

# ID Cards
Button(policies_fr, text="ID Cards", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("ID Cards"))\
    .grid(row=12, column=2, sticky=W, padx=5)
id_sb = Spinbox(policies_fr, values=SLIDERS["id"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
id_sb.grid(row=12, column=3, sticky=W, padx=5)

# Import Tariffs
Button(policies_fr, text="Import Tariffs", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Import Tariffs"))\
    .grid(row=13, column=2, sticky=W, padx=5)
tariffs_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tariffs_sb.grid(row=13, column=3, sticky=W, padx=5)

# Income Tax
Button(policies_fr, text="Income Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Income Tax"))\
    .grid(row=14, column=2, sticky=W, padx=5)
income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
income_tax_sb.grid(row=14, column=3, sticky=W, padx=5)

# Flat Income Tax
Button(policies_fr, text="Flat Income Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Flat Income Tax"))\
    .grid(row=15, column=2, sticky=W, padx=5)
flat_income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
flat_income_tax_sb.grid(row=15, column=3, sticky=W, padx=5)

# Capital Gains Tax
Button(policies_fr, text="Capital Gains Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Capital Gains Tax"))\
    .grid(row=16, column=2, sticky=W, padx=5)
flat_income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
flat_income_tax_sb.grid(row=16, column=3, sticky=W, padx=5)

# Inheritance Tax
Button(policies_fr, text="Inheritance Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Inheritance Tax"))\
    .grid(row=17, column=2, sticky=W, padx=5)
inheritance_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
inheritance_tax_sb.grid(row=17, column=3, sticky=W, padx=5)

# Intelligence Services
Button(policies_fr, text="Intelligence Services", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Intelligence Services"))\
    .grid(row=18, column=2, sticky=W, padx=5)
intel_sb = Spinbox(policies_fr, values=SLIDERS["intel"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
intel_sb.grid(row=18, column=3, sticky=W, padx=5)

# Internet Censorship
Button(policies_fr, text="Internet Censorship", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Internet Censorship"))\
    .grid(row=19, column=2, sticky=W, padx=5)
internet_censorship_sb = Spinbox(policies_fr, values=SLIDERS["net censorship"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
internet_censorship_sb.grid(row=19, column=3, sticky=W, padx=5)

# Internet Tax
Button(policies_fr, text="Internet Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Internet Tax"))\
    .grid(row=20, column=2, sticky=W, padx=5)
internet_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
internet_tax_sb.grid(row=20, column=3, sticky=W, padx=5)

# Jury Trial
Button(policies_fr, text="Jury Trial", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Jury Trial"))\
    .grid(row=21, column=2, sticky=W, padx=5)
jury_trial_sb = Spinbox(policies_fr, values=SLIDERS["jury trial"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
jury_trial_sb.grid(row=21, column=3, sticky=W, padx=5)

# Labor Laws
Button(policies_fr, text="Labor Laws", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Labor Laws"))\
    .grid(row=22, column=2, sticky=W, padx=5)
labor_laws_sb = Spinbox(policies_fr, values=SLIDERS["labor laws"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
labor_laws_sb.grid(row=22, column=3, sticky=W, padx=5)

# Legal Aid
Button(policies_fr, text="Legal Aid", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Legal Aid"))\
    .grid(row=23, column=2, sticky=W, padx=5)
legal_aid_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
legal_aid_sb.grid(row=23, column=3, sticky=W, padx=5)

# Legalize Prostitution
Button(policies_fr, text="Legalize Prostitution", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Legalize Prostitution"))\
    .grid(row=24, column=2, sticky=W, padx=5)
prostitution_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prostitution_sb.grid(row=24, column=3, sticky=W, padx=5)

# Luxury Goods Tax
Button(policies_fr, text="Luxury Goods Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Luxury Goods Tax"))\
    .grid(row=0, column=4, sticky=W, padx=5)
luxary_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
luxary_tax_sb.grid(row=0, column=5, sticky=W, padx=5)

# Married Tax Allowance
Button(policies_fr, text="Married Tax Allow.", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Married Tax Allowance"))\
    .grid(row=1, column=4, sticky=W, padx=5)
married_tax_sb = Spinbox(policies_fr, values=SLIDERS["marrage tax"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
married_tax_sb.grid(row=1, column=5, sticky=W, padx=5)

# Maternity Leave
Button(policies_fr, text="Maternity Leave", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Maternity Leave"))\
    .grid(row=2, column=4, sticky=W, padx=5)
maternity_sb = Spinbox(policies_fr, values=SLIDERS["maternity"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
maternity_sb.grid(row=2, column=5, sticky=W, padx=5)

# Micro-Generation Grants
Button(policies_fr, text="Micro-Gen. Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Micro-Generation Grants"))\
    .grid(row=3, column=4, sticky=W, padx=5)
microgen_grants_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
microgen_grants_sb.grid(row=3, column=5, sticky=W, padx=5)

# Military Spending
Button(policies_fr, text="Military Spending", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Military Spending"))\
    .grid(row=4, column=4, sticky=W, padx=5)
military_sb = Spinbox(policies_fr, values=SLIDERS["military"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
military_sb.grid(row=4, column=5, sticky=W, padx=5)

# National Monorail System
Button(policies_fr, text="Monorail System", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("National Monorail System"))\
    .grid(row=5, column=4, sticky=W, padx=5)
monorail_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
monorail_sb.grid(row=5, column=5, sticky=W, padx=5)

# Mortgage Tax Relief
Button(policies_fr, text="Mort. Tax Relief", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Mortgage Tax Relief"))\
    .grid(row=6, column=4, sticky=W, padx=5)
mortgage_relief_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
mortgage_relief_sb.grid(row=6, column=5, sticky=W, padx=5)

# Narcotics
Button(policies_fr, text="Narcotics", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Narcotics"))\
    .grid(row=7, column=4, sticky=W, padx=5)
narcotics_sb = Spinbox(policies_fr, values=SLIDERS["narcotics"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
narcotics_sb.grid(row=7, column=5, sticky=W, padx=5)

# National Service
Button(policies_fr, text="National Service", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("National Service"))\
    .grid(row=8, column=4, sticky=W, padx=5)
national_service_sb = Spinbox(policies_fr, values=SLIDERS["national service"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
national_service_sb.grid(row=8, column=5, sticky=W, padx=5)

# Organ Donation
Button(policies_fr, text="Organ Donation", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Organ Donation"))\
    .grid(row=9, column=4, sticky=W, padx=5)
organ_donor_sb = Spinbox(policies_fr, values=SLIDERS["organs"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
organ_donor_sb.grid(row=9, column=5, sticky=W, padx=5)

# Organic Farming Subsidy
Button(policies_fr, text="Organic Farming", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Organic Farming Subsidy"))\
    .grid(row=10, column=4, sticky=W, padx=5)
organic_farm_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
organic_farm_sb.grid(row=10, column=5, sticky=W, padx=5)

# Petrol Tax
Button(policies_fr, text="Petrol Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Petrol Tax"))\
    .grid(row=11, column=4, sticky=W, padx=5)
petrol_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
petrol_tax_sb.grid(row=11, column=5, sticky=W, padx=5)

# Wire Tapping
Button(policies_fr, text="Wire Tapping", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Wire Tapping"))\
    .grid(row=12, column=4, sticky=W, padx=5)
wire_tapping_sb = Spinbox(policies_fr, values=SLIDERS["wire tap"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
wire_tapping_sb.grid(row=12, column=5, sticky=W, padx=5)

# Plastic Bag Tax
Button(policies_fr, text="Plastic Bag Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Plastic Bag Tax"))\
    .grid(row=13, column=4, sticky=W, padx=5)
plas_bag_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
plas_bag_sb.grid(row=13, column=5, sticky=W, padx=5)

# Police Force (compulsoray)
Button(policies_fr, text="Police Force", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Police Force"))\
    .grid(row=14, column=4, sticky=W, padx=5)
police_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
police_sb.grid(row=14, column=5, sticky=W, padx=5)

# Pollution Controls
Button(policies_fr, text="Pollution Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Pollution Controls"))\
    .grid(row=15, column=4, sticky=W, padx=5)
pollution_sb = Spinbox(policies_fr, values=SLIDERS["pollution"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pollution_sb.grid(row=15, column=5, sticky=W, padx=5)

# Prisoner Tagging
Button(policies_fr, text="Prisoner Tagging", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Prisoner Tagging"))\
    .grid(row=16, column=4, sticky=W, padx=5)
pris_tag_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pris_tag_sb.grid(row=16, column=5, sticky=W, padx=5)

# Prisons
Button(policies_fr, text="Prisons", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Prisons"))\
    .grid(row=17, column=4, sticky=W, padx=5)
prisons_sb = Spinbox(policies_fr, values=SLIDERS["prison"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prisons_sb.grid(row=17, column=5, sticky=W, padx=5)

# Property Tax
Button(policies_fr, text="Property Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Property Tax"))\
    .grid(row=18, column=4, sticky=W, padx=5)
prop_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
prop_tax_sb.grid(row=18, column=5, sticky=W, padx=5)

# Public Libraries
Button(policies_fr, text="Public Libraries", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Public Libraries"))\
    .grid(row=19, column=4, sticky=W, padx=5)
libraries_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
libraries_sb.grid(row=19, column=5, sticky=W, padx=5)

# Racial Profiling
Button(policies_fr, text="Racial Profiling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Racial Profiling"))\
    .grid(row=20, column=4, sticky=W, padx=5)
profiling_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
profiling_sb.grid(row=20, column=5, sticky=W, padx=5)

# Race Discrimination
Button(policies_fr, text="Race Discrimination", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Race Discrimination Act"))\
    .grid(row=21, column=4, sticky=W, padx=5)
discrimination_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
discrimination_sb.grid(row=21, column=5, sticky=W, padx=5)

# Rail Subsidies
Button(policies_fr, text="Rail Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Rail Subsidies"))\
    .grid(row=22, column=4, sticky=W, padx=5)
discrimination_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
discrimination_sb.grid(row=22, column=5, sticky=W, padx=5)

# Recycling
Button(policies_fr, text="Recycling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Recycling"))\
    .grid(row=23, column=4, sticky=W, padx=5)
recycling_sb = Spinbox(policies_fr, values=SLIDERS["recycling"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
recycling_sb.grid(row=23, column=5, sticky=W, padx=5)

# Road Building
Button(policies_fr, text="Road Building", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Road Building"))\
    .grid(row=24, column=4, sticky=W, padx=5)
roads_sb = Spinbox(policies_fr, values=SLIDERS["roads"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
roads_sb.grid(row=24, column=5, sticky=W, padx=5)

# Rural Development Grants
Button(policies_fr, text="Rural Development", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Rural Development"))\
    .grid(row=0, column=6, sticky=W, padx=5)
rural_dev_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
rural_dev_sb.grid(row=0, column=7, sticky=W, padx=5)

# Sales Tax
Button(policies_fr, text="Sales Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Sales Tax"))\
    .grid(row=1, column=6, sticky=W, padx=5)
sales_tax_sb = Spinbox(policies_fr, from_=0, to=50, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
sales_tax_sb.grid(row=1, column=7, sticky=W, padx=5)

# Satellite Road Pricing
Button(policies_fr, text="Satellite Road Pricing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Satellite Road Pricing"))\
    .grid(row=2, column=6, sticky=W, padx=5)
sat_rd_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sat_rd_sb.grid(row=2, column=7, sticky=W, padx=5)

# Sub. School Bus
Button(policies_fr, text="Sub. School Bus", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Sub. School Bus"))\
    .grid(row=3, column=6, sticky=W, padx=5)
sub_sch_bus_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sub_sch_bus_sb.grid(row=3, column=7, sticky=W, padx=5)

# School Prayers
Button(policies_fr, text="School Prayers", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("School Prayers"))\
    .grid(row=4, column=6, sticky=W, padx=5)
prayer_sb = Spinbox(policies_fr, values=SLIDERS["prayer"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prayer_sb.grid(row=4, column=7, sticky=W, padx=5)

# Science Funding
Button(policies_fr, text="Science Funding", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Science Funding"))\
    .grid(row=5, column=6, sticky=W, padx=5)
science_sb = Spinbox(policies_fr, values=SLIDERS["science"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
science_sb.grid(row=5, column=7, sticky=W, padx=5)

# Small Bus. Grants
Button(policies_fr, text="Small Bus. Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Small Business Grants"))\
    .grid(row=6, column=6, sticky=W, padx=5)
small_business_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
small_business_sb.grid(row=6, column=7, sticky=W, padx=5)

# Space Program
Button(policies_fr, text="Space Program", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Space Program"))\
    .grid(row=7, column=6, sticky=W, padx=5)
space_sb = Spinbox(policies_fr, values=SLIDERS["space"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
space_sb.grid(row=7, column=7, sticky=W, padx=5)

# Speed Cameras
Button(policies_fr, text="Speed Cameras", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Speed Cameras"))\
    .grid(row=8, column=6, sticky=W, padx=5)
speed_sb = Spinbox(policies_fr, values=SLIDERS["speed"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
speed_sb.grid(row=8, column=7, sticky=W, padx=5)

#  State Health Service
Button(policies_fr, text="State Health Service", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Health Service"))\
    .grid(row=9, column=6, sticky=W, padx=5)
health_sb = Spinbox(policies_fr, values=SLIDERS["health"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
health_sb.grid(row=9, column=7, sticky=W, padx=5)

# State Housing
Button(policies_fr, text="State Housing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Housing"))\
    .grid(row=10, column=6, sticky=W, padx=5)
housing_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
housing_sb.grid(row=10, column=7, sticky=W, padx=5)

# State Pensions
Button(policies_fr, text="State Pensions", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Pensions"))\
    .grid(row=11, column=6, sticky=W, padx=5)
pension_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pension_sb.grid(row=11, column=7, sticky=W, padx=5)

# State Schools
Button(policies_fr, text="State Schools", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Schools"))\
    .grid(row=12, column=6, sticky=W, padx=5)
sschools_sb = Spinbox(policies_fr, values=SLIDERS["schools"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sschools_sb.grid(row=12, column=7, sticky=W, padx=5)

# Stem Cell Research
Button(policies_fr, text="Stem Cell Research", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Stem Cell Research"))\
    .grid(row=13, column=6, sticky=W, padx=5)
stem_cell_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
stem_cell_sb.grid(row=13, column=7, sticky=W, padx=5)

# Tax Shelters
Button(policies_fr, text="Tax Shelters", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Tax Shelters"))\
    .grid(row=14, column=6, sticky=W, padx=5)
tax_shelter_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tax_shelter_sb.grid(row=14, column=7, sticky=W, padx=5)

# Technology Colleges
Button(policies_fr, text="Technology Colleges", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Technology Colleges"))\
    .grid(row=15, column=6, sticky=W, padx=5)
tech_college_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tech_college_sb.grid(row=15, column=7, sticky=W, padx=5)

# Technology Grants
Button(policies_fr, text="Technology Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Technology Grants"))\
    .grid(row=16, column=6, sticky=W, padx=5)
tech_grant_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tech_grant_sb.grid(row=16, column=7, sticky=W, padx=5)

# Telecommuting Initiative
Button(policies_fr, text="Telecommuting", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Telecommuting"))\
    .grid(row=17, column=6, sticky=W, padx=5)
telecommute_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
telecommute_sb.grid(row=17, column=7, sticky=W, padx=5)

# Tobacco Tax
Button(policies_fr, text="Tobacco Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Tobacco Tax"))\
    .grid(row=18, column=6, sticky=W, padx=5)
tobac_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
tobac_tax_sb.grid(row=18, column=7, sticky=W, padx=5)

# Toll Roads
Button(policies_fr, text="Toll Roads", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Toll Roads"))\
    .grid(row=19, column=6, sticky=W, padx=5)
toll_road_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
toll_road_sb.grid(row=19, column=7, sticky=W, padx=5)

# Unemployed Benefit 
Button(policies_fr, text="Unemployed Benefit", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Unemployed Benefit"))\
    .grid(row=20, column=6, sticky=W, padx=5)
unemployment_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
unemployment_sb.grid(row=20, column=7, sticky=W, padx=5)

# University Grants
Button(policies_fr, text="Uni Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Uni Grants"))\
    .grid(row=21, column=6, sticky=W, padx=5)
university_sb = Spinbox(policies_fr, values=SLIDERS["uni"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
university_sb.grid(row=21, column=7, sticky=W, padx=5)

# Welfare Fraud Dept.
Button(policies_fr, text="Welfare Fraud", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Welfare Fraud"))\
    .grid(row=22, column=6, sticky=W, padx=5)
wel_fraud_sb = Spinbox(policies_fr, values=SLIDERS["welfare"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
wel_fraud_sb.grid(row=22, column=7, sticky=W, padx=5)

# Winter Fuel Subsidy
Button(policies_fr, text="Winter Fuel", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Winter Fuel"))\
    .grid(row=23, column=6, sticky=W, padx=5)
winter_fuel_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
winter_fuel_sb.grid(row=23, column=7, sticky=W, padx=5)

# Work Safety Law
Button(policies_fr, text="Work Safety", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Work Safety"))\
    .grid(row=24, column=6, sticky=W, padx=5)
work_safe_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
work_safe_sb.grid(row=24, column=7, sticky=W, padx=5)

# Youth Club Subsidies
Button(policies_fr, text="Youth Clubs", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Youth Clubs"))\
    .grid(row=0, column=8, sticky=W, padx=5)
youth_club_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
youth_club_sb.grid(row=0, column=9, sticky=W, padx=5)

# Abortion Law
Button(policies_fr, text="Abortion Law", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Abortion Law"))\
    .grid(row=1, column=8, sticky=W, padx=5)
abortion_sb = Spinbox(policies_fr, values=SLIDERS["abortion"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
abortion_sb.grid(row=1, column=9, sticky=W, padx=5)

# Rent Controls
Button(policies_fr, text="Rent Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Rent Controls"))\
    .grid(row=2, column=8, sticky=W, padx=5)
rent_cont_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
rent_cont_sb.grid(row=2, column=9, sticky=W, padx=5)

# School Vouchers
Button(policies_fr, text="School Vouchers", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("School Vouchers"))\
    .grid(row=3, column=8, sticky=W, padx=5)
rent_cont_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
rent_cont_sb.grid(row=3, column=9, sticky=W, padx=5)

# Oil Drilling Subsidies
Button(policies_fr, text="Oil Drilling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Oil Drilling"))\
    .grid(row=4, column=8, sticky=W, padx=5)
oil_drilling_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
oil_drilling_sb.grid(row=4, column=9, sticky=W, padx=5)

# Mansion Tax
Button(policies_fr, text="Mansion Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Mansion Tax"))\
    .grid(row=5, column=8, sticky=W, padx=5)
mansion_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
mansion_sb.grid(row=5, column=9, sticky=W, padx=5)

# Fuel Efficiency Standards
Button(policies_fr, text="Fuel Efficiency", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Fuel Efficiency"))\
    .grid(row=6, column=8, sticky=W, padx=5)
fuel_eff_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
fuel_eff_sb.grid(row=6, column=9, sticky=W, padx=5)

# Foreign Investor Tax Breaks
Button(policies_fr, text="Foreign Invest.", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Foreign Invest."))\
    .grid(row=7, column=8, sticky=W, padx=5)
for_invest_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
for_invest_sb.grid(row=7, column=9, sticky=W, padx=5)

# Robotics Research Grants
Button(policies_fr, text="Robot Research", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Robot Research"))\
    .grid(row=8, column=8, sticky=W, padx=5)
robot_research_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
robot_research_sb.grid(row=8, column=9, sticky=W, padx=5)

# Private Prisons
Button(policies_fr, text="Private Prisons", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Private Prisons"))\
    .grid(row=9, column=8, sticky=W, padx=5)
prov_pris_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prov_pris_sb.grid(row=9, column=9, sticky=W, padx=5)

# Junk Food Tax
Button(policies_fr, text="Junk Food Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Junk Food Tax"))\
    .grid(row=10, column=8, sticky=W, padx=5)
junk_food_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT, state="readonly")
junk_food_sb.grid(row=10, column=9, sticky=W, padx=5)

# Health Food Subsidies
Button(policies_fr, text="Health Food", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Health Food Subsidies"))\
    .grid(row=11, column=8, sticky=W, padx=5)
health_food_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
health_food_sb.grid(row=11, column=9, sticky=W, padx=5)

# Tasers
Button(policies_fr, text="Tasers", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Tasers"))\
    .grid(row=12, column=8, sticky=W, padx=5)
tasers_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tasers_sb.grid(row=12, column=9, sticky=W, padx=5)

# Police Drones
Button(policies_fr, text="Police Drones", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Police Drones"))\
    .grid(row=13, column=8, sticky=W, padx=5)
police_drones_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
police_drones_sb.grid(row=13, column=9, sticky=W, padx=5)

# Arts Subsidies
Button(policies_fr, text="Arts Subsidies ", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Arts Subsidies"))\
    .grid(row=14, column=8, sticky=W, padx=5)
art_sub_sb = Spinbox(policies_fr, values=SLIDERS["arts"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
art_sub_sb.grid(row=14, column=9, sticky=W, padx=5)

# Healthcare Vouchers
Button(policies_fr, text="Healthcare Vouchers", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Healthcare Vouchers"))\
    .grid(row=15, column=8, sticky=W, padx=5)
health_vouch_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
health_vouch_sb.grid(row=15, column=9, sticky=W, padx=5)

# Health Tax Credits
Button(policies_fr, text="Health Tax Credits", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Health Tax Credits"))\
    .grid(row=16, column=8, sticky=W, padx=5)
health_tax_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
health_tax_sb.grid(row=16, column=9, sticky=W, padx=5)

# School Tax Credits
Button(policies_fr, text="School Tax Credits", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("School Tax Credits"))\
    .grid(row=17, column=8, sticky=W, padx=5)
school_tax_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
school_tax_sb.grid(row=17, column=9, sticky=W, padx=5)

# Food Stamps
Button(policies_fr, text="Food Stamps", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Food Stamps"))\
    .grid(row=18, column=8, sticky=W, padx=5)
food_stamps_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
food_stamps_sb.grid(row=18, column=9, sticky=W, padx=5)

# Food Standards Agency
Button(policies_fr, text="Food Stand. Agency", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Food Standards Agency"))\
    .grid(row=19, column=8, sticky=W, padx=5)
food_stand_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
food_stand_sb.grid(row=19, column=9, sticky=W, padx=5)

# Enterprise Investment Scheme
Button(policies_fr, text="Enter. Invest. Scheme", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Enterprise Investment Scheme"))\
    .grid(row=20, column=8, sticky=W, padx=5)
ent_invest_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
ent_invest_sb.grid(row=20, column=9, sticky=W, padx=5)

# Recreational Drugs Tax
Button(policies_fr, text="Rec. Drugs Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Recreational Drugs Tax"))\
    .grid(row=21, column=8, sticky=W, padx=5)
rec_drug_tax_sb = Spinbox(policies_fr, values=SLIDERS["default values"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
rec_drug_tax_sb.grid(row=21, column=9, sticky=W, padx=5)

# Gated Communities
Button(policies_fr, text="Gated Communities", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Gated Communities"))\
    .grid(row=22, column=8, sticky=W, padx=5)
gated_sb = Spinbox(policies_fr, values=SLIDERS["gated"], bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
gated_sb.grid(row=22, column=9, sticky=W, padx=5)

# *** Bottom button frame
buttons_fr = Frame(root, bg=BG_COLOUR)
buttons_fr.grid(row=3, column=0, columnspan= 2, sticky=E, padx=5)

# Save button
Button(buttons_fr, text="Save", width = 15, bg=BG_COLOUR, font=BUTTON).grid(row=0, column=0, padx=5, pady=10, sticky=E, command=save)

# Load button
Button(buttons_fr, text="Load", width = 15, bg=BG_COLOUR, font=BUTTON).grid(row=0, column=1, padx=5, pady=10, sticky=E, command=load)

# Export button
Button(buttons_fr, text="Export", width = 15, bg=BG_COLOUR, font=BUTTON).grid(row=0, column=2, padx=5, pady=10, sticky=E, command=export)


# **** run window loop ****
root.mainloop()