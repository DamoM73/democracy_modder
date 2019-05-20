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
BODY = ("Arial",8)
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
    "Income Tax" : "One of the most popular ways to raise money for government is a direct tax on peoples earnings, deducted at source by their employer.\n\nIncome tax is generally a progressive tax (the wealthy pay more as a fraction of their income than the poor) and for this reason it is popular with socialists and the low paid.",
    "Flat Income Tax" : "A flat-rate income tax is a tax where every citizen pays the same marginal rate of income tax regardless of their total income.\n\nAs a result, the cleaner in the office pays the same rate as the CEO, though the CEO's total tax bill will be higher.\n\nThis simpler structure can lead to lower avoidance and evasion.\n\nIt is not progressive, and can exacerbate income inequality.",
    "Capital Gains Tax" : "CGT is a tax levied on non-salary income such as stock market profits and share dividends, and profits from selling property or other assets.\n\nPrimarily it affects the wealthy and business owners, and will raise more money if the economy is booming.\n\nBecause it taxes profits from investments, it also acts as a slight deterrent to investment and thus be detrimental to the economy.",
    "Inheritance Tax" : "A tax paid on the wealth of an individual as it is passed on to their descendants.\n\nAn inheritance tax protects equality, by preventing families amassing wealth and advantage over the generations, so it is popular with socialists and the poor.\n\nHowever, some people are strongly opposed to anything that prevents them handing on their hard-earned wealth, especially their house, to their children.",
    "Intelligence Services" : "Security services are an essential tool in the fight against organized crime and terrorism.\n\nGood, reliable intelligence can be difficult and expensive to obtain, and in many cases the methods employed can be unpopular with liberals and human rights advocates.",
    "Internet Censorship" : "Liberals would suggest that the internet's greatest characteristic is its freedom from censorship and control, leading to an open and tolerant society.\n\nFreedom has its price however, and there is no shortage of material on the internet that can assist those with criminal intent.\n\nOpinion on what should and should not be censored on the web is bitterly divided.",
    "Internet Tax" : "As more and more commerce moves from conventional 'bricks and mortar' establishments to the web, governments are tempted to levy taxes on such transactions in order to 'level the playing field'.\n\nHowever, opponents of an internet tax claim that such a move would cripple the hi-tech economy and do enormous harm to the country's competitiveness.",
    "Jury Trial" : "The right to be tried by ordinary members of the public rather than a judge is seen as a fundamental human right by many liberals.\n\nConservatives argue that such a process is expensive, time wasting and is no fairer than a judge or a group of magistrates.\n\nIts entirely possible to have a system where a jury trial is reserved for more serious offences, with minor trials presided over by a magistrate.",
    "Labor Laws" : "Labor laws are basically restrictions on a worker's right to strike.\n\nCapitalists argue that such restrictions are vital to prevent key workers such as power station workers, policemen and train drivers from holding the country to ransom.\n\nTrade unionists consider the right to strike to be fundamental and not open to negotiation.",
    "Legal Aid" : "Not everyone has the money to pay a lawyer to defend themselves in court.\n\nAlthough a citizen could theoretically defend himself, providing state-employed lawyers should make for a fairer system.\n\nOn the other hand, this is basically a big subsidy to people who have already been charged with a crime but remember they are innocent until proved guilty.",
    "Legalize Prostitution" : "Conservatives claim that the legalization of prostitution would mark a severe decline in family values.\n\nOthers claim that as prostitution is unlikely to disappear, even if illegal, it's better for society and prostitutes that the practice is regulated and monitored rather than criminalized.",
    "Luxury Goods Tax" : "A tax aimed specifically at the high spenders in our society.\n\nA surcharge is added to high value luxuries such as sports cars, private yachts etc.\n\nAlthough it is never a vast source of income, a luxury goods tax can be popular with those people concerned with the gap between rich and poor.\n\nA luxury goods tax could encourage high earners to live and work elsewhere.",
    "Married Tax Allowance" : "This is a tax break for married couples, given as an encouragement for people to marry and also to stick together.\n\nChurch groups see it as essential that the state encourages traditional family values.\n\nSome see it as religion meddling in the tax system for no good reason.",
    "Maternity Leave" : "To some people, ensuring that mothers have a right to maternity leave and to return to their jobs afterwards is a sign of a civilized society, and one that encourages women to work.\n\nSome small businesses are concerned that it can put an unpredictable and even potentially crippling burden on an employer, especially where the number of employees is small.\n\nIt could be argued that this actually encourages employers not to employ women.",
    "Micro-Generation Grants" : "These grants are given to citizens to help subsidize the cost of energy micro-generation systems such as solar panels and wind turbines.\n\nThis is a good way to take advantage of some people's desire to make a personal step towards cleaner and greener energy, and will increase the country's overall energy efficiency.",
    "Military Spending" : "A modern, well equipped military can cost an absolute fortune, and many people feel that the money could best be spent elsewhere.\n\nOthers (especially patriots) would argue that you cannot put a price on freedom and security, and also point out the huge benefits for our businesses, technology and employment figures.",
    "National Monorail System" : "Monorails are often seen as the transport system of the future. They are promoted as being fast, reliable and environmentally beneficial.\n\nThe main problem however is the high cost.\n\nThe construction time is also a major consideration so investment in a national network would take a long time to give an eventually good payoff.",
    "Mortgage Tax Relief" : "This allows people to claim tax relief on the interest payments they have to make when they borrow money to buy a house.\n\nThis helps homebuyers to afford their mortgage payments, but can be resented by those who are not in a position to buy a house, as it is effectively a tax break for homebuyers.",
    "Narcotics" : "Should drugs such as cannabis and heroin be legalized?\n\nSupporters suggest that it is the crime associated with the buying black-market drugs that cause problems, and legalizing narcotics would reduce crime.\n\nOpponents point to the health risks and say it would be giving into criminals.",
    "National Service" : "Compulsory military service for some citizens where they are taught the basics of how to defend this country from attack has some benefits.\n\nFor example it would allow us to have a smaller regular army.\n\nHowever, there are concerns about forcing people to bear arms against their will.",
    "Organ Donation" : "There are few who would disagree that organ transplant is an amazing technology but it requires a plentiful supply of donors.\n\nSadly many people do not give the topic consideration.\n\nSome suggest that an 'opt-out' policy is best, with consent for donation assumed unless otherwise stated.\n\nOthers suggest that this is no place for the state to interfere and explicit permission should be requested.",
    "Organic Farming Subsidy" : "Supporters of organic farming say the state should subsidize this method of farming because of the perceived health benefits of food without artificial flavorings and additives.\n\nNaturally this is popular with farmers and environmentalists, but some people see it as a pointless distortion of what should be a free market.",
    "Petrol Tax" : "Taxing fuel can be a huge source of income for a government, and can also be seen as a 'green' policy by encouraging people to drive less, or to use more fuel efficient cars.\n\nCritics suggest that this is just another cynical tax on the motorist, and some complain that the alternative (public transport) is not a viable option for everyone.",
    "Wire Tapping" : "From a law and order perspective, wire tapping is an essential weapon in the fight against organized crime and terrorism.\n\nThe problem is that it's difficult to prevent misuse of such a system, and liberals are keen to point out how widespread wire tapping is a very sinister sign of a police state.",
    "Plastic Bag Tax" : "Plastic bags, unlike paper ones are not biodegradable so can last more or less forever, eventually ending up in huge unsightly landfill sites.\n\nA tax on bags discourages their use and encourages people to re-use stronger, more environmentally friendly alternatives.\n\nCapitalists just see this as the state meddling.",
    "Police Force" : "Every government needs to employ a police force to ensure order is kept and laws are obeyed, but it's a matter of debate exactly how much should be spent on the police.\n\nSome favor a large force with police on every street corner, other prefer a more low-key and tolerant approach.",
    "Pollution Controls" : "Restrictions on what chemicals and emissions can be released into the atmosphere.\n\nControls reduce pollution and increase health, possibly at the cost of economic competitiveness.",
    "Prisoner Tagging" : "A high tech alternative to incarceration that allows people to re-integrate with the community upon release from prison, whilst allowing law enforcement authorities to keep a close eye on them.\n\nLiberals have concerns that such a system is a step towards a police state which monitors our every move.",
    "Prisons" : "Some argue that providing the minimum number of bare, cold cells is the only provision that needs to be made for those who have broken the law.\n\nOthers suggest that spending more money allows for prisoners to be rehabilitated as well as punished and reduces the chances of reoffending.",
    "Property Tax" : "Property tax is a tax levied on the value of homes. The valuation is often made by a government body, and the money is used to fund local government services (at least in part) such as the provision of street lighting and emergency services.\n\nSome see it as a fair tax which mostly affects those who own large homes and are wealthy, others see it as an unfair tax on retired people with large homes but little actual income.",
    "Public Libraries" : "Public libraries provide a number of services:, acting as a focus for communities, providing access to information and literature to those on low incomes, and enabling people to learn new skills outside the normal educational establishment.",
    "Racial Profiling" : "Racial (or ethnic) profiling is the practice of using race as a factor in identifying criminals and potential criminals.\n\nLaw enforcement officials claim that using racial profiling allows them to quickly narrow down lists of potential suspects, and to best concentrate their efforts but opponents fear that it leads to racial discrimination by the police.",
    "Race Discrimination Act" : "Prevents citizens being discriminated against purely on the basis of race, i.e. racist employment practices etc.",
    "Rail Subsidies" : "Travelling by rail is not only more environmentally sound than car travel, its much more efficient in terms of transport times and congestion.\n\nOf course that requires adequate investment over the very long term, and in the meantime, motorists take offence at subsidizing a system they do not use.\n\nIt can take several years for the effects of rail investment to take effect.",
    "Recycling" : "Supporters of recycling argue that dumping waste in landfills just isn't a long term solution, and the government needs to show the way by providing facilities to recycle as many waste materials as possible.\n\nThis might include recycling newspapers, cardboard, bottles and even some plastics.",
    "Road Building" : "Although environmentalists often argue that more roads just lead to more congestion, not surprisingly this isn't how the motorist who is sat in traffic sees it.\n\nBuilding new roads is a very expensive and very slow process, but some suggest its vital to keep our economy functioning.",
    "Rural Development" : "As technology advances and more and more citizens take jobs in our cities, there is a danger that poverty and unemployment will rise to unacceptable levels in the countryside.\n\nRural development grants do distort the free market, but they also support rural businesses and prevent poverty amongst farmers and other rural occupations.",
    "Sales Tax" : "Sales tax is the classic 'regressive' tax, which means it does not take into account the ability to pay.\n\nCritics argue that this affects the poor disproportionately and thus increases inequality.\n\nSupporters argue that it is relatively easy to collect and affects everyone, and is thus fair.\n\nBusinesses can be opposed to the administrative burden of the tax.",
    "Satellite Road Pricing" : "An expensive system that requires transponders to be fitted to everyone's car and keeps track of what roads people use (and when).\n\nAllows per-road pricing for car usage which gives local authorities fine control over reducing congestion without burdening motorists in more remote rural areas who have no alternative transport system.",
    "Sub. School Bus" : "State subsidies for school buses ensure that every school kid has an efficient, and safe journey to school, whilst reducing the number of short 'school-run' trips carried out by parents, thus reducing traffic on the roads.\n\nParents are also happier knowing that there are proper approved school buses.",
    "School Prayers" : "Liberals will often argue that the education of our younger citizens should be kept entirely separate from any religious teachings.\n\nOn the other hand, it's argued that some compulsory prayer in schools is a way of promoting moral values in our children.",
    "Science Funding" : "In some countries, the majority of research is funded by private companies.\n\nState-sponsored science can be useful for investing in very long-term research projects or those that may not be commercially rewarding.\n\nThe benefits of state sector research are freely available to the entire population, rather than patented by corporations.",
    "Small Business Grants" : "The failure rate for small businesses is very high.\n\nIn the early years of trading, a preferential government grant can be an enormous help to get a new enterprise off the ground.\n\nThis can lead to a big boost to the economy, but it can also be an expensive policy with no guarantee of good results.",
    "Space Program" : "Invest in your country's efforts to explore space!\n\nAs well as the purely scientific benefits, a well-funded space program will boost the level of technological expertise throughout the entire economy.\n\nIt will also unite the country and encourage patriotism.",
    "Speed Cameras" : "Speed cameras are an automated way to enforce speed restrictions on our roads, without having to invest a fortune in extra traffic police.\n\nSupporters claim they reduce road deaths and free up the police to deal with more serious crime, opponents claim they are a cynical way of taxing the motorist and have nothing to do with safety",
    "State Health Service" : "Although many citizens would be happy to pay privately for their own health treatment, there is an argument that the state has a duty to provide a minimum level of free health treatment for everyone regardless of income.\n\nHealth provision can be expensive, so it's a matter of debate as to how much should be spent.",
    "State Housing" : "Some citizens prefer to own their own homes, but the cost of housing is such that a large proportion of the population live in rented accommodation.\n\nState housing is provided, at a reduced rate, to those who cannot afford to pay the market rate.\n\nThis can be expensive to fund, but the social benefits are also significant.",
    "State Pensions" : "Rather than leave it up to the individual to provide for themselves after retirement, state pensions can guarantee a minimum standard of living for the elderly.\n\nBe aware that as life expectancy rises, the cost to the state of paying out pensions increases hugely.\n\nThe level of state pension may encourage or discourage citizens to save into private pension plans.",
    "State Schools" : "Free education for all ensures high levels of literacy and can be beneficial to the economy, especially those parts of the economy requiring a skilled workforce.\n\nThe flipside of this is that state education can be expensive for the government.\n\nWealthy individuals, not making use of state schools, may resent subsidizing them.",
    "Stem Cell Research" : "A stem cell is a primitive type of cell that can be developed into most of the types of cells found in the human body.\n\nSome scientists claim that stem cell research offers great hope for curing diseases such as diabetes and multiple sclerosis.\n\nHowever, because stem cells are taken from discarded human embryos, many 'pro-life' and religious groups oppose their usage.",
    "Tax Shelters" : "By not fully taxing the wealth of the super-rich, tax shelters can be a great way to encourage successful entrepreneurs to make our country their home.\n\nWith an ever-shrinking world, the rich are free to settle wherever they please.\n\nEncouraging them to live here may mean that they spend their wealth in this country.\n\nSuch measures can be very unpopular with the poor, who resent paying tax on their much lower earnings.",
    "Technology Colleges" : "Technology colleges are 'specialist schools' with a focus on computer literacy, biotechnology and similar subjects.\n\nThese state-run colleges receive special funding from central government in order to encourage a greater level of technological literacy amongst the future workforce.",
    "Technology Grants" : "The government can provide state funding to encourage business to invest in new and exciting technologies.\n\nAlthough this helps give us a competitive advantage and can create jobs, it can be argued that its an unnecessary distortion of the market.",
    "Telecommuting" : "Telecommuting, or 'working from home' is seen as desirable because it reduces the pressure on the transport infrastructure, and can be an improvement to people's quality of life. It's also welcomed by parents.\n\nThis policy offers tax incentives to companies supporting this option.",
    "Tobacco Tax" : "Despite the failure of tobacco companies to admit it, there is good reason to believe that smoking has negative effects on health.\n\nThis is used as a justification for taxing tobacco.\n\nCynics point out that the government benefits hugely from a tax on a product it is supposedly against.\n\nHealth campaigners encourage the tax as a way to encourage a more healthy population",
    "Toll Roads" : "Toll roads charge motorists to use specific roads (normally major highways).\n\nThis is a great example of directly applying market forces, by only charging those who use a particular route for the construction and maintenance of that route.\n\nMotorists tend to see this as just another form of taxation, whereas commuters appreciate not being charged for roads they seldom use."
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
INTEL_SLIDER = ("A few spies", "Small spy agency", "Sizeable spy agency", "High tech spy service", "Spy satellite network")
INTERNET_CENSORSHIP_SLIDER = ("None", "In extreme cases", "On police request", "Some sites blocked", "All traffic monitored")
JURY_TRIAL_SLIDER = ("None", "In exceptional cases", "In serious cases", "If requested", "Widespread", "Universal")
LABOR_LAW_SLIDER = ("Pro-employer", "Balanced", "Pro-union")
MARRIED_TAX_SLIDER = ("None", "Small", "Advantageous", "Incentive")
MATERNITY_SLIDER = ("None", "Quarter pay", "Half pay", "Three quarters pay", "Full pay", "Full & paternity leave")
MILITARY_SLIDER = ("Ceremonial only", "Reservists", "Light defensive", "Well trained", "Highly trained", "Overwhelming force")
NARCOTICS_SLIDER = ("Outlawed", "Legalised cannabis", "Legal LSD", "Leagalise all drugs")
NATIONAL_SERVICE_SLIDER = ("None", "Basic training", "3 months service", "6 months service", "1 year service", "Periodic service")
ORGAN_SLIDER = ("By request", "Next of kin approved", "Presumed consent", "No opt-out")
WIRE_TAP_SLIDER = ("None", "Gov't decree", "Judicial order", "Police chief consent", "Police request", "Widespread use", "Universal monitoring")
POLLUTION_SLIDER = ("None", "Minimal monitoring", "Extensive monitoring", "Gov't targets", "Restrictions and fines", "Major fines")
PRISON_SLIDER = ("Overcrowded cells", "Shared cells", "Basic provisions", "Some re-education", "Extensive rehab.")
RECYCLING_SLIDER = ("None","Poster campaign", "Bottle Banks", "Recycling centers", "Limited doorstep collection", "Universal doorstep collection")
ROAD_SLIDER = ("Essential maintenance", "Basic maintenance", "Existing roads fixed", "Some expansion", "Major expansion", "New road networks")
PRAYER_SLIDER = ("None", "Parental request", "Optional", "Once weekly", "Daily", "Twice daily")
SCIENCE_SLIDER = ("Test-tubes", "Microscopes", "Electron microscope", "Particle accelerators")
SPACE_SLIDER = ("None", "Telescope", "Big telescopes", "Arrays of telescopes", "Satellites", "Unmanned probes", "Reusable shuttle", "Space stations")
SPEED_SLIDER = ("Trials", "Accident hotspots", "Outside Schools", "Residential areas", "Widespread", "Everywhere")
HEALTH_SLIDER = ("Life threatening", "Major ops", "Serious illness only", "Some prevention", "Excellent")
SCHOOLS_SLIDER = ("Wooden schoolhuts", "Shared textbooks", "Modern textbooks", "Student laptops")








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
flat_income_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
flat_income_tax_sb.grid(row=16, column=3, sticky=W, padx=5)

