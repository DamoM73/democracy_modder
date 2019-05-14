''' this program allows users to create their own country for Democracy 3 '''
from tkinter import *
from tkinter import messagebox

WIDTH = 1300
HEIGHT = 800

# formatting
BG_COLOUR = "light grey"
ENTRY_COLOUR = "white"
HEADING_1 = ("Arial",16)
HEADING_2 = ("Arial",12)
BODY = ("Arial",10)
SB_WIDTH = 15

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
    "adult ed" : "Adult education subsidies are a way to encourage people to re-train and continue their education after they have joined the workforce. This includes evening classes and distance learning resources.\n\nThese schemes help to raise the overall educational level of the workforce.",
    "agriculture" : "For strategic reasons some governments are happy to pay subsidies to farmers to ensure the security of the nation's food supply.\n\nThis goes against free market economics and can also be very expensive, but it does safeguard jobs (and votes) in agricultural communities.",
    "airline" : "Airline fuel has generally not been subject to taxation.\n\nSupporters of air fuel taxes insist that this results in an unfair subsidy on an environmentally destructive form of transport.\n\nThe airlines point out that taxing airline fuel will just encourage them to refuel elsewhere thereby diverting funds from our economy.",
    "alcohol" : "There is ample evidence that excessive consumption of alcohol can lead to health problems and even premature death.\n\nHowever, some people object to the state interfering in an individual's right to choose what he/she drinks.\n\nThere is also the complication that the government can make a lot of money by taxing alcohol.",
    "alcohol tax" : "Medically there is a clear case for the government to tax alcohol in order to discourage consumption because of its negative effects on health and its possible links to social breakdown.\n\nOn the other hand, those who drink socially see the government benefiting from such a tax to be hypocritical.",
    "armed police" : "Arming police officers can be an effective strategy in deterring crime and maintaining order.\n\nOpponents would argue that it encourages criminals to use firearms in a 'criminal arms race'.\n\nCritics also worry that arming the police will distance them from law-abiding citizens.",
    "sun trade" : "The Christian religion generally recognizes the 'Sabbath' as a 'day of rest' and many religious people believe that there should be no shopping carried out on that day.\n\nSome trade unions also believe that an enforced day of rest prevents its members being exploited.",
    "biofuel" : "Biofuels can reduce oil demand, by mixing ethanol derived from corn with petro-chemical fuel.\n\nThis is generally popular with environmentalists.Farmers who earn money producing corn for biofuel use also benefit.\n\nBiofuels with a higher mix of ethanol can be subsidized through tax breaks.",
    "border" : "Without some kind of customs checks at the borders, your country is open to the problem of mass illegal immigration.\n\nSome people argue that these immigrants cause crime, others that they take jobs away from your own citizens.\n\nBorder controls can be effective in reducing illegal immigration.",
    "bus lanes" : "Setting aside specific lanes of a road for use only by buses (and perhaps taxis and motorbikes) is one way to get traffic flowing faster and avoid congestion. It also shortens journey times for public transport and therefore encourages usage.\n\nThere are noticeable costs involved in setting up such schemes, and motorists can be annoyed if the bus lanes seem empty while they remain stuck in traffic."
    }

# sliders
NAME_LISTS = ("Australia", "Canada", "France", "Germany", "UK", "USA")
DEFAULT_SLIDER = ("None", "Low", "Medium", "High", "Maximum")
ALCOHOL_SLIDER = ("No limits", "Min age 16", "Min age 18", "Min age 21", "Low stregnth beer", "Strong retrictions")
ARMED_POLICE_SLIDER = ("None","Specialists", "In every dept.", "Widespread", "Every Officer", "Submachineguns")
BORDER_SLIDER = ("Random checks", "Passport checks", "Biometric Checks", "Armed guards", "Retina Scans")



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
Button(country_fr,text="Name", bg=BG_COLOUR, font=BODY, width=9, anchor=W, relief=FLAT, command=lambda: help_message(INFO["country"]))\
    .grid(row=0, column=0, sticky=W)
name_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
name_ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# leader title
Button(country_fr,text="Leader Title", bg=BG_COLOUR, font=BODY, width=8, anchor=W, relief=FLAT, command=lambda: help_message(INFO["leader"]))\
    .grid(row=1, column=0, sticky=W)
leader_ent = Entry(country_fr, width=40, relief = FLAT, bg=ENTRY_COLOUR)
leader_ent.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# population
Button(country_fr,text="Pop (million)", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["pop"]))\
    .grid(row=0, column=2, sticky=W)
pop_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
pop_ent.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# currency symbol
Button(country_fr,text="Currency Symbol", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["currency"]))\
    .grid(row=1, column=2, sticky=W)
currency_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
currency_ent.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# max income
Button(country_fr,text="Max Income ('000)", bg=BG_COLOUR, font=BODY, width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_inc"]))\
    .grid(row=0, column=4, sticky=W)
max_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
max_inc_ent.grid(row=0, column=5, padx=5, pady=5)

# min income
Button(country_fr,text="Min Income ('000)", bg=BG_COLOUR, font=BODY, width=14, anchor=W, relief=FLAT, command=lambda: help_message(INFO["min_inc"]))\
    .grid(row=1, column=4, sticky=W)
min_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
min_inc_ent.grid(row=1, column=5, padx=5, pady=5)

# max gdp
Button(country_fr,text="Max GDP (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["max_gdp"]))\
    .grid(row=0, column=6, sticky=W)
max_gdp_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
max_gdp_ent.grid(row=0, column=7, padx=5, pady=5)

# debt
Button(country_fr,text="Debt (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message(INFO["debt"]))\
    .grid(row=1, column=6, sticky=W)
debt_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR)
debt_ent.grid(row=1, column=7, padx=5, pady=5)


# name file
Button(country_fr,text="Citizen Names", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["name_file"]))\
    .grid(row=2, column=6, sticky=W)
cit_name_sb = Spinbox(country_fr, values=NAME_LISTS, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=8)
cit_name_sb.grid(row=2, column=7, sticky=W, padx=5)

'''
# Economic Cycle
Button(country_fr,text="Global Economy", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["economy"]))\
    .grid(row=0, column=9, sticky=SW)
economic_control = IntVar()
Scale(country_fr, variable=economic_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=120, highlightbackground=BG_COLOUR)\
    .grid(row=1,column=9, sticky=NW)

# Wealth Indicator
Button(country_fr,text="Relavitve wealth", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message(INFO["wealth"]))\
    .grid(row=3, column=9, sticky=SW)
wealth_control = IntVar()
Scale(country_fr, variable=wealth_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=120, highlightbackground=BG_COLOUR, from_=1, to=25)\
    .grid(row=4, column=9, sticky=NW)
'''

# Description
Button(country_fr,text="Country Description", bg=BG_COLOUR, font=BODY, relief=FLAT, width=20, anchor=W, command=lambda: help_message(INFO["description"]))\
    .grid(row=0, column=8, sticky=W)
description_tb = Text(country_fr,width=35, height=10)
description_tb.grid(row=1, column=8, rowspan=4, sticky=W, padx=5, pady=5)


# ** Policies Frame
policies_fr = LabelFrame(root,text="Policies", font=HEADING_1, bg= BG_COLOUR)
policies_fr.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Adult Education Subsidies
Button(policies_fr, text="Adult Education", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["adult ed"]))\
    .grid(row=0, column=0, sticky=W, padx=5)
ad_ed_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
ad_ed_sb.grid(row=0, column=1, sticky=W, padx=5)

# Agriculture Subsidies
Button(policies_fr, text="Agriculture Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["agriculture"]))\
    .grid(row=1, column=0, sticky=W, padx=5)
agri_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
agri_sb.grid(row=1, column=1, sticky=W, padx=5)

# Airline Tax
Button(policies_fr, text="Airline Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["airline"]))\
    .grid(row=2, column=0, sticky=W, padx=5)
airline_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
airline_tax_sb.grid(row=2, column=1, sticky=W, padx=5)

# Alcohol Law
Button(policies_fr, text="Alcohol Law", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["alcohol"]))\
    .grid(row=3, column=0, sticky=W, padx=5)
alco_sb = Spinbox(policies_fr, values=ALCOHOL_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
alco_sb.grid(row=3, column=1, sticky=W, padx=5)

# Alcohol Tax
Button(policies_fr, text="Alcohol Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["alcohol tax"]))\
    .grid(row=4, column=0, sticky=W, padx=5)
alco_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
alco_tax_sb.grid(row=4, column=1, sticky=W, padx=5)

# Armed Police
Button(policies_fr, text="Armed Police", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["armed police"]))\
    .grid(row=5, column=0, sticky=W, padx=5)
arm_pol_sb = Spinbox(policies_fr, values=ARMED_POLICE_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
arm_pol_sb.grid(row=5, column=1, sticky=W, padx=5)

# Ban Sunday Shopping
Button(policies_fr, text="Ban Sunday Shopping", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["sun trade"]))\
    .grid(row=6, column=0, sticky=W, padx=5)
sun_trade_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sun_trade_sb.grid(row=6, column=1, sticky=W, padx=5)

# Biofuel Subsidies
Button(policies_fr, text="Biofuel Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["biofuel"]))\
    .grid(row=7, column=0, sticky=W, padx=5)
biofuel_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
biofuel_sb.grid(row=7, column=1, sticky=W, padx=5)

# Border Controls
Button(policies_fr, text="Border Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["border"]))\
    .grid(row=8, column=0, sticky=W, padx=5)
border_sb = Spinbox(policies_fr, values=BORDER_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
border_sb.grid(row=8, column=1, sticky=W, padx=5)

# Bus Lanes
Button(policies_fr, text="Bus Lanes", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message(INFO["bus lanes"]))\
    .grid(row=9, column=0, sticky=W, padx=5)
bus_lane_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_lane_sb.grid(row=9, column=1, sticky=W, padx=5)

# **** run window loop ****
root.mainloop()