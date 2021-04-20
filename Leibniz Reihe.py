# Annäherung an Pi mittels Leibnis Reihe

def Leibnizreihe(Anzahl, k=0, prev=0):
    prev += ((-1)**k)/(2*k+1)
    if k >= Anzahl -1:
        return 4*prev
    return Leibnizreihe(Anzahl, k+1, prev)

print(Leibnizreihe(Anzahl = int(input('Bitte geben Sie an, wie viele Brüche berechnet werden sollen:\n'))))
