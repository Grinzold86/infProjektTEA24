
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
ergebnisLow = False
ergebnisHigh = False

###INPUT###
#Alle Programmrelevanten Eingabeabfragen mit .lower() und .strip() einlesen -> wandelt in Kleinbuchstaben und löscht überflüssige Leerzeichen
#!!! Dran denken, Variablen dann auch mit kleinbuchstaben abfragen !!!
#erhuns job

Name = input("Bitte geben Sie Ihren Namen ein ")
print ("Hallo", Name, "Willkommen zu unserem Roulette Spiel")

Altersabfrage = input("Sind Sie über 18 Jahre alt? (Ja/Nein) ").lower().strip() #lässt weiterspielen nur für den Fall 'ja' zu
if (Altersabfrage == "ja"):
    print("Achtung! Glückspiel kann süchtig machen")
    
else:
    print("Sorry, Sie sind nicht alt genug!")
    exit()


while True:                    #while Schleife prüft Fehleingaben und lässt Korrektur zu ohne das Programm zu beenden
    Auswahl = input("Worauf möchten Sie setzen? ('Zahl' 'Gerade/Ungerade' 'Low/High'): ").lower().strip() #input wird in Kleinbuchstaben gewandelt und Leerzeichen gelöscht
    if Auswahl in ["zahl", "gerade/ungerade", "low/high"]:
        break                   #Endet nur, wenn einer der geforderten Werte eingegeben wurde
    print("Ungültige Eingabe, geben Sie 'Zahl','Gerade/Ungerade' oder 'Low/High'ein ")
    
    
if (Auswahl == "zahl"):
    eingabeZahl = int(input("Eine Zahl zwischen 0 und 36 eingeben ")) #ließt Tipp ein und castet als Int
 
elif (Auswahl == "gerade/ungerade"):
    while True:
        eingabeZahl = (input("Setzen Sie auf Gerade oder Ungerade? ").lower().strip())
        if eingabeZahl in ["gerade", "ungerade"]:
            break
        print("ungültige Eingabe!")

elif (Auswahl == "low/high"):
        while True:
            eingabeZahl = (input("Bitte wählen 'LOW' oder 'HIGH' ")).lower().strip()
            if eingabeZahl in ["low", "high"]:
                break
            print("ungültige Eingabe")
else:
    print("Fehler!")
    exit()

#Algorithmus

rouletteZahl = random.randrange(0, 37) #Zufallszahl (0-36 inklusive) wird generiert

#normal/zahl
if (Auswahl == "zahl"):
    if (rouletteZahl == eingabeZahl):
        ergebnisZahl  = True

#gerade/ungerade
elif (Auswahl == "gerade/ungerade"):
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
elif (Auswahl == "low/high"):
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



