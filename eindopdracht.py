import time 

Antwoord_A = ["A", "a"]
Antwoord_B = ["B", "b"]
Antwoord_C = ["C", "c"]

def optie_spion():

    print ("je hebt gekozen om een spion te worden.")
    time.sleep(2)
    print ("""Wat ga jij nu doen?
    A. Je gaat werken als audiobewerker.
    B. Je gaat werken als acquister.
    C. Je word een technicus.""")
    time.sleep(2)
    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_leger()

    elif Antwoord in Antwoord_B:
        optie_ruslandleger

    elif Antwoord in Antwoord_C:
        print("ggr")




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
        optie_vechten()

    elif Antwoord in Antwoord_B:
        print("gg")

    elif Antwoord in Antwoord_C:
        print("ggr")


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
        print("ggh")

    elif Antwoord in Antwoord_B:
        print("ghg")

    elif Antwoord in Antwoord_C:
        print("ggr")
#1e vraag optie C
def optie_thuisblijven():
    print("Je besluit om thuis te blijven, je hoort ineens geklop aan de deur.")
   
    print ("""Wat ga jij doen?
    A. Je doet de deur open.
    B. Je gaat je verstoppen
    C. Je rent het huis uit.""")

    
    Antwoord = input(">>>")
    if Antwoord in Antwoord_A: 
        optie_vechten()

    elif Antwoord in Antwoord_B:
        optie_Vluchten()


    elif Antwoord in Antwoord_C:
        print("ggr")

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












