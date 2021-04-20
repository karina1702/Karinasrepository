#Leibniz Reihe 2

iterations = int(input("Anzahl der Durchläufeangeben: "))
i = 0
counter = 0
while i < iterations:
    counter += (((-1)**i)/(2*i+1))
    i += 1
    
print(counter*4)
