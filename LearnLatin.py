import csv
import random

fileName = "database1.csv"
READ = 'r'
WRITE = 'w'
APPEND = 'a'
allDataList = []

#Spielbeschreibung
print("LearnLatinWithEase V 0.1")
print()

#Importieren der Daten aus dem CSV-Dokument
csvFile = open(fileName, mode = READ)
dataList = csv.reader(csvFile, delimiter=';')
for current in dataList:
    allDataList.append(current)
csvFile.close()
print("Daten erfolgreich importiert.")
print()

#Spiel startet
print("Spiel beginnt jetzt!")
print()
while True:
    randNum = random.randint(0,len(allDataList)-1)
    print(allDataList[randNum][2])
    #Kasusüberprüfung
    while True:
        answer1In = input("Bitte gebe den vorliegenden Kasus ein: ")
        if answer1In.upper() == 'EXIT':
            break
        elif answer1In.upper() == allDataList[randNum][0].upper():
            break
        else: 
          print("Leider falsch! Überlege noch einmal genau.")
    #Kasusfunktionsüberprüfung
    while True:
        answer2In = input("Bitte gebe nun die vorliegende Kasusfunktion ein (nur die Funktion ohne Kasus, z.B. als Attribut): ")
        if answer2In.upper() == 'EXIT':
            break 
        elif answer2In.upper() == allDataList[randNum][1].upper():
              break
        else: 
            print("Leider falsch! Überlege noch einmal genau.")
    print("Gut gemacht!")
    print()
    print()
    goOn = input("Fortsetzen? j/n: ")
    while goOn != 'j' and goOn != 'n':
        goOn = input("Fehler! Bitte noch einmal... j/n: ")
    if goOn == 'n':
        break
    print()


print("----Max Sandmann, V 0.1.1 , 26.11.2017----")

