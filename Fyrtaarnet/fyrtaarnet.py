import time

moerkt = True
rom = ["Soverom", "Hovedrom", "Lager", "Ute", "Skur", "Oppe"]
soverom = ["Vindu", "Nattbord"]
print()
print("Du våkner plutselig av et høyt smell")
print()
oppeavSengen = False # Reist seg fra sengen
harLykt = False # Funnet parafinlampen
tentLykt = False # Tent parafinlampen
harArk = False # Lest arket i soverommet
rommet = rom[0] # Nåværende rom. Starter i soverommet
hvorErTanken = rom[4] # Hvor tanken står når man ikke bærer den
lampepaaminnelse = False # Fått påminnelsen om lampen
harKlaer = False # Plukket opp klærne
harNoekkel = False # Har nøkkelen til lageret
noekkelFall = False 
blittKald = False # Vært ute uten kklør
noekkelpaagulv = False 
aapenKiste = False # om kisten på lageret er åpent
baererTank = False # Bærer parafintanken
tankiSkur = True
lyktFull = False # Tanken til fyrlykt fylt på
heisOppe = True # Om heisen er i toppen
tankPaaHeis = False # Om tanken er på heisen
staarPaaHeis = False
antallInput = 0


def skrivArk():
                            print("""
┌──────────────────────────────────────────────┐
│   20.april 1889                              │
│                                              │
│ Velkommen til fyrtårnet.                     │
│                                              │
│ Du er den nye fyrvokteren. Jeg har satt      │
│ mye tillit til deg. Skulle ønske jeg ikke    │
│ måtte, men min hånd er tvunget. Tilgi min    │
│ utålmodighet, men du er nødt til å tenne     │
│ lykten i toppen av tårnet. Jeg vil følge     │
│ nøye med på hvert steg du tar.               │                           
│ Tiden vil vise om du er rett mann for jobben.│                          
│                                              │                         
│  - Albert                                    │                        
│                                              │
└──────────────────────────────────────────────┘
""")
                            
def skrivTonne():
                            print(r"""
      _________
     /         \
    |===========|
    |    |||    |
    |    |||    |
    |===========|
     \_________/
""")
                            
def sjekkLampe():  
    if antallInput < 10:
        print("Lampen er full")
    elif 10 <= antallInput < 20:
        print("Lampen er 90% full")
    elif 20 <= antallInput < 30:
        print("Lampen er 80% full")
    elif 30 <= antallInput < 40:
        print("Lampen er 70% full")
    elif 40 <= antallInput < 50:
        print("Lampen er 60% full")
    elif 50 <= antallInput < 60:
        print("Lampen er 50% full")
    elif 60 <= antallInput < 70:
        print("Lampen er 40% full")
    elif 70 <= antallInput < 80:
        print("Lampen er 30% full")           
    elif 80 <= antallInput < 90:
        print("Lampen er 20% full")
    elif 90 <= antallInput < 100:
        print("Lampen er 10% full")  