# Inheritance Tax
Button(policies_fr, text="Inheritance Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Inheritance Tax"))\
    .grid(row=17, column=2, sticky=W, padx=5)
inheritance_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
inheritance_tax_sb.grid(row=17, column=3, sticky=W, padx=5)

# Intelligence Services
Button(policies_fr, text="Intelligence Services", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Intelligence Services"))\
    .grid(row=18, column=2, sticky=W, padx=5)
intel_sb = Spinbox(policies_fr, values=INTEL_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
intel_sb.grid(row=18, column=3, sticky=W, padx=5)

# Internet Censorship
Button(policies_fr, text="Internet Censorship", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Internet Censorship"))\
    .grid(row=19, column=2, sticky=W, padx=5)
internet_censorship_sb = Spinbox(policies_fr, values=INTERNET_CENSORSHIP_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
internet_censorship_sb.grid(row=19, column=3, sticky=W, padx=5)

# Internet Tax
Button(policies_fr, text="Internet Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Internet Tax"))\
    .grid(row=20, column=2, sticky=W, padx=5)
internet_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
internet_tax_sb.grid(row=20, column=3, sticky=W, padx=5)

# Jury Trial
Button(policies_fr, text="Jury Trial", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Jury Trial"))\
    .grid(row=21, column=2, sticky=W, padx=5)
jury_trial_sb = Spinbox(policies_fr, values=JURY_TRIAL_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
jury_trial_sb.grid(row=21, column=3, sticky=W, padx=5)

# Labor Laws
Button(policies_fr, text="Labor Laws", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Labor Laws"))\
    .grid(row=22, column=2, sticky=W, padx=5)
labor_laws_sb = Spinbox(policies_fr, values=LABOR_LAW_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
labor_laws_sb.grid(row=22, column=3, sticky=W, padx=5)

# Legal Aid
Button(policies_fr, text="Legal Aid", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Legal Aid"))\
    .grid(row=23, column=2, sticky=W, padx=5)
legal_aid_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
legal_aid_sb.grid(row=23, column=3, sticky=W, padx=5)

# Legalize Prostitution
Button(policies_fr, text="Legalize Prostitution", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Legalize Prostitution"))\
    .grid(row=24, column=2, sticky=W, padx=5)
prostitution_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prostitution_sb.grid(row=24, column=3, sticky=W, padx=5)

# Luxury Goods Tax
Button(policies_fr, text="Luxury Goods Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Luxury Goods Tax"))\
    .grid(row=0, column=4, sticky=W, padx=5)
luxary_tax_sb = Spinbox(policies_fr, from_=0, to=90, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
luxary_tax_sb.grid(row=0, column=5, sticky=W, padx=5)

# Married Tax Allowance
Button(policies_fr, text="Married Tax Allowance", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Married Tax Allowance"))\
    .grid(row=1, column=4, sticky=W, padx=5)
married_tax_sb = Spinbox(policies_fr, values=MARRIED_TAX_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
married_tax_sb.grid(row=1, column=5, sticky=W, padx=5)

# Maternity Leave
Button(policies_fr, text="Maternity Leave", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Maternity Leave"))\
    .grid(row=2, column=4, sticky=W, padx=5)
maternity_sb = Spinbox(policies_fr, values=MATERNITY_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
maternity_sb.grid(row=2, column=5, sticky=W, padx=5)

# Micro-Generation Grants
Button(policies_fr, text="Micro-Generation Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Micro-Generation Grants"))\
    .grid(row=3, column=4, sticky=W, padx=5)
microgen_grants_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
microgen_grants_sb.grid(row=3, column=5, sticky=W, padx=5)

# Military Spending
Button(policies_fr, text="Military Spending", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Military Spending"))\
    .grid(row=4, column=4, sticky=W, padx=5)
military_sb = Spinbox(policies_fr, values=MILITARY_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
military_sb.grid(row=4, column=5, sticky=W, padx=5)

# National Monorail System
Button(policies_fr, text="National Monorail System", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("National Monorail System"))\
    .grid(row=5, column=4, sticky=W, padx=5)
monorail_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
monorail_sb.grid(row=5, column=5, sticky=W, padx=5)

# Mortgage Tax Relief
Button(policies_fr, text="Mortgage Tax Relief", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Mortgage Tax Relief"))\
    .grid(row=6, column=4, sticky=W, padx=5)
mortgage_relief_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
mortgage_relief_sb.grid(row=6, column=5, sticky=W, padx=5)

# Narcotics
Button(policies_fr, text="Narcotics", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Narcotics"))\
    .grid(row=7, column=4, sticky=W, padx=5)
narcotics_sb = Spinbox(policies_fr, values=NARCOTICS_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
narcotics_sb.grid(row=7, column=5, sticky=W, padx=5)

# National Service
Button(policies_fr, text="National Service", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("National Service"))\
    .grid(row=8, column=4, sticky=W, padx=5)
national_service_sb = Spinbox(policies_fr, values=NATIONAL_SERVICE_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
national_service_sb.grid(row=8, column=5, sticky=W, padx=5)

# Organ Donation
Button(policies_fr, text="Organ Donation", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Organ Donation"))\
    .grid(row=9, column=4, sticky=W, padx=5)
organ_donor_sb = Spinbox(policies_fr, values=ORGAN_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
organ_donor_sb.grid(row=9, column=5, sticky=W, padx=5)

# Organic Farming Subsidy
Button(policies_fr, text="Organic Farming Subsidy", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Organic Farming Subsidy"))\
    .grid(row=10, column=4, sticky=W, padx=5)
organic_farm_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
organic_farm_sb.grid(row=10, column=5, sticky=W, padx=5)

# Petrol Tax
Button(policies_fr, text="Petrol Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Petrol Tax"))\
    .grid(row=11, column=4, sticky=W, padx=5)
petrol_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
petrol_tax_sb.grid(row=11, column=5, sticky=W, padx=5)

# Wire Tapping
Button(policies_fr, text="Wire Tapping", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Wire Tapping"))\
    .grid(row=12, column=4, sticky=W, padx=5)
wire_tapping_sb = Spinbox(policies_fr, values=WIRE_TAP_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
wire_tapping_sb.grid(row=12, column=5, sticky=W, padx=5)

# Plastic Bag Tax
Button(policies_fr, text="Plastic Bag Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Plastic Bag Tax"))\
    .grid(row=13, column=4, sticky=W, padx=5)
plas_bag_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
plas_bag_sb.grid(row=13, column=5, sticky=W, padx=5)

# Police Force (compulsoray)
Button(policies_fr, text="Police Force", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Police Force"))\
    .grid(row=14, column=4, sticky=W, padx=5)
police_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
police_sb.grid(row=14, column=5, sticky=W, padx=5)

# Pollution Controls
Button(policies_fr, text="Pollution Controls", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Pollution Controls"))\
    .grid(row=15, column=4, sticky=W, padx=5)
pollution_sb = Spinbox(policies_fr, values=POLLUTION_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pollution_sb.grid(row=15, column=5, sticky=W, padx=5)

# Prisoner Tagging
Button(policies_fr, text="Prisoner Tagging", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Prisoner Tagging"))\
    .grid(row=16, column=4, sticky=W, padx=5)
pris_tag_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pris_tag_sb.grid(row=16, column=5, sticky=W, padx=5)

# Prisons
Button(policies_fr, text="Prisons", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Prisons"))\
    .grid(row=17, column=4, sticky=W, padx=5)
prisons_sb = Spinbox(policies_fr, values=PRISON_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prisons_sb.grid(row=17, column=5, sticky=W, padx=5)

# Property Tax
Button(policies_fr, text="Property Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Property Tax"))\
    .grid(row=18, column=4, sticky=W, padx=5)
prop_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
prop_tax_sb.grid(row=18, column=5, sticky=W, padx=5)

# Public Libraries
Button(policies_fr, text="Public Libraries", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Public Libraries"))\
    .grid(row=19, column=4, sticky=W, padx=5)
libraries_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
libraries_sb.grid(row=19, column=5, sticky=W, padx=5)

# Racial Profiling
Button(policies_fr, text="Racial Profiling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Racial Profiling"))\
    .grid(row=20, column=4, sticky=W, padx=5)
profiling_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
profiling_sb.grid(row=20, column=5, sticky=W, padx=5)

# Race Discrimination Act
Button(policies_fr, text="Race Discrimination Act", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Race Discrimination Act"))\
    .grid(row=21, column=4, sticky=W, padx=5)
discrimination_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
discrimination_sb.grid(row=21, column=5, sticky=W, padx=5)

# Rail Subsidies
Button(policies_fr, text="Rail Subsidies", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Rail Subsidies"))\
    .grid(row=22, column=4, sticky=W, padx=5)
discrimination_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
discrimination_sb.grid(row=22, column=5, sticky=W, padx=5)

# Recycling
Button(policies_fr, text="Recycling", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Recycling"))\
    .grid(row=23, column=4, sticky=W, padx=5)
recycling_sb = Spinbox(policies_fr, values=RECYCLING_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
recycling_sb.grid(row=23, column=5, sticky=W, padx=5)

# Road Building
Button(policies_fr, text="Road Building", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Road Building"))\
    .grid(row=24, column=4, sticky=W, padx=5)
roads_sb = Spinbox(policies_fr, values=ROAD_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
roads_sb.grid(row=24, column=5, sticky=W, padx=5)

# Rural Development Grants
Button(policies_fr, text="Rural Development", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Rural Development"))\
    .grid(row=0, column=6, sticky=W, padx=5)
rural_dev_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
rural_dev_sb.grid(row=0, column=7, sticky=W, padx=5)

# Sales Tax
Button(policies_fr, text="Sales Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Sales Tax"))\
    .grid(row=1, column=6, sticky=W, padx=5)
sales_tax_sb = Spinbox(policies_fr, from_=0, to=50, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
sales_tax_sb.grid(row=1, column=7, sticky=W, padx=5)

# Satellite Road Pricing
Button(policies_fr, text="Satellite Road Pricing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Satellite Road Pricing"))\
    .grid(row=2, column=6, sticky=W, padx=5)
sat_rd_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sat_rd_sb.grid(row=2, column=7, sticky=W, padx=5)

# Sub. School Bus
Button(policies_fr, text="Sub. School Bus", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Sub. School Bus"))\
    .grid(row=3, column=6, sticky=W, padx=5)
sub_sch_bus_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sub_sch_bus_sb.grid(row=3, column=7, sticky=W, padx=5)

# School Prayers
Button(policies_fr, text="School Prayers", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("School Prayers"))\
    .grid(row=4, column=6, sticky=W, padx=5)
prayer_sb = Spinbox(policies_fr, values=PRAYER_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
prayer_sb.grid(row=4, column=7, sticky=W, padx=5)

# Science Funding
Button(policies_fr, text="Science Funding", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Science Funding"))\
    .grid(row=5, column=6, sticky=W, padx=5)
science_sb = Spinbox(policies_fr, values=SCIENCE_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
science_sb.grid(row=5, column=7, sticky=W, padx=5)

# Small Business Grants
Button(policies_fr, text="Small Business Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Small Business Grants"))\
    .grid(row=6, column=6, sticky=W, padx=5)
small_business_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
small_business_sb.grid(row=6, column=7, sticky=W, padx=5)

# Space Program
Button(policies_fr, text="Space Program", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Space Program"))\
    .grid(row=7, column=6, sticky=W, padx=5)
space_sb = Spinbox(policies_fr, values=SPACE_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
space_sb.grid(row=7, column=7, sticky=W, padx=5)

# Speed Cameras
Button(policies_fr, text="Speed Cameras", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Speed Cameras"))\
    .grid(row=8, column=6, sticky=W, padx=5)
speed_sb = Spinbox(policies_fr, values=SPEED_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
speed_sb.grid(row=8, column=7, sticky=W, padx=5)

#  State Health Service
Button(policies_fr, text="State Health Service", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Health Service"))\
    .grid(row=9, column=6, sticky=W, padx=5)
health_sb = Spinbox(policies_fr, values=HEALTH_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
health_sb.grid(row=9, column=7, sticky=W, padx=5)

# State Housing
Button(policies_fr, text="State Housing", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Housing"))\
    .grid(row=10, column=6, sticky=W, padx=5)
housing_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
housing_sb.grid(row=10, column=7, sticky=W, padx=5)

# State Pensions
Button(policies_fr, text="State Pensions", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Pensions"))\
    .grid(row=11, column=6, sticky=W, padx=5)
pension_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
pension_sb.grid(row=11, column=7, sticky=W, padx=5)

# State Schools
Button(policies_fr, text="State Schools", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("State Schools"))\
    .grid(row=12, column=6, sticky=W, padx=5)
sschools_sb = Spinbox(policies_fr, values=SCHOOLS_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
sschools_sb.grid(row=12, column=7, sticky=W, padx=5)

# Stem Cell Research
Button(policies_fr, text="Stem Cell Research", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Stem Cell Research"))\
    .grid(row=13, column=6, sticky=W, padx=5)
stem_cell_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
stem_cell_sb.grid(row=13, column=7, sticky=W, padx=5)

# Tax Shelters
Button(policies_fr, text="Tax Shelters", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Tax Shelters"))\
    .grid(row=14, column=6, sticky=W, padx=5)
tax_shelter_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tax_shelter_sb.grid(row=14, column=7, sticky=W, padx=5)

# Technology Colleges
Button(policies_fr, text="Technology Colleges", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Technology Colleges"))\
    .grid(row=15, column=6, sticky=W, padx=5)
tech_college_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tech_college_sb.grid(row=15, column=7, sticky=W, padx=5)

# Technology Grants
Button(policies_fr, text="Technology Grants", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Technology Grants"))\
    .grid(row=16, column=6, sticky=W, padx=5)
tech_grant_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
tech_grant_sb.grid(row=16, column=7, sticky=W, padx=5)

# Telecommuting Initiative
Button(policies_fr, text="Telecommuting", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Telecommuting"))\
    .grid(row=17, column=6, sticky=W, padx=5)
telecommute_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
telecommute_sb.grid(row=17, column=7, sticky=W, padx=5)

# Tobacco Tax
Button(policies_fr, text="Tobacco Tax", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Tobacco Tax"))\
    .grid(row=18, column=6, sticky=W, padx=5)
tobac_tax_sb = Spinbox(policies_fr, from_=0, to=75, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, justify=RIGHT)
tobac_tax_sb.grid(row=18, column=7, sticky=W, padx=5)

# Toll Roads
Button(policies_fr, text="Toll Roads", bg=BG_COLOUR, font=BODY, anchor=W, relief=FLAT, command=lambda: help_message("Toll Roads"))\
    .grid(row=19, column=6, sticky=W, padx=5)
toll_road_sb = Spinbox(policies_fr, values=DEFAULT_SLIDER, bg=ENTRY_COLOUR, font=BODY, relief=FLAT, width=SB_WIDTH, state="readonly")
toll_road_sb.grid(row=19, column=7, sticky=W, padx=5)

# **** run window loop ****
root.mainloop()