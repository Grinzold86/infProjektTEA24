
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
    ergebnisZahl  = True

#gerade/ungerade
if (rouletteZahl % 2) == 1:
    geradeRouletteZahl = False

if (eingabeZahl % 2) == 1:
    geradeEingabeZahl = False

if(geradeEingabeZahl==geradeRouletteZahl):
    ergebnisGerade = True

#Low(1-18)/High(19-36)
if (rouletteZahl >= 1) and (rouletteZahl <= 18):
    ergebnisLowHigh = True
else: 
    ergebnisLowHigh = False

#Output



