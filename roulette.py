
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
# Autor:    Linus Wohlgemuth, Nico Leder, Erhun Omuemu,   
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
rouletteZahl = 0            #ist die zufällige Zahl die generiert wird
eingabeZahl = 0             #ist die Zahl die der Spieler eingibt
ergebnisZahl = False       
ergebnisGerade = False
gewinn = 0
geradeRouletteZahl = True
geradeEingabeZahl = True
ergebnisLow = False
ergebnisHigh = False

#Input
#erhuns job
Name = input("Bitte geben Sie Ihren Namen ein")
print ("Hallo", Name, "Willkommen zu unserem Roulette Spiel")

Altersabfrage = input("Sind Sie über 18 Jahre alt? (Ja/Nein)")
if (Altersabfrage == "Nein"):
    print("Sorry, Sie sind nicht alt genug")
    exit()
else:
    print("Achtung! Glückspiel kann süchtig machen")

#Algorithmus

rouletteZahl = random.randrange(0, 37) #Zufallszahl wird generiert

#normal
if (Auswahl == "Zahl"):
    if (rouletteZahl == eingabeZahl):
        ergebnisZahl  = True

#gerade/ungerade
if (Auswahl == "Gerade/Ungerade"):
    if (rouletteZahl % 2) == 1:
        geradeRouletteZahl = False

    if (eingabeZahl % 2) == 1:
        geradeEingabeZahl = False

    if(geradeEingabeZahl==geradeRouletteZahl):
        ergebnisGerade = True

#Low(1-18)/High(19-36)
if (Auswahl == "Low/High"):
    if (rouletteZahl >= 1) and (rouletteZahl <= 18):
        ergebnisLow = True

    if (rouletteZahl >= 19) and (rouletteZahl <= 36):
        ergebnisHigh = True 

    if (rouletteZahl == 0):
        ergebnisLow = False
        ergebnisHigh = False

#Output



