
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
# Autor:    Linus Wohlgemuth (Grinzold86), Nico Leder, Erhun Omuemu,   
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
rouletteZahl = 0            #ist die zufällige Zahl, die generiert wird
eingabeZahl = 0             #ist die Zahl, die der Spieler eingibt
ergebnisZahl = False        #Auswertung, ob richtige Zahl getippt
ergebnisGerade = False      #Auswertung, ob gerade/ungerade getippt
gewinn = 0                  #Variable für Gewinnberechnung 
geradeRouletteZahl = True   
geradeEingabeZahl = True
ergebnisLow = False
ergebnisHigh = False

###INPUT###
#Alle Programmrelevanten Eingabeabfragen mit .lower() und .strip() einlesen -> wandelt in Kleinbuchstaben und löscht überflüssige Leerzeichen
#!!! Dran denken, Variablen dann auch mit kleinbuchstaben abfragen !!!
#erhuns job

name = input("Bitte geben Sie Ihren Namen ein ")
print ("Hallo", name, "Willkommen zu unserem Roulette Spiel")

altersabfrage = input("Sind Sie über 18 Jahre alt? (Ja/Nein) ").lower().strip() #lässt weiterspielen nur für den Fall 'ja' zu
if (altersabfrage == "ja"):
    print("Achtung! Glückspiel kann süchtig machen")
    
else:
    print("Sorry, Sie sind nicht alt genug!")
    exit()


information = input("Möchten Sie die Spielregeln wissen? (Ja/Nein)").lower().strip() #liest Information bei bedarf ein
if information == "ja":

    print("\n Spielregeln für Roulette")
    print("1. Setzen Sie einen Betrag.")
    print("2. Wählen Sie ein Feld aus.")
    print("3. Viel Glück!\n")
elif information == "nein":
    print("\nViel Glück!\n")
else:
    print("\n Ungültige Eingabe! Bitte geben Sie 'Ja' oder 'Nein' ein.\n")
    

gewinn_abfrage = input("Wie hoch ist Ihr Einsatz?")
print("Ihr Einsatz beträgt", gewinn_abfrage, "Euro")
try:
    gewinn = int(gewinn_abfrage) 
except:
    print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")





while True:                    #while Schleife prüft Fehleingaben und lässt Korrektur zu ohne das Programm zu beenden
    auswahl = input("Worauf möchten Sie setzen? ('Zahl' 'Gerade/Ungerade' 'Low/High'): ").lower().strip() #input wird in Kleinbuchstaben gewandelt und Leerzeichen gelöscht
    if auswahl in ["zahl", "gerade/ungerade", "low/high"]:
        break                   #Endet nur, wenn einer der geforderten Werte eingegeben wurde
    print("Ungültige Eingabe, geben Sie 'Zahl','Gerade/Ungerade' oder 'Low/High'ein ")

    
if (auswahl == "zahl"):

    eingabeZahl = int(input("Eine Zahl zwischen 0 und 36 eingeben ")) #ließt Tipp ein und castet als Int
 
elif (auswahl == "gerade/ungerade"):
    while True:
        eingabeZahl = (input("Setzen Sie auf Gerade oder Ungerade? ").lower().strip())
        if eingabeZahl in ["gerade", "ungerade"]:
            break
        print("Ungültige eingabe!")

elif (auswahl == "low/high"):
        while True:
            eingabeZahl = (input("Bitte wählen 'LOW' oder 'HIGH' ")).lower().strip()
            if eingabeZahl in ["low", "high"]:
                break
            print("Ungültige eingabe")
else:
    print("Fehler!")
    exit()

#Algorithmus

rouletteZahl = random.randrange(0, 37) #Zufallszahl (0-36 inklusive) wird generiert

#normal/zahl
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

#Output



