
###################################################################################################
# /$$$$$$$                      /$$             /$$     /$$              
#| $$__  $$                    | $$            | $$    | $$              
#| $$  \ $$  /$$$$$$  /$$   /$$| $$  /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$ 
#| $$$$$$$/ /$$__  $$| $$  | $$| $$ /$$__  $$|_  $$_/|_  $$_/   /$$__  $$
#| $$__  $$| $$  \ $$| $$  | $$| $$| $$$$$$$$  | $$    | $$    | $$$$$$$$
#| $$  \ $$| $$  | $$| $$  | $$| $$| $$_____/  | $$ /$$| $$ /$$| $$_____/
#| $$  | $$|  $$$$$$/|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$$
#|__/  |__/ \______/  \______/ |__/ \_______/   \___/   \___/   \_______/
###################################################################################################
# Projekt:  Roulette_TEA24  
# Datei:    roulette.py  
# Autor:    Linus Wohlgemuth (Grinzold86), Nico Leder (xNox33), Erhun Omuemu (TEA24EO8), Avinash Suthakaran (Avinash21-creator)
# Datum:    4.3.2025  
# Version:  1.0   
###################################################################################################
# Beschreibung: 
# Diese Projekt verfolgt das Ziel einen Roulettetisch nach zu bilden
# Zu aller erst wählt man ein Feld aus und danach den Einsatz
# Der Algorithmus wählt zufällig eine Zahl und errechnet bei Gewinn den Erlös aus
###################################################################################################                                                                         

#Defines
import random               #ist notwendig, um eine zufällige Zahl zu generieren
import time                 #ist notwendig, um eine Wartezeit zu generieren
rouletteZahl = 0            #ist die zufällige Zahl, die generiert wird
eingabeZahl = 0             #ist die Zahl, die der Spieler eingibt
ergebnisZahl = False        #Auswertung, ob richtige Zahl getippt
ergebnisGerade = False      #Auswertung, ob gerade/ungerade getippt
gewinn = 0                  #Variable für Gewinnberechnung 
geradeRouletteZahl = True   
geradeEingabeZahl = True
ergebnisLow = False
ergebnisHigh = False
einsatz = 0
einsatzAbfrage = 0
highscore = 0


###Functions###

  #Begrüßt den Spieler und fragt nach seinem Namen.
  #Rückgabe: Name des Spielers
def begrüßung():
    name = input("Bitte geben Sie Ihren Namen ein ")
    print ("Hallo", name, "Willkommen zu unserem Roulette Spiel!\n")
    return name

def Altersabfrage():
    while True:  

        altersabfrage = input("Sind Sie über 18 Jahre alt? (Ja/Nein) ").lower().strip() #lässt weiterspielen nur für den Fall 'ja' zu
        if(altersabfrage) in ["ja","nein"]:

            if (altersabfrage == "ja"):
                print("\nAchtung! Glückspiel kann süchtig machen!")
                break
            else:
                print("Sorry, Sie sind nicht alt genug!")
                exit()
        else:
            print ("Ungültige Eingabe! Bitte geben Sie 'Ja' oder 'Nein' ein.\n")

  #Bietet dem Spieler an, die Spielregeln zu lesen.
  #Bei Bedarf werden die Regeln ausgegeben, ansonsten wird direkt fortgefahren

def spielregeln():
    while True:
        
        information = input("Möchten Sie die Spielregeln wissen? (Ja/Nein) ").lower().strip() #liest Information bei bedarf ein
        if information == "ja":
            print("\n --------Spielregeln für Roulette--------")
            print("1. Setzen Sie einen Betrag.")
            print("2. Wählen Sie aus, auf was Sie setzten möchten:\n -> Eine Zahl von 0 bis 36 \n -> Auf gerade/ungerade Felder\n -> obere Hälfte/untere Hälfte")
            print("3. Viel Glück!\n")
            break

        elif information == "nein":
            print("\nViel Glück!\n")
            break

        else:
            print("\n Ungültige Eingabe! Bitte geben Sie 'Ja' oder 'Nein' ein.\n")
        
def einsatzAbfrage():
    while True:                                                         #Schleife um Falscheingaben abzufangen und Korrektur zu ermöglichen
        einsatzAbfrage = input("Wie hoch ist Ihr Einsatz? ")
        try:                                                            #-> versucht Eingabe als Zahl zu lesen
            einsatz = int(einsatzAbfrage)
            print("Ihr Einsatz beträgt", einsatz, "Euro")
            return einsatz                                              #...,wenn erfolgreich -> Schleife verlassen
        except:                                                         #...,wenn nicht erfolgreich, Erneute Abfrage
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.\n")

def auswahlAbfrage():                                                   
    while True:                                                         #while Schleife prüft Fehleingaben und lässt Korrektur zu
        auswahl = input("Worauf möchten Sie setzen? ('Zahl' 'Gerade/Ungerade' 'Low/High'): ").lower().strip() #input wird in Kleinbuchstaben gewandelt und Leerzeichen gelöscht
        if auswahl in ["zahl", "gerade/ungerade", "low/high"]:
            return auswahl
        print("Ungültige Eingabe, geben Sie 'Zahl','Gerade/Ungerade' oder 'Low/High'ein \n")

  #Fragt den Spieler nach einer Zahl zwischen 0 und 36.
  #Stellt sicher, dass die Eingabe innerhalb des gültigen Bereichs liegt.

def zahlSetzen():
    while True:
        try:
            eingabeZahl = int(input("Eine Zahl zwischen 0 und 36 eingeben ")) #ließt Tipp ein und castet als Int
            if (0<= eingabeZahl <= 36):
                return eingabeZahl
        except:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.\n")

  #Fragt den Spieler, ob er auf 'gerade' oder 'ungerade' setzen möchte.

def geradeUngeradeSetzen():
    while True:
        eingabeZahl = (input("Setzen Sie auf Gerade oder Ungerade? ").lower().strip())
        if eingabeZahl in ["gerade", "ungerade"]:
                return eingabeZahl
        else:
            print("Ungültige Eingabe! Bitte 'gerade' oder 'ungerade' eingeben.")
    
def lowHighSetzen():
    while True:
            eingabeZahl = (input("Bitte wählen 'LOW' oder 'HIGH' ")).lower().strip()
            if eingabeZahl in ["low", "high"]:
                return eingabeZahl
            else:
                print("Ungültige Eingabe! Bitte 'low' oder 'high' eingeben.")
            
def rouletteDrehung():
#Generiert kleine Animation für den Roulettevorgang und zufällige Roulette-Zahl zwischen 0und 36
   print("""
 ZZZZZ   III   EEEEE  H   H  U   U  N   N   GGGGG
    Z     I    E      H   H  U   U  NN  N  G      
   Z      I    EEEE   HHHHH  U   U  N N N  G  GG  
  Z       I    E      H   H  U   U  N  NN  G   G  
 ZZZZZ   III   EEEEE  H   H  UUUUU  N   N   GGGGG
""")
   i=0
   for i in range(3):
        print(".")
        time.sleep(1)

   return random.randrange(0, 37)

  #Nach jeder Runde wird überprüft, ob der aktuelle Gewinn höher ist als der bisherige Highscore.
  #Bei einem neuen Highscore wird dieser angezeigt.

def highscoreCheck(gewinn, highscore):
        if gewinn > highscore:
            highscore = gewinn
            print(f"Neuer Highscore! Ihr bisher höchster Gewinn beträgt: {highscore} Euro")
        return highscore

   #Fragt den Spieler, ob er weiterspielen möchte.
   #Bei negativer Antwort wird das Programm beendet

def abfrageWeiterspielen():
        while True:
            abfrageWiederholung = input("Möchten Sie weiter spielen? (Ja/Nein) ").lower().strip()
            if(abfrageWiederholung == "nein"):
                print("Vielen Dank für ihren Besuch!")
                exit()
            elif(abfrageWiederholung == "ja"):
                print("Wir wünschen Ihnen noch viel Spaß!")
                break
            else:
                print("Ungültige Eingabe! Bitte 'Ja' oder 'Nein' eingeben. \n")
        
    



###INPUT###
#Alle Programmrelevanten Eingabeabfragen mit .lower() und .strip() einlesen -> wandelt in Kleinbuchstaben und löscht überflüssige Leerzeichen
#!!! Dran denken, Variablen dann auch mit kleinbuchstaben abfragen !!!

#Spielbeginn
name = begrüßung()
Altersabfrage()
spielregeln()

while True:
    einsatz = einsatzAbfrage()
    auswahl = auswahlAbfrage()

    if (auswahl == "zahl"):
        eingabeZahl = zahlSetzen()

    elif (auswahl == "gerade/ungerade"):
        eingabeZahl = geradeUngeradeSetzen()

    elif (auswahl == "low/high"):
        eingabeZahl = lowHighSetzen()

    else:
        print("Fehler!")
        exit()

    rouletteZahl = rouletteDrehung()
    ergebnisZahl = ergebnisGerade = ergebnisLow = ergebnisHigh = False

    #Auswahlverarbeitung
    #Zahl
    if (auswahl == "zahl"):
        if (rouletteZahl == eingabeZahl):
            ergebnisZahl  = True

    #gerade/ungerade
    elif (auswahl == "gerade/ungerade"):
        if (rouletteZahl % 2) == 1:
            geradeRouletteZahl = False
        else:
            geradeRouletteZahl = True

        if(eingabeZahl == "gerade") and (geradeRouletteZahl == True):
            ergebnisGerade = True

        elif(eingabeZahl == "ungerade") and (geradeRouletteZahl == False):
            ergebnisGerade = True

        else:
            ergebnisGerade = False

    #Low(1-18)/High(19-36)
    elif (auswahl == "low/high"):
        if (rouletteZahl >= 1) and (rouletteZahl <= 18) and (eingabeZahl == "low"):
            ergebnisLow = True
        else:
            ergebnisLow = False

        if (rouletteZahl >= 19) and (rouletteZahl <= 36) and (eingabeZahl == "high"):
            ergebnisHigh = True 
        else:
            ergebnisHigh = False

        if (rouletteZahl == 0):
            ergebnisLow = False
            ergebnisHigh = False
    else:
        print("Fehler!")
        exit()

    #Output der Spielergebnisse
    print(f"\nDie Roulette-Zahl ist: {rouletteZahl}")
    if ergebnisZahl:
        gewinn = einsatz * 35
        print(f"Herzlichen Glückwunsch {name}, Sie haben auf die richtige Zahl gesetzt und haben {gewinn} Euro gewonnen!")
    elif ergebnisGerade or ergebnisLow or ergebnisHigh:
        gewinn = einsatz * 2
        print(f"Glückwunsch {name}, Sie haben gewonnen und erhalten {gewinn} Euro!")
    else:
        print(f"Leider haben Sie verloren, {name}. Ihr Einsatz von {einsatz} haben sie leider verloren.")

    #Überprüfung, ob Highscore geknackt wurde
    highscore = highscoreCheck(gewinn, highscore)
    
    #Abfrage für weiteres Spielen
    print("\nVielen Dank fürs Spielen! Wir hoffen, Sie hatten Ihren Spaß.")
    abfrageWeiterspielen()