while moerkt:
    if antallInput == 100:
        print("Lyset i lampen slukner. Alt blir mørkt")
        print("Pulvis et umbra sumus")
        exit()
    
    tekst = input().lower().strip()
    print()
    gyldig_kommando = False  # Variabel for å sjekke om en gyldig kommando ble brukt

    if tentLykt:
        antallInput += 1
    
    if tekst in ["slukk lampen", "slukk lampa", "skru av lampen", "skru av lampa", "skru av lyset", "slukk lyset", "slukk lyset i lampen", "skru av lyset i lampen"]:
        if tentLykt:
            print("Du kan ikke skru av lampen. Du må ha den for å se")
            print()
            gyldig_kommando = True

    elif tekst in ["sjekk lampen", "sjekk lampa", "se på lampen", "sjekk parafin", "undersøk lampen", "sjekk parafinlampen", "se på parafinlampen", "sjekk parafin", "undersøk parafinlampen", "sjekk parafinlampa"]:
        if harLykt:
            if not tentLykt:
                print("Lampen er full av parafin, men den er ikke tent")
                print()
                gyldig_kommando = True
            else:
                sjekkLampe()
                print()
                gyldig_kommando = True
        

    if rommet == rom[0]: # Soverom
        if not oppeavSengen:
            if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
                print("Du ligger i sengen din. Rommet er mørkt. Du kan høre regndråper som treffer vinduet.")
                print()
                gyldig_kommando = True

            elif tekst in ["reis deg", "reis deg opp", "gå opp", "reis deg fra sengen", "gå opp av sengen", "gå ut av sengen" "reis deg opp av sengen", "stå opp", "Stå opp av sengen"]:
                print("Du reiser deg. Du har jævlig vondt i hodet. Du husker ikke hva du heter eller hvor du er.")
                print()
                oppeavSengen = True
                gyldig_kommando = True

        # Denne delen håndteres kun når spilleren har reist seg fra sengen
        if oppeavSengen:
            if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
                if noekkelFall and not harNoekkel:
                    print("Rommet ser likt ut som tidligere, bortsett fra at det ligger noe på gulvet")
                    print()
                    gyldig_kommando = True
                else:
                    print("Du ser et nattbord ved siden av sengen din. En dør leder ut av soverommet. Du ser at det er mørkt ut gjennom vinduet.")
                    print()
                    gyldig_kommando = True
                if hvorErTanken == rom[0]:
                    print("Det står en parafintank i rommet")

            elif tekst in ["se nærmere", "se på gulvet", "se på nøkkelen", "plukk opp nøkkelen", "se på det som ligger på gulvet", "plukk det opp", "plukk den opp", "se på tingen", "plukk opp tingen"]:
                 if noekkelFall and not harNoekkel:   
                    print("Du plukker det opp og ser at det er en nøkkel")
                    print(r"""
                          
             .--.
            /.-. '----------.
            \'-' .--"--""-"-'
             '--'
                          """)
                    harNoekkel = True
                    print()
                    gyldig_kommando = True      
                     
            elif tekst in ["gå til vinduet", "se på vinduet", "se bort på vinduet", "gå til vindu", "se på vindu", "se bort på vindu"]:
                if not harLykt:
                    print("Det er mørkt ute. Det eneste lyset du kan se er månen og et par stjerner. Regnet høljer ned. Det står en parafinlampe i vinduskarmen.")
                else:
                    print("Det er mørkt ute. Det eneste lyset du kan se er månen og et par stjerner. Regnet høljer ned.")
                print()

                gyldig_kommando = True

            elif tekst in ["åpne vinduet", "åpne vindu", "gå ut vindu", "gå ut vinduet", "knus vindu", "knus vinduet"]:
                    print("Du prøver, men klarer ikke å få det opp")
                    gyldig_kommando = True

            elif tekst in ["ta lampen", "ta lampa", "ta parafinlampen", "ta parafinlampa", "plukk opp parafinlampen", "plukk opp parafinlampa", "plukk opp lampen", "plukk opp lampa"]:
                if not harLykt:
                    print("Du plukker opp lampen")
                    print("""
     ║ ║             
     ║ ║             
     ███             
    (___) 
                    """)
                    print()
                    harLykt = True
                    gyldig_kommando = True
                else:
                    print("Du har allerede lampen.")
                    print()
                    gyldig_kommando = True  

            elif tekst in ["tenn på lampen", "skru på lampen", "tenn på lampa", "skru på lampa", "tenn lampa", "tenn parafinlampen", "tenn lampen"]:
                if harLykt and not tentLykt:  
                    print("Du tenner på lampen. Lyset brenner fint, og ting blir lettere å se.")
                    print()
                    tentLykt = True
                    gyldig_kommando = True
                else:
                    print("Lampen er allerede tent.")
                    print()
                    gyldig_kommando = True
          
            elif tekst in ["se på nattbordet", "gå til nattbordet", "se mot nattbordet", "se på nattbord"]:
                if not harArk:
                    print("Du ser ned på nattbordet. Der ligger det et papirark med noe skrift.")
                    print()
                    gyldig_kommando = True
                else:
                    print("Du ser ned på nattbordet. Det er ingenting der.")
                    print()
                    gyldig_kommando = True
                    
            
            elif tekst in ["ta arket", "plukk opp arket","ta papirark", "les arket", "ta papirarket", "ta ark", "les ark", "plukk opp papirarket", "les papirarket", "se på arket"]:
                if not harArk:
                    if not tentLykt:
                        print("Du plukker opp arket, men det er for mørkt for å lese det. Du legger arket tilbake på nattbordet")
                        print()
                        gyldig_kommando = True
                    else:
                        skrivArk()
                        harArk = True
                        gyldig_kommando = True
            elif tekst in ["se på døren", "se på døra", "se mot døren", "se mot døra"]:
                 print("Du ser på døren. Den ser gammel og slitt ut. Du vet ikke hvor den leder.")
                 print()
                 gyldig_kommando = True
            
            elif tekst in ["åpne døren", "åpne døra", "gå ut døren", "gå til døren", "gå mot døren", "gå ut av rommet", "gå ut av soverommet", "gå ut"]:
                if not tentLykt:
                     print("Du åpner døren, men det er for mørkt for å se noe. Du går tilbake inn på soverommet.")
                     print()
                     gyldig_kommando = True
                else:
                     print("Du går ut av soverommet")
                     print()
                     rommet = rom[1]
                     gyldig_kommando = True
            
            elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
                if hvorErTanken == rom[0]:
                    baererTank = True
                    print("Du løfter tanken.")
                    print()
                    skrivTonne()
                    print()
                    hvorErTanken = None
                    gyldig_kommando = True
        
            elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
                if baererTank:
                    baererTank = False
                    print("Du setter ned tanken.")
                    print()
                    hvorErTanken = rom[0]
                    gyldig_kommando = True

    elif rommet == rom[1]: # Hovedrom
        if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
            if not lampepaaminnelse:
                print("Du er inne i et kjempehøyt rundt rom. Det er en stor dør i den andre enden av rommet, og en annen dør det står lager på.")
                print("En rusten trapp går i sirkler mot toppen.")
                print("Du ser at parafinnivået i lampen har gått ned. Du minner deg selv på at du må sjekke den jevnlig så den ikke går tom.")
                print()
                lampepaaminnelse = True
                gyldig_kommando = True
            else:
                print("Rommet er høyt som et tårn. En trapp leder mot toppen. Du ser tre dører: Soveromsdøren, lagerdøren og en stor metalldør")
                if not heisOppe:
                    print("I midten av rommet står en heis")
                if hvorErTanken == rom[1]:
                    print("Det står og en parafintank i rommet")
                print()
                gyldig_kommando = True
        
        elif tekst in ["gå på heisen", "still deg på heisen", "stå på heisen", "dra med heisen", "ta heisen"]:
            if not staarPaaHeis:
                print("Du stiller deg på heisen")
                print()
                staarPaaHeis = True
                gyldig_kommando = True
        
        elif tekst in ["snurr på spaken", "snurr spaken", "dra opp med heisen", "ta heisen oppover", "ta heisen opp", "dra med heisen", "ta heisen", "vri på spaken"]:
            if staarPaaHeis:
                print("Du snurrer på spaken og heisen begynner å gå oppover.")
                print()
                time.sleep(5)
                print("Omsider når du toppen")
                print()
                antallInput += 4
                rommet = rom[5]
                heisOppe = True
                staarPaaHeis = False
                gyldig_kommando = True
            elif not heisOppe:
                print("Du må stå på heisen for å bruke den.")
                print()
                gyldig_kommando = True

        elif tekst in ["gå inn på soverommet", "åpne soverommet", "åpne døren til soverommet", "gå inn på soverom", "åpne soveromsdøren", "åpne den lille døren", "åpne den små døren", "gå inn den lille døren", "gå inn den små døren", "gå inn liten dør", "gå inn små dør", "gå inn i soverommet"]:
            print("Du går inn på soverommet")
            print()
            staarPaaHeis = False
            rommet = rom[0]
            gyldig_kommando = True
        elif tekst in ["se på soveromsdøren", "se på døren til soverommet", "se på den lille døren", "se på den små døren"]:
            
            print("Det er en liten dør av tre.")
            gyldig_kommando = True
        
        elif tekst in ["se på metalldøren", "se på døren ut", "se på inngangsdøren", "se på den store døren"]:
            print("Døren er stor og av metall. Du får en følelse av at den leder ut.")
            gyldig_kommando = True
        
        elif tekst in ["åpne den store døren", "gå ut metalldøren" "gå ut den store døren", "gå ut", "gå ut av fyrtårnet", "åpne metalldøren", "åpne metalldør"]:
            staarPaaHeis = False
            if not harKlaer:
                print("Du åpner døren, vinden blåser regnet mot ansiktet ditt, og du blir iskald.") 
                print("Du går inn og lukker døren for å unngå å fryse ihjel")
                print()
                blittKald = True
                gyldig_kommando = True
            else:
                print("Du går ut døren")
                print()
                rommet = rom[3]
                gyldig_kommando = True
        
        elif tekst in ["åpne lageret", "gå inn på lageret", "åpne lagerdøren", "gå inn på lager", "åpne døren til lageret", "gå inn lagerdøren", "åpne døren det står lager på"]:
            staarPaaHeis = False
            if not harNoekkel:
                if not noekkelFall:
                    print("Du prøver å åpne døren, men den er låst. Du hører lyden av noe som treffer bakken på soverommet")
                    print()
                    noekkelFall = True
                    gyldig_kommando = True
                else:
                    print("Du prøver å åpne døren, men den er låst.")
                    print()
                    gyldig_kommando = True
            else:
                if blittKald:
                    print("Du prøver å sette nøkkelen i låsen, men skjelver og mister nøkkelen på gulvet.")
                    print()
                    noekkelpaagulv = True
                    gyldig_kommando = True
                else:
                    print("Du går inn på lageret")
                    rommet = rom[2]
                    print()
                    gyldig_kommando = True
        
        elif tekst in ["se på gulvet", "se ned på gulvet", "se etter nøkkelen", "se på nøkkelen"]:
            if noekkelpaagulv:
                print("Nøkkelen ligger på gulvet foran deg")
                print()
                gyldig_kommando = True


       
        elif tekst in ["se nærmere", "se på nøkkelen", "plukk opp nøkkelen", "ta nøkkel", " ta nøkkelen", "se på det som ligger på gulvet", "plukk det opp", "plukk den opp", "se på tingen", "plukk opp tingen"]:
            if noekkelpaagulv:
                print("Du plukker opp nøkkelen")
                print()
                blittKald = False
                noekkelpaagulv = False
                gyldig_kommando = True
        
        elif tekst in ["se på trappen", "se på trappa"]:
            print("Trappen er rusten og av metall. Den går i sirkler mot toppen")
            print()
            gyldig_kommando = True
        
        elif tekst in ["gå opp trappen", "gå opp", "gå opp trappa", "ta trappen", "gå til toppen", "ta trappa"]:
            staarPaaHeis = False
            if not baererTank:
                print("Du starter å gå opp trappen")
                print()
                time.sleep(5)
                print("Tiden går og du blir sliten")
                print()
                time.sleep(5)
                print("Omsider når du toppen")
                print()
                antallInput += 8
                rommet = rom[5]
                gyldig_kommando = True
            else:
                print("Parafintanken er for tung. Du klarer ikke å bære den opp trappen.")
                print()
                gyldig_kommando = True
        
        elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
            if hvorErTanken == rom[1]:
                baererTank = True
                print("Du løfter tanken.")
                print()
                skrivTonne()
                print()
                hvorErTanken = None
                gyldig_kommando = True
        
        elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
            if baererTank:
                baererTank = False
                print("Du setter ned tanken.")
                print()
                hvorErTanken = rom[1]
                gyldig_kommando = True


    elif rommet == rom[2]: # Lager
        if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
            print("Du står inne i et lite og trangt rom. Foran deg står det en kiste")
            if hvorErTanken == rom[2]:
                    print("Det står og en parafintank i rommet")
            print()
            gyldig_kommando = True

        elif tekst in ["åpne døren", "åpne døra", "gå ut døren", "gå ut", "gå til døren", "gå mot døren", "gå ut av rommet", "gå ut av soverommet"]:
            rommet = rom[1]
            print("Du går ut av rommet.")
            print()
            gyldig_kommando = True

        elif tekst in ["se på kisten", "se ned på kisten", "se på kiste"]:
            if not aapenKiste:
                print("Det er en gammel kiste laget av tre.")
                print()
                gyldig_kommando = True
            else:
                if not harKlaer:
                    print("Kisten er åpen. Det ligger en gammel oljebukse og en regnjakke og en sydvest.")
                    print()
                    gyldig_kommando = True
                else:
                    print("Kisten er tom")
                    print()
                    gyldig_kommando = True

        elif tekst in ["åpne kisten", "åpne kiste", "sett inn nøkkelen", "lukk opp kisten", "sett inn nøkkelen i kisten", "sett nøkkelen i nøkkelhullet", "sett inn nøkkelen i nøkkelhullet", "sett nøkkelen inn i kisten"]:
                    if not aapenKiste: 
                        if harNoekkel:
                            aapenKiste = True
                            print("Du åpner kisten")
                            print()
                            gyldig_kommando = True
                        else:
                            print("Du har ikke nøkkelen til kisten")
                            print()
                            gyldig_kommando = True
                    else:
                        print("Kisten er allerede åpen")
                        print()
                        gyldig_kommando = True

        elif tekst in ["plukk opp klærne", "plukk opp jakken", "plukk opp regnjakken", "ta jakken", "ta jakke", "ta regnjakken", "ta regnjakke", "ta klærne", "ta klær", "ta buksen", "plukk opp buksen", "ta oljebuksen", "plukk opp oljebuksen", "ta sydvest", "ta sydvesten", "plukk opp sydvest", "plukk opp sydvest"]:
            if aapenKiste: 
                if not harKlaer:
                    harKlaer = True
                    print("Du tar på deg klærne. Du kjennet at du blir varmere.")
                    print()
                    gyldig_kommando = True
                else:
                    print("Du har allerede tatt opp klærne fra kisten")
                    print()
                    gyldig_kommando = True
        
        elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
            if hvorErTanken == rom[2]:
                baererTank = True
                print("Du løfter tanken.")
                print()
                skrivTonne()
                print()
                hvorErTanken = None
                gyldig_kommando = True
        
        elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
            if baererTank:
                baererTank = False
                print("Du setter ned tanken.")
                print()
                hvorErTanken = rom[2]
                gyldig_kommando = True

    elif rommet == rom[3]: #Ute
        if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
            print("Du ser opp på det høye fyrtårnet som peker opp mot stjernehimmelen. Du er på en øy uten noe sivilisasjon i sikte. Det står et lite skur ved siden av fyrtårnet.")
            if hvorErTanken == rom[3]:
                print("Det står en parafintank på bakken.")
            print()
            gyldig_kommando = True
        
        elif tekst in ["se på skuret", "se bort på skuret", "se på skur"]:
            print("Det er et gammelt treskur. Noen av plankene er råtne.")
            print()
            gyldig_kommando = True

        elif tekst in ["gå inn i skuret", "gå inn i skur", "åpne skuret", "åpne skurdøren", "åpne døren til skuret", "gå til skuret"]:
            rommet = rom[4]
            print("Du går inn i skuret.")
            print()
            gyldig_kommando = True
        
        elif tekst in ["åpne metalldøren", "åpne døren til fyrtårnet", "gå inn i fyrtårnet", "gå inn døren til fyrtårnet", "gå inn i tårnet"]:
            rommet = rom[1]
            print("Du går tilbake inn i fyrtårnet")
            print()
            gyldig_kommando = True
    
        elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
            if hvorErTanken == rom[3]:
                baererTank = True
                print("Du løfter tanken.")
                print()
                skrivTonne()
                print()
                hvorErTanken = None
                gyldig_kommando = True
        
        elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
            if baererTank:
                baererTank = False
                print("Du setter ned tanken.")
                print()
                hvorErTanken = rom[3]
                gyldig_kommando = True


    elif rommet == rom[4]: # Skur
        if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
            if hvorErTanken == rom[4]:
                print("Du står inne i et lite og gammelt skur. Du kan kjenne lukten av råte. Det står en parafintank i midten av rommet. Utenom det er skuret tomt.")
                print()
                gyldig_kommando = True
            else:
                print("Du står inne i et lite og gammelt skur. Du kan kjenne lukten av råte. Skuret er tomt.")
                print()
                gyldig_kommando = True

        elif tekst in ["se på tanken", "se på parafintanken"]:
            print("Tanken er full. Den ser ganske tung ut, men du føler at du vil klare å bære den med deg.")
            print()
            gyldig_kommando = True
        
        elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
            if hvorErTanken == rom[4]:
                baererTank = True
                print("Du klarer akkurat å løfte tanken")
                print()
                skrivTonne()
                print()
                hvorErTanken = None
                gyldig_kommando = True
        
        elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
            if baererTank:
                baererTank = False
                print("Du setter ned tanken.")
                print()
                hvorErTanken = rom[4]
                gyldig_kommando = True
        
        elif tekst in ["gå ut", "gå ut av skuret", "åpne døren", "gå  ut døren"]:
            rommet = rom[3]
            if baererTank:
                tankiSkur = False
                hvorErTanken = None
            print("Du går ut av skuret")
            print()
            gyldig_kommando = True
            


    elif rommet == rom[5]: # Oppe

        if tekst in ["se deg rundt", "se rundt", "se deg omkring", "se omkring", "se omkring deg", "se meg rundt", "se meg omkring"]:
            print("Du er høyt oppe og omringet av glass. En gigantisk lykt er i sentrum av rommet.")
            if heisOppe:
                print("I den andre enden av rommet står noe som ligner på en heis.")
                print()
            if hvorErTanken == rom[5]:
                print("Det står og en parafintank i rommet")
            gyldig_kommando = True
        
        elif tekst in ["gå ned trappen", "gå ned trappa", "ta trappen", "gå bunnen", "ta trappa"]:
            staarPaaHeis = False
            if not baererTank:
                print("Du starter å gå ned trappen")
                print()
                time.sleep(5)
                print("Tiden går og du blir sliten")
                print()
                time.sleep(5)
                print("Omsider når du bunnen")
                print()
                antallInput += 8
                rommet = rom[1]
                gyldig_kommando = True
            else:
                print("Det går ikke an å slepe tanken ned trappen.")
                print()
                gyldig_kommando = True

        elif tekst in ["plukk opp tanken", "ta tanken", "plukk opp parafintanken", "slep tanken", "ta parafintanken", "slep parafintanken", "ta med tanken", "ta med deg tanken", "ta med parafintanken", "ta med deg parafintanken"]:
            if hvorErTanken == rom[5]:
                baererTank = True
                print("Du løfter tanken")
                print()
                skrivTonne()
                print()
                hvorErTanken = None
                gyldig_kommando = True
        
        elif tekst in ["slipp tanken", "slipp parafintanken", "sett ned tanken", "sett ned parafintanken", "sett tanken på bakken", "sett parafintanken på bakken", "sett parafintanken på gulvet", "sett tanken på gulvet"]:
            if baererTank:
                baererTank = False
                print("Du setter ned tanken.")
                print()
                hvorErTanken = rom[5]
                gyldig_kommando = True

        elif tekst in ["se på heisen", "gå til heisen", "se på heis", "gå til heis"]:
            print("Det er en gammel heis av tre. Den har en spake man kan snurre på.")
            print()
            gyldig_kommando = True    
        elif tekst in ["se ut glasset", "se ut", "se ut vinduet"]:
            print("Det er helt mørkt ute. Du kan så vidt skimte bølgene som treffer berget under deg.")
            print()
            gyldig_kommando = True

        elif tekst in ["se på lykten", "se på lykt", "se på fyrlykten", "undersøk lykten", "undersøk fyrlykten"]:
            print("Lykten er er høy. Den øverste delen er laget av glass og den nederste av metall. Den har en knapp og et lokk som kan åpnes.")
            print()
            gyldig_kommando = True

        elif tekst in ["tenn på lykten", "tenn lykten", "tenn lykt", "skru på lykten", "sett fyr på lykten", "skru på tenningsmekanisme", "skru på lykt", "trykk på knappen", "trykk inn knappen" "trykk på knapp", "trykk inn knapp" "tenn på lykt", "sett på tenningsmekanismen"]:
            if lyktFull:
                print("Du blir blendet av et sterkt lys")
                print()
                time.sleep(2)
                print("Gratulerer!")
                print(f"Du har fullført spillet på", antallInput, "kommandoer")
                print()
                antallInput = 0
                moerkt = False
                gyldig_kommando = True
            else:
                print("Du prøver å tenne på lykten, men det virker ikke.")
                print()
                gyldig_kommando = True
            
        elif tekst in ["se på lokket", "se på lokk", "åpne lokket", "sjekk lokket", "ta på lokket", "åpne lokk", "åpne lokk"]:
            if not lyktFull:   
                print("Du åpner lokket. Det lukter parafin, men tanken er tom")
                print()
                gyldig_kommando = True    
            else:
                print("Du åpner lokket. Tanken er full av parafin")
                print()
                gyldig_kommando = True

        elif tekst in ["se på knappen", "se på knapp"]:
            print("Det er en liten svart knapp. Over den står det: Tenn Lykten")
            print()
            gyldig_kommando = True
        
        elif tekst in ["fyll på tanken", "fyll tanken", "hell parafin i tanken", "tøm parafin i tanken", "fyll parafin i tanken", "fyll parafin i lokket", "fyll parafin ned lokket", "tøm parafin ned lokket", "fyll i tanken", "fyll på lykten", "tøm parafin i lykten", "hell parafin i lykten"]:
            if baererTank:
                print("Du tømmer parafintanken inn i lykten")
                print()
                lyktFull = True
                baererTank = False
                gyldig_kommando = True
        
        elif tekst in ["gå på heisen", "still deg på heisen", "stå på heisen", "dra med heisen", "ta heisen"]:
            if not staarPaaHeis:
                print("Du stiller deg på heisen")
                print()
                staarPaaHeis = True
                gyldig_kommando = True
        
        
        elif tekst in ["snurr på spaken", "snurr spaken", "dra ned med heisen", "ta heisen nedover", "ta heisen ned", "dra med heisen", "ta heisen", "vri på spaken"]:
            if staarPaaHeis:
                print("Du snurrer på spaken og heisen begynner å gå nedover.")
                print()
                time.sleep(5)
                print("Omsider når du bunnen")
                print()
                antallInput += 4
                rommet = rom[1]
                heisOppe = False
                staarPaaHeis = False
                gyldig_kommando = True
            elif heisOppe:
                print("Du må stå på heisen for å bruke den.")
                print()
                gyldig_kommando = True
   

    # Skriv "Det forsto jeg ikke" kun hvis ingen kommandoer ble matchet
    if not gyldig_kommando:
        print("Det forsto jeg ikke")
        print()
    