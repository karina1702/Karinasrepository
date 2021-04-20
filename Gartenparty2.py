# einfaches '=' Zeichen: Zuweisung

strWetter = input("Wochenendwetter - sonnig oder regnerisch")

# doppeltes '==' Zeichen: Vergleichsoperator 

if strWetter == "sonnig": 
    print("Gartenparty")
    
if strWetter != "sonnig" :
    print("Kellerparty")
if strWetter == "regnerisch":
    print("Kellerparty")
    
elif strWetter == "regnerisch" :
    print("Kellerparty")
else:
    print("bitte entweder 'sonnig' oder 'regnerisch' eingeben!")
    