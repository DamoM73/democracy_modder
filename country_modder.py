''' this program allows users to create their own country for Democracy 3 '''
from tkinter import *
from tkinter import messagebox

WIDTH = 1300
HEIGHT = 950

# formatting
BG_COLOUR = "light grey"
ENTRY_COLOUR = "white"
HEADING_1 = ("Arial",16)
HEADING_2 = ("Arial",12)
BODY = ("Arial",9)
SB_WIDTH = 17

INFO = {"Country Name" : "The common name of the country.\nFor example, Australia.",
    "Leader Title" : "The common title for the leader of the country.\nFor example, President.",
    "Population" : "The number of people residing in the country (in millions).",
    "Currency Symbol" : "The symbol the country uses to denote currency.\n For example $.",
    "Max Income" : "The highest annual salary in your country (in thousands).",
    "Min Income" : "The lowest annual salary in your country (in thousands).",
    "Max GDP" : "The historical highest value of the country's\nGross Domestic Product (in millions).",
    "Debt" : "The federal government's debt (in millions).",
    "Citizen Names" : "The basis for the possilbe first and last names of the citizens of the country.",
    "Global Economy" : "The global economic cycle works on a sine wave.\nAt 25 the world economy is at peak of growth,\nat 75 it is at the trough of growth.",
    "Relavitve wealth" : "How wealthy is the country compared to other nations?\nFor example, USA would be 23, and Somalia would be 1",
    "Country Description" : "A short paragraph describing the higlights of the country",
    "Adult Education" : "Adult education subsidies are a way to encourage people to re-train and continue their education after they have joined the workforce. This includes evening classes and distance learning resources.\n\nThese schemes help to raise the overall educational level of the workforce.",
    "Agriculture Subsidies" : "For strategic reasons some governments are happy to pay subsidies to farmers to ensure the security of the nation's food supply.\n\nThis goes against free market economics and can also be very expensive, but it does safeguard jobs (and votes) in agricultural communities.",
    "Airline Tax" : "Airline fuel has generally not been subject to taxation.\n\nSupporters of air fuel taxes insist that this results in an unfair subsidy on an environmentally destructive form of transport.\n\nThe airlines point out that taxing airline fuel will just encourage them to refuel elsewhere thereby diverting funds from our economy.",
    "Alcohol Law" : "There is ample evidence that excessive consumption of alcohol can lead to health problems and even premature death.\n\nHowever, some people object to the state interfering in an individual's right to choose what he/she drinks.\n\nThere is also the complication that the government can make a lot of money by taxing alcohol.",
    "Alcohol Tax" : "Medically there is a clear case for the government to tax alcohol in order to discourage consumption because of its negative effects on health and its possible links to social breakdown.\n\nOn the other hand, those who drink socially see the government benefiting from such a tax to be hypocritical.",
    "Armed Police" : "Arming police officers can be an effective strategy in deterring crime and maintaining order.\n\nOpponents would argue that it encourages criminals to use firearms in a 'criminal arms race'.\n\nCritics also worry that arming the police will distance them from law-abiding citizens.",
    "Ban Sunday Shopping" : "The Christian religion generally recognizes the 'Sabbath' as a 'day of rest' and many religious people believe that there should be no shopping carried out on that day.\n\nSome trade unions also believe that an enforced day of rest prevents its members being exploited.",
    "Biofuel Subsidies" : "Biofuels can reduce oil demand, by mixing ethanol derived from corn with petro-chemical fuel.\n\nThis is generally popular with environmentalists.Farmers who earn money producing corn for biofuel use also benefit.\n\nBiofuels with a higher mix of ethanol can be subsidized through tax breaks.",
    "Border Controls" : "Without some kind of customs checks at the borders, your country is open to the problem of mass illegal immigration.\n\nSome people argue that these immigrants cause crime, others that they take jobs away from your own citizens.\n\nBorder controls can be effective in reducing illegal immigration.",
    "Bus Lanes" : "Setting aside specific lanes of a road for use only by buses (and perhaps taxis and motorbikes) is one way to get traffic flowing faster and avoid congestion. It also shortens journey times for public transport and therefore encourages usage.\n\nThere are noticeable costs involved in setting up such schemes, and motorists can be annoyed if the bus lanes seem empty while they remain stuck in traffic.",
    "Bus Subsidies" : "Traffic congestion and pollution can be reduced by encouraging people to travel by bus instead of car.\n\nIt can be an expensive option though, and some motorists may resent a transport system they do not use being subsidized.",
    "Carbon Tax" : "A carbon tax is a tax levied on all emissions of Carbon Dioxide, thought to be the main cause of climate change.\n\nThe tax is effectively a pollution tax, and a way to make those individuals and industries who contribute to climate change pay for the damage they cause or to reduce emissions.\n\nObviously the tax is popular with environmentalists, and can also lead to a more energy efficient economy.",
    "Car Emission Limits" : "Setting legal limits on exhaust fumes helps to reduce air pollution, especially in cities,\nbut it's unpopular with motorists who look upon it as yet more bureaucracy and tax.",
    "Car Tax": "Taxing the ownership of all motor vehicles is one way to persuade people to use alternative forms of transport.\n\nIt can be argued however, that such a system increases the fixed costs of car ownership, encouraging people to use a car more once they have gone to the trouble of taxing it.\n\nThere is also an argument that this is a tax that unfairly hits the poor and people in rural communities where a car is a necessity.",
    "CCTV Cameras" : "CCTV cameras can be a great help in catching criminals and cameras also deter crime.\n\nThe installation costs are extremely high, and there are concerns about civil rights from people who don't like to feel that the government is constantly watching them.",
    "Child Benefit" : "A fixed payment made by the state directly to parents to assist in the cost of bringing up children.\n\nPopular with parents for obvious reasons, and the poor who see it as a redistributive tax, but capitalists are opposed to such an unnecessary level of interference by government.",
    "Childcare Provision" : "By giving state subsidies for childcare, we can ensure more parents return to the workforce after having children, and therefore benefit the economy.\n\nAlthough this can be expensive, and is also a distortion of the market, it is popular with parents.",
    "Citizenship Tests" : "Citizenship tests are a way of ensuring that people migrating to our country have a demonstrable understanding of our culture and history.\n\nThis lessens the chances of a clash of cultures for newcomers to the country, encourages integration and reassures patriotic members of society that they need not fear immigration.",
    "Clean Energy Subsidies" : "Renewable energy might not be ultra efficient yet, but there is an argument for investing heavily in it now so as to strategically prepare our country for a future without fossil fuels.\n\nEnvironmentalists are happy for obvious reasons, but capitalists see it as an unwelcome distortion of the energy market.",
    "Clean Fuel Subsidy" : "A Subsidy for cleaner fuels such as Ultra-Low Sulfur fuel in an effort to reduce the environmental impact of motoring.\n\nThe subsidy will reduce the costs of fitting catalytic converters to older cars, and provide an incentive at the  pump to choose less damaging fuels.",
    "Community Policing" : "Working with the community rather than attempting to control it. Community policing encourages the police to better understand the needs of the local community, especially in areas with ethnic minorities.\n\nCritics see it as an expensive waste of money which could be spent on more direct methods to cut crime.",
    "Consumer Rights" : "At a minimum level, the state guarantees that the consumer is not totally ripped off.\n\nAt the other end of the spectrum, draconian legislation can benefit the consumer at the expense of business.\n\nCompanies often complain about the amount of legislation governing selling to the public.",
    "Corporation Tax" : "A direct and proportionate tax on the profits of business.\n\nSome argue that this should be the only form of taxation, others that such taxes stifle entrepreneurship and discourage people from starting a business.\n\nIt is often one of the main ways the government brings in money.",
    "Creationism vs. Evolution" : "A bitter battle has raged about the way children are taught evolution versus creationism.\n\nScientists and Liberals consider it obvious that evidence based evolution should be taught in science classes.\n\nSome religious groups feel that it is wrong to teach evolution or 'Darwinism' as fact, when it remains an unproven theory or that creationism should be taught as an alternative theory in science.\n\nThe government has to decide what is taught in our schools.",
    "Curfews" : "Introduced for a short period of time in state of national emergency. These can be an effective way to combat crime at the cost of much personal liberty.\n\nOften, however, limiting the ability of peaceful citizens to leave their homes at night can be a sign of a country's degeneration into severe authoritarianism.",
    "Death Penalty" : "The death penalty is the ultimate punishment for serious crimes.\n\nOpponents are concerned by the possibility of killing the wrong person, and suggest that only a barbaric state has the death penalty.\n\nSupporters point out that it absolutely guarantees no re-offending, and acts as a deterrent to serious crime.",
    "Detention Without Trial" : "Detention without trial allows your police and security services to detain suspects when they do not have sufficient evidence (or cannot reveal sensitive evidence) to convict suspects.\n\nThis can be justified in the name of preventing terrorism, but Liberals are concerned that this infringes human-rights.",
    "Disability Benefit" : "A direct payment from the state to disabled people to allow for the fact that they are possibly unable, or need assistance to work.\n\nAdditionally many disabled people have special requirements in terms of transport or housing.",
    "Faith School Subsidies" : "Religious schools can achieve good academic standards.\n\nTheir supporters make a case that the government should subsidize methods of education that are proven to be effective.\n\nCritics say that religion has no place in education and that the government cannot be seen to 'push' a particular religion on children.",
    "Foreign Aid" : "Some foreign countries have very poor economies, poor education or food shortages, and it can be argued that relatively rich nations such as ours have a moral duty to help them.\n\nOthers may argue that the first priority of any nation is to its own citizens, and if those citizens wish to help, they can do so individually through charities.",
    "Free Bus Passes" : "Traditionally, free bus travel is offered as a concession to those citizens of retirement age.\n\nThis can be expensive, but it’s a great way to reduce car usage and thus reduce pollution and congestion.\n\nSome oppose such a distortion of the market however.",
    "Free Eye Tests" : "Eye tests catch problems early and advise those with poor eyesight that they need glasses.\n\nGetting your eyes tested privately can be expensive, and it's a luxury many people just do without.\n\nSocialists believe that the universal provision of free eye tests are essential in providing a health 'safety net' for all.",
    "Free School Meals" : "Not only are free school meals a way of redistributing wealth by ensuring everyone can afford to feed their children.\n\nIt's also a way to ensure that children eat healthily rather than surviving purely on junk food.",
    "Gambling" : "To some, gambling is a sin which leads to poverty and disaster.\n\nOthers believe that some 'social' gambling is harmless fun which can also be taxed nicely by the government as an additional form of revenue.\n\nIt also encourages tourism and creates jobs.",
    "Graduate tax" : "A graduate tax is a deciated tax levied purely on people graduating from university, as a way of them contributing to the cost of their university tuition.\n\nSupporters say this is fair because not everyone benefits from a university education.\n\nOpponents argue that it creates a disincentive to study purely academic subjects and the arts, as well as penalizing ambition.",
    "Handgun Laws" : "Some countries allow the virtually unrestricted ownership of any kind of firearm, whereas in others it is strictly controlled.\n\nSome people talk of the basic right to defend yourself, others are concerned that gun ownership leads to gun crime.",
    "Hybrid Cars" : "Hybrid cars are less damaging to the environment, because at slower speeds they use electric engines that produce no CO2. They also get higher fuel efficiency, thus reducing demand for oil.\n\nThe downside is they are very expensive, but tax incentives can encourage more people to buy hybrid models when they get new cars.",
    "ID Cards" : "Some say ID Cards act as a powerful deterrent against terrorism and other serious crimes.\n\nLiberals would argue that it is an infringement of an individual's civil liberties for the state to demand that citizens identify themselves on the spot.",
    "Import Tariffs" : "Cheap imports can be damaging to the economy because local companies cannot match the lower salaries paid by foreign competitors.\n\nImport tariffs help to protect local manufacturers from 'unfair' competition.\n\nThis does go against real free-market economics though, and can be seen as being unfair to foreign countries, possibly sparking retaliation.",
    "Income Tax" : "One of the most popular ways to raise money for government is a direct tax on peoples earnings, deducted at source by their employer.\n\nIncome tax is generally a progressive tax (the wealthy pay more as a fraction of their income than the poor) and for this reason it is popular with socialists and the low paid."
    }

