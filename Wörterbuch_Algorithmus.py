# 1) Eingabe Suchbeggriff (deutsch)
# 2) Bestimmung der gesamtanzahl der Elemente ( = maximaler Index )
# 3) Schleife: Vergleich Eingabe mit jew. Listenelement
# 4) Wenn Element gefunden -> Index speichern
# 5) Zugriff auf Listenelement[Index] in Liste (englisches Wörterbuch)
'''
woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
print(woerterbuch_deutsch)
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]


Wort = input("Bitte geben Sie Ihr Wort ein das Sie ins Englische übersetzen wollen:")

Index_Wort = 0
k = 0
Iterationen = len(woerterbuch_deutsch)

while k < Iterationen:
    
    if woerterbuch_deutsch[k] == Wort:
        Index_Wort = k
    
    k += 1


print("Ihr Wort lautet Übersetzt:", woerterbuch_english[Index_Wort] )
'''
#Richtig / Schöner

woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
print(woerterbuch_deutsch)
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

Auswahl = input("Was möchten Sie tun? \n Einfügen [E] \n Löschen [L] \n Abfragen [A]:" )

Auswahl = Auswahl.upper()

if Auswahl == "E":
    Wort = input("Bitte geben Sie ihr deutsches Wort ein: ")
    woerterbuch_deutsch.append(Wort) #Wort in Liste hinzufügen
    Word = input("Bitte geben Sie ihr englisches Wort ein: ")
    woerterbuch_english.append(Word)
    
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
    
elif Auswahl == "L" or Auswahl == "l":
    Wort = input("Welches Wort Möchten sie löschen? ")
    
    Index_Wort = 0
    k = 0
    Iterationen = len(woerterbuch_deutsch)
    
    while k < Iterationen:
    
        if woerterbuch_deutsch[k].lower() == Wort.lower():
            Index_Wort = k
            woerterbuch_deutsch.remove(woerterbuch_deutsch[Index_Wort])
            woerterbuch_english.remove(woerterbuch_english[Index_Wort])
            break
    
        elif woerterbuch_english[k].lower() == Wort.lower():
            Index_Wort = k
            woerterbuch_english.remove(woerterbuch_english[Index_Wort])
            woerterbuch_deutsch.remove(woerterbuch_deutsch[Index_Wort])
            break
        k += 1
        
    print(woerterbuch_deutsch)
    print(woerterbuch_english)
        
else: 

    Wort = input("Bitte geben Sie Ihr Wort ein das Sie ins Englische übersetzen wollen:")

    Index_Wort = 0
    k = 0
    Iterationen = len(woerterbuch_deutsch)

    while k < Iterationen:
    
        if woerterbuch_deutsch[k].lower() == Wort.lower():
            Index_Wort = k
            print("Ihr Wort lautet Übersetzt:", woerterbuch_english[Index_Wort] )
            break
    
        k += 1
    if k == max:
        print("Ihr Wort wurde nicht gefunden")



'''
piviertel = 0
k = 0
Iterationen = int(input("Bitte geben Sie die gewünschte Anzahl an Iterationen ein:"))

while k < Iterationen:
    
    
    print("k=" , k )
    piviertel =  piviertel + (  ( -1 ) ** k )  / ( 2*k + 1 )
    k = k + 1
    print("pi viertel =" , piviertel )
    
pi = piviertel * 4
print("pi=" , pi )
'''