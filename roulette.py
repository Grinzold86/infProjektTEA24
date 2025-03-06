
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
# Autor:    Linus Wohlgemuth, Nico Leder, ,   
# Datum:    4.3.2025  
# Version:  1.0   
###################################################################################################
# Beschreibung: 
# Diese Projekt verfolgt das Ziel einen Roulettetisch nach zu bilden
# Zu aller erst wählt man ein Feld aus und danach den Einsatz
# Der Algorithmus wählt zufällig eine Zahl und errechnet bei Gewinn den Erlös aus
###################################################################################################                                                                         

#Defines
import random           #ist notwendig um eine zufällige Zahl zu generieren
rouletteZahl = 0
eingabeZahl = 0
ergebnisZahl = False
ergebnisGerade = False
gewinn = 0
geradeRouletteZahl = True
geradeEingabeZahl = True

#Input
#erhuns job

#Algorithmus
#normal
rouletteZahl = random.randrange(0, 37)
if rouletteZahl == eingabeZahl:
    ergebnis  = True

#gerade/ungerade
if (rouletteZahl % 2) == 1:
    gerade = False

if (eingabeZahl % 2) == 1:
    gerade = False

#Output