# sliders
NAME_LISTS = ("Australia", "Canada", "France", "Germany", "UK", "USA")
DEFAULT_SLIDER = ("None", "Low", "Medium", "High", "Maximum")
ALCOHOL_SLIDER = ("No limits", "Min age 16", "Min age 18", "Min age 21", "Low stregnth beer", "Strong retrictions")
ARMED_POLICE_SLIDER = ("None","Specialists", "In every dept.", "Widespread", "Every Officer", "Submachineguns")
BORDER_SLIDER = ("Random checks", "Passport checks", "Biometric Checks", "Armed guards", "Retina Scans")
CCTV_SLIDER = ("None","Crime spots only", "Town centres", "Widespread", "Every street corner", "Facial recognistion")
CONSUMER_SLIDER = ("None", "Limited rights", "Right to return goods", "Automated refunds", "Cooling-off periods")
CREATION_SLIDER = ("Creation only", "Creation emphasis", "Both systems", "Evolution emphasis", "Evolution only")
CURFEWS_SLIDER = ("None", "For under 16s", "In certain areas", "1am to 3am", "12am to 6am", "10pm to 8am")
DEATH_SLIDER = ("None", "Mass murderers", "Homicide", "Homicide & rape", "Violent Crime", "Serious crime", "Most crime")
DETENTION_SLIDER = ("None", "72 hours", "7 days", "30 days", "90 days", "Unlimited")
GAMBLING_SLIDER = ("None", "Age and stakes limited", "No stakes limit", "No restrictions")
HANDGUN_SLIDER = ("No limit", "No machineguns", "No automatics", "Licence required", "Licence & min age", "Strict controls", "Total ban")
ID_SLIDER = ("Voluntary", "Widespread", "Compulsory", "Biometric", "Heavily enforced")



# **** Functions ****
def help_message(key):
    messagebox.showinfo(key+" Explanation", INFO[key])


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
Button(country_fr,text="Country Name", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Country Name"))\
    .grid(row=0, column=0, sticky=W)
name_ent = Entry(country_fr, width=35, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
name_ent.grid(row=0, column=1, padx=5, pady=5, sticky=W)

# leader title
Button(country_fr,text="Leader Title", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Leader Title"))\
    .grid(row=1, column=0, sticky=W)
leader_ent = Entry(country_fr, width=35, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
leader_ent.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# citizen names
Button(country_fr,text="Citizen Names", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Citizen Names"))\
    .grid(row=2, column=0, sticky=W)
cit_name_sb = Spinbox(country_fr, values=NAME_LISTS, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=34)
cit_name_sb.grid(row=2, column=1, sticky=W, padx=5)

# Economic Cycle
Button(country_fr,text="Global Economy", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Global Economy"))\
    .grid(row=3, column=0, sticky=W)
economic_control = IntVar()
Scale(country_fr, variable=economic_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=252, highlightbackground=BG_COLOUR)\
    .grid(row=3,column=1, sticky=NW)

# population
Button(country_fr,text="Pop (million)", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Population"))\
    .grid(row=0, column=2, sticky=W)
pop_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
pop_ent.grid(row=0, column=3, padx=5, pady=5, sticky=W)

# currency symbol
Button(country_fr,text="Currency Symbol", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Currency Symbol"))\
    .grid(row=1, column=2, sticky=W)
currency_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
currency_ent.grid(row=1, column=3, padx=5, pady=5, sticky=W)

# max income
Button(country_fr,text="Max Income ('000)", bg=BG_COLOUR, font=BODY, width=14, anchor=W, relief=FLAT, command=lambda: help_message("Max Income"))\
    .grid(row=0, column=4, sticky=W)
max_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
max_inc_ent.grid(row=0, column=5, padx=5, pady=5)

# min income
Button(country_fr,text="Min Income ('000)", bg=BG_COLOUR, font=BODY, width=14, anchor=W, relief=FLAT, command=lambda: help_message("Min Income"))\
    .grid(row=1, column=4, sticky=W)
min_inc_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
min_inc_ent.grid(row=1, column=5, padx=5, pady=5)

# max gdp
Button(country_fr,text="Max GDP (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Max GDP"))\
    .grid(row=2, column=2, sticky=W)
max_gdp_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
max_gdp_ent.grid(row=2, column=3, padx=5, pady=5)

# debt
Button(country_fr,text="Debt (millions)", bg=BG_COLOUR, font=BODY, width=15, anchor=W, relief=FLAT, command=lambda: help_message("Debt"))\
    .grid(row=2, column=4, sticky=W)
debt_ent = Entry(country_fr, width=10, relief = FLAT, bg=ENTRY_COLOUR, font=BODY)
debt_ent.grid(row=2, column=5, padx=5, pady=5)

# Wealth Indicator
Button(country_fr,text="Relavitve wealth", bg=BG_COLOUR, font=BODY, width=13, anchor=W, relief=FLAT, command=lambda: help_message("Relavitve wealth"))\
    .grid(row=3, column=2, sticky=W)
wealth_control = IntVar()
Scale(country_fr, variable=wealth_control, orient=HORIZONTAL, bg=BG_COLOUR, relief=FLAT, length=270, highlightbackground=BG_COLOUR, from_=1, to=25)\
    .grid(row=3, column=3, sticky=NW, columnspan=3)

# Description
Button(country_fr,text="Country Description", bg=BG_COLOUR, font=BODY, relief=FLAT, width=20, anchor=W, command=lambda: help_message("Country Description"))\
    .grid(row=0, column=8, sticky=W)
description_tb = Text(country_fr,width=63, height=6)
description_tb.grid(row=1, column=8, rowspan=3, sticky=W, padx=5, pady=5)

# ** Policies Frame
policies_fr = LabelFrame(root,text="Policies", font=HEADING_1, bg= BG_COLOUR)
policies_fr.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Adult Education Subsidies
Button(policies_fr, text="Adult Education", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Adult Education"))\
    .grid(row=0, column=0, sticky=W, padx=5)
ad_ed_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
ad_ed_sb.grid(row=0, column=1, sticky=W, padx=5)

# Agriculture Subsidies
Button(policies_fr, text="Agriculture Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Agriculture Subsidies"))\
    .grid(row=1, column=0, sticky=W, padx=5)
agri_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
agri_sb.grid(row=1, column=1, sticky=W, padx=5)

# Airline Tax
Button(policies_fr, text="Airline Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Airline Tax"))\
    .grid(row=2, column=0, sticky=W, padx=5)
airline_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
airline_tax_sb.grid(row=2, column=1, sticky=W, padx=5)

# Alcohol Law
Button(policies_fr, text="Alcohol Law", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Alcohol Law"))\
    .grid(row=3, column=0, sticky=W, padx=5)
alco_sb = Spinbox(policies_fr, values=ALCOHOL_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
alco_sb.grid(row=3, column=1, sticky=W, padx=5)

# Alcohol Tax
Button(policies_fr, text="Alcohol Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Alcohol Tax"))\
    .grid(row=4, column=0, sticky=W, padx=5)
alco_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
alco_tax_sb.grid(row=4, column=1, sticky=W, padx=5)

# Armed Police
Button(policies_fr, text="Armed Police", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Armed Police"))\
    .grid(row=5, column=0, sticky=W, padx=5)
arm_pol_sb = Spinbox(policies_fr, values=ARMED_POLICE_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
arm_pol_sb.grid(row=5, column=1, sticky=W, padx=5)

# Ban Sunday Shopping
Button(policies_fr, text="Ban Sunday Shopping", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Ban Sunday Shopping"))\
    .grid(row=6, column=0, sticky=W, padx=5)
sun_trade_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sun_trade_sb.grid(row=6, column=1, sticky=W, padx=5)

# Biofuel Subsidies
Button(policies_fr, text="Biofuel Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Biofuel Subsidies"))\
    .grid(row=7, column=0, sticky=W, padx=5)
biofuel_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
biofuel_sb.grid(row=7, column=1, sticky=W, padx=5)

# Border Controls
Button(policies_fr, text="Border Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Border Controls"))\
    .grid(row=8, column=0, sticky=W, padx=5)
border_sb = Spinbox(policies_fr, values=BORDER_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
border_sb.grid(row=8, column=1, sticky=W, padx=5)

# Bus Lanes
Button(policies_fr, text="Bus Lanes", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Bus Lanes"))\
    .grid(row=9, column=0, sticky=W, padx=5)
bus_lane_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_lane_sb.grid(row=9, column=1, sticky=W, padx=5)

# Bus Subsidies
Button(policies_fr, text="Bus Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Bus Subsidies"))\
    .grid(row=10, column=0, sticky=W, padx=5)
bus_subs_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_subs_sb.grid(row=10, column=1, sticky=W, padx=5)

# Carbon Tax
Button(policies_fr, text="Carbon Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Carbon Tax"))\
    .grid(row=11, column=0, sticky=W, padx=5)
carbon_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
carbon_tax_sb.grid(row=11, column=1, sticky=W, padx=5)

# Car Emission Limits
Button(policies_fr, text="Car Emission Limits", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Car Emission Limits"))\
    .grid(row=12, column=0, sticky=W, padx=5)
car_emissions_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
car_emissions_sb.grid(row=12, column=1, sticky=W, padx=5)

# Car Tax
Button(policies_fr, text="Car Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Car Tax"))\
    .grid(row=13, column=0, sticky=W, padx=5)
car_tax_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
car_tax_sb.grid(row=13, column=1, sticky=W, padx=5)

# CCTV Cameras
Button(policies_fr, text="CCTV Cameras", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("CCTV Cameras"))\
    .grid(row=14, column=0, sticky=W, padx=5)
cctv_sb = Spinbox(policies_fr, values=CCTV_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
cctv_sb.grid(row=14, column=1, sticky=W, padx=5)

# Child Benefit
Button(policies_fr, text="Child Benefit", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Child Benefit"))\
    .grid(row=15, column=0, sticky=W, padx=5)
child_benefit_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
child_benefit_sb.grid(row=15, column=1, sticky=W, padx=5)

# Childcare Provision
Button(policies_fr, text="Childcare Provision", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Childcare Provision"))\
    .grid(row=16, column=0, sticky=W, padx=5)
childcare_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
childcare_sb.grid(row=16, column=1, sticky=W, padx=5)

# Citizenship Tests
Button(policies_fr, text="Citizenship Tests", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Citizenship Tests"))\
    .grid(row=17, column=0, sticky=W, padx=5)
citizen_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
citizen_sb.grid(row=17, column=1, sticky=W, padx=5)

# Clean Energy Subsidies
Button(policies_fr, text="Clean Energy Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Clean Energy Subsidies"))\
    .grid(row=18, column=0, sticky=W, padx=5)
clean_energy_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
clean_energy_sb.grid(row=18, column=1, sticky=W, padx=5)

# Clean Fuel Subsidy
Button(policies_fr, text="Clean Fuel Subsidy", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Clean Fuel Subsidy"))\
    .grid(row=19, column=0, sticky=W, padx=5)
clean_fuel_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
clean_fuel_sb.grid(row=19, column=1, sticky=W, padx=5)

# Community Policing
Button(policies_fr, text="Community Policing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Community Policing"))\
    .grid(row=20, column=0, sticky=W, padx=5)
com_pol_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
com_pol_sb.grid(row=20, column=1, sticky=W, padx=5)

# Consumer Rights
Button(policies_fr, text="Consumer Rights", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Consumer Rights"))\
    .grid(row=21, column=0, sticky=W, padx=5)
consumer_rts_sb = Spinbox(policies_fr, values=CONSUMER_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
consumer_rts_sb.grid(row=21, column=1, sticky=W, padx=5)

# Corporation Tax
Button(policies_fr, text="Corporation Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Corporation Tax"))\
    .grid(row=22, column=0, sticky=W, padx=5)
corp_tax_sb = Spinbox(policies_fr, from_=1, to=50, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
corp_tax_sb.grid(row=22, column=1, sticky=W, padx=5)

# Creationism vs. Evolution
Button(policies_fr, text="Creationism vs. Evolution", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Creationism vs. Evolution"))\
    .grid(row=23, column=0, sticky=W, padx=5)
creationism_sb = Spinbox(policies_fr, values=CREATION_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
creationism_sb.grid(row=23, column=1, sticky=W, padx=5)

# Curfews
Button(policies_fr, text="Curfews", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Curfews"))\
    .grid(row=24, column=0, sticky=W, padx=5)
curfews_sb = Spinbox(policies_fr, values=CURFEWS_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
curfews_sb.grid(row=24, column=1, sticky=W, padx=5)

# Death Penalty
Button(policies_fr, text="Death Penalty", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Death Penalty"))\
    .grid(row=0, column=2, sticky=W, padx=5)
death_pen_sb = Spinbox(policies_fr, values=DEATH_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
death_pen_sb.grid(row=0, column=3, sticky=W, padx=5)

# Detention Without Trial
Button(policies_fr, text="Detention Without Trial", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Detention Without Trial"))\
    .grid(row=1, column=2, sticky=W, padx=5)
detention_sb = Spinbox(policies_fr, values=DETENTION_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
detention_sb.grid(row=1, column=3, sticky=W, padx=5)

# Disability Benefit
Button(policies_fr, text="Disability Benefit", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Disability Benefit"))\
    .grid(row=2, column=2, sticky=W, padx=5)
disability_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
disability_sb.grid(row=2, column=3, sticky=W, padx=5)

# Faith School Subsidies
Button(policies_fr, text="Faith School Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Faith School Subsidies"))\
    .grid(row=3, column=2, sticky=W, padx=5)
faith_schools_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
faith_schools_sb.grid(row=3, column=3, sticky=W, padx=5)

# Foreign Aid
Button(policies_fr, text="Foreign Aid", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Foreign Aid"))\
    .grid(row=4, column=2, sticky=W, padx=5)
foreign_aid_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
foreign_aid_sb.grid(row=4, column=3, sticky=W, padx=5)

# Bus Passes
Button(policies_fr, text="Free Bus Passes", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free Bus Passes"))\
    .grid(row=5, column=2, sticky=W, padx=5)
bus_passes_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
bus_passes_sb.grid(row=5, column=3, sticky=W, padx=5)

# Free Eye Tests
Button(policies_fr, text="Free Eye Tests", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free Eye Tests"))\
    .grid(row=6, column=2, sticky=W, padx=5)
eye_tests_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
eye_tests_sb.grid(row=6, column=3, sticky=W, padx=5)

# Free School Meals
Button(policies_fr, text="Free School Meals", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Free School Meals"))\
    .grid(row=7, column=2, sticky=W, padx=5)
school_meals_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
school_meals_sb.grid(row=7, column=3, sticky=W, padx=5)

# Gambling
Button(policies_fr, text="Gambling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Gambling"))\
    .grid(row=8, column=2, sticky=W, padx=5)
gambling_sb = Spinbox(policies_fr, values=GAMBLING_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
gambling_sb.grid(row=8, column=3, sticky=W, padx=5)

# Graduate tax
Button(policies_fr, text="Graduate tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Graduate tax"))\
    .grid(row=9, column=2, sticky=W, padx=5)
grad_tax_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
grad_tax_sb.grid(row=9, column=3, sticky=W, padx=5)

# Handgun Laws
Button(policies_fr, text="Handgun Laws", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Handgun Laws"))\
    .grid(row=10, column=2, sticky=W, padx=5)
handgun_sb = Spinbox(policies_fr, values=HANDGUN_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
handgun_sb.grid(row=10, column=3, sticky=W, padx=5)

# Hybrid Cars Initiative
Button(policies_fr, text="Hybrid Cars", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Hybrid Cars"))\
    .grid(row=11, column=2, sticky=W, padx=5)
hybrid_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
hybrid_sb.grid(row=11, column=3, sticky=W, padx=5)

# ID Cards
Button(policies_fr, text="ID Cards", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("ID Cards"))\
    .grid(row=12, column=2, sticky=W, padx=5)
id_sb = Spinbox(policies_fr, values=ID_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
id_sb.grid(row=12, column=3, sticky=W, padx=5)

# Import Tariffs
Button(policies_fr, text="Import Tariffs", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Import Tariffs"))\
    .grid(row=13, column=2, sticky=W, padx=5)
tariffs_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tariffs_sb.grid(row=13, column=3, sticky=W, padx=5)

# Income Tax
Button(policies_fr, text="Income Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Income Tax"))\
    .grid(row=14, column=2, sticky=W, padx=5)
income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
income_tax_sb.grid(row=14, column=3, sticky=W, padx=5)

# Flat Income Tax
Button(policies_fr, text="Flat Income Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Flat Income Tax"))\
    .grid(row=15, column=2, sticky=W, padx=5)
flat_income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
flat_income_tax_sb.grid(row=15, column=3, sticky=W, padx=5)

# Capital Gains Tax
Button(policies_fr, text="Capital Gains Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Capital Gains Tax"))\
    .grid(row=16, column=2, sticky=W, padx=5)
flat_income_tax_sb = Spinbox(policies_fr, from_=0, to=50, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
flat_income_tax_sb.grid(row=16, column=3, sticky=W, padx=5)



# **** run window loop ****
root.mainloop()