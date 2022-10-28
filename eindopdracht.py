import time 

Antwoord_A = ["A", "a"]
Antwoord_B = ["B", "b"]
Antwoord_C = ["C", "c"]


def optie_Onderduiken ():
    print("Je rent weg van het leger en gaat onderduiken, na 3e jaar word het eindelijk opgelost en is de oorlog voorbij.")
    time.sleep(2)
    x = input() 
    if x == "Ja":
        optie_Rusland()
    else:
        quit() 
    
 


def optie_Techniekus():
    print("Je word een Techniekus voor het leger, en je blijft veilig in Oekraïne.")
    time.sleep(2)
    x = input() 
    if x == "Ja":
        optie_Rusland()
    else:
        quit() 
    
   



def optie_Acquister():
    print("Je word een Acquister, je word naar rusland gestuurd om informatie te onthalen.")
    time.sleep(2)
    print ("""Wat ga je doen?
    A. Je probeert het leger te infaltreren 
    B. Je gaat naar de hoofdstad en probeert burgers te ondervragen
    C. Je probeert russiche vrienden te maken.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_Audiobewerker():
    print("Je word Audiobewerker, je zet microfoons op plekken die mensen niet kunnen zien.")
    print("Je moet een microfoon op een andere spion zetten waar plaats je hem?")
    time.sleep(2)
    print (""""" Waar plaats je hem?
    A. Bij zn borst
    B. In zn koffer
    C. Je schiet het in zn nek.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_Waterbrigade():
    print("Je komt bij de waterbrigade, welke boot pak je?")
    time.sleep(2)
    print ("""Wat ga je doen?
    A. Onderzeër
    B. Luchtverdedegingschip
    C. Mijnenjagers.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_Straaljagerpiloot():
    print("Je word straaljagerpiloot, je pakt je straaljager. Je ziet 3 vliegtuigen van rusland.")
    time.sleep(2)
    print ("""Wat ga je doen?
    A. Je schiet ze uit de lucht
    B. Je geeft het door aan de basis en blijft van de radar af
    C. Je probeert met ze in contact te komen.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_Soldaat():
    print("Je word soldaat, eenmaal aangenomen word je gestuurd naar de frontline. Welk wapen kies je?")
    time.sleep(2)
    print ("""Welk wapen pak jij? (Heeft nadelen of voordelen in volgende keuzes)
    A. AK47
    B. G36
    C. M4.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_Wegrijden():
    print("Je probeert weg te rijden, je ziet het leger achter je aankomen en je word geschoten.")
    time.sleep(2)
    print('Start opnieuw.')
    print("Wil je opnieuw beginnen?")
    x = input() 
    if x == "Ja":
        optie_Rusland()
    else:
        quit() 

  

def optie_Sluipen():
    print("Je probeert lang de border te sluipen je ziet deze objecten wat pak je?")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Een trap
    B. Een knipschaar
    C. Een trampoline.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_border():
    print("Je pakte de auto en gaat naar de border, eenmaal daar aan vragen ze hoe oud je bent")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je zegt dat je 18 bent
    B. Je zegt dat je 19 bent
    C. Je skipt de vraag en rijd door.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_rennen():

    print ("Je rent weg, alleen je hoort hem achter je aan rennen je.")
    print("Eenmaal uit je huis gerend kom je aan bij een rand van de berg")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je springt
    B. je stopt en kijkt wie het is
    C.  je ziet een  bosje je probeert erin te verstoppen""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_leger()

    elif Antwoord in Antwoord_B:
        optie_ruslandleger

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_verstoppen():

    print ("je verstopt je, de deur word ingetrapt.")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je blijft verstoppen
    B. Je probeert weg te rennen.
    C. Je gaat kijken wie het is.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_leger()

    elif Antwoord in Antwoord_B:
        optie_rennen()

    elif Antwoord in Antwoord_C:
        print("ggr")


def optie_verstoppen():

    print ("je verstopt je, de deur word ingetrapt.")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je blijft verstoppen
    B. Je probeert weg te rennen.
    C. Je gaat kijken wie het is.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_leger()

    elif Antwoord in Antwoord_B:
        optie_ruslandleger

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_deuropenen():

    print ("je doet de deur open, het leger staat aan de deur.")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je rent weg
    B. Je vraagt waarvoor hij komt.
    C. Je probeert hem te slaan.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_Onderduiken

    elif Antwoord in Antwoord_B:
        optie_ruslandleger

    elif Antwoord in Antwoord_C:
        print("ggr")



def optie_spion():

    print ("je hebt gekozen om een spion te worden.")
    time.sleep(2)
    print ("""Je wilt spion worden wat wil je precies doen?
    A. Je gaat werken als audiobewerker.
    B. Je gaat werken als acquister.
    C. Je word een technicus.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_Audiobewerker()

    elif Antwoord in Antwoord_B:
        optie_Acquister()

    elif Antwoord in Antwoord_C:
    
     print("Www")        




#2e keuze B
def optie_ruslandleger():

    print ("je wilt je eigen land veraden, de overheid ziet dit en schieten je dood.")
    print('Start opnieuw.')
    print("Wil je opnieuw beginnen?")
    x = input() 
    if x == "Ja":
        optie_Rusland()
    else:
        quit() 






#2e keuze A 
def optie_leger():

    print ("je meld je aan in het leger, je kan kiezen uit: Straaljagerpiloot, Soldaat, ")
    time.sleep(2)
    print ("""Wat ga kies jij?"
    A. Soldaat
    B. Straaljagerpiloot
    C. Waterbrigade.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_Soldaat()

    elif Antwoord in Antwoord_B:
        optie_Straaljagerpiloot()

    elif Antwoord in Antwoord_C:
        optie_Waterbrigade()


#2e vraag keuze vechten
def optie_vechten():

    print ("je moet zometeen vechten")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je meld je aan bij het leger.
    B. Je gaat bij rusland in het leger.
    C. Je word een spion.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_leger()

    elif Antwoord in Antwoord_B:
        optie_ruslandleger

    elif Antwoord in Antwoord_C:
        optie_spion
#1e vraag optie B
def optie_Vluchten():
    print("Je wilt vluchten en je pakt je auto.")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je gaat naar de border
    B. Je  probeert langs de border te sluipen
    C. Je  rijd zo snel mogelijk langs het leger.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_border

    elif Antwoord in Antwoord_B:
        optie_Sluipen

    elif Antwoord in Antwoord_C:
        optie_Wegrijden()
#1e vraag optie C
def optie_thuisblijven():
    print("Je besluit om thuis te blijven, je hoort ineens geklop aan de deur.")
   
    print ("""Wat ga jij doen?
    A. Je doet de deur open.
    B. Je gaat je verstoppen
    C. Je rent het huis uit.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_deuropenen()

    elif Antwoord in Antwoord_B:
        optie_verstoppen()


    elif Antwoord in Antwoord_C:
        optie_rennen()

#1e vraag
def optie_Rusland():
    print ("Je bent 19 jaar en woont in Oekraïne, alles gaat goed totdat Rusland ineens binnenvalt. Oekraïne roept iedereen boven de 18 aan om mee te doen aan de oorlog.")
    time.sleep(2)
    print ("""Wat ga jij doen?
    A. Je meld je aan om te vechten.
    B. Je gaat vluchten
    C. Je weet het nog niet en blijft nog thuis.""")

    #1e keuze
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_vechten()

    elif Antwoord in Antwoord_B:
        optie_Vluchten()


    elif Antwoord in Antwoord_C:
        optie_thuisblijven()


#Introducite tot het spel met username
print("Welkom bij mijn Tekstbased applicatie, Wat is je gebruikersnaam?")
gebruikersnaam = input()
print("Welkom", gebruikersnaam)
time.sleep(2.5)
optie_Rusland()












