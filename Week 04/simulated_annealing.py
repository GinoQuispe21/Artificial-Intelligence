import random
import math

class Pais:
    def __init__(self, id, name, cord):
        self.id = id
        self.name = name
        self.cord = cord

paises = []
pais = Pais(1, "Venezuela", (35,40))
paises.append(pais)
pais = Pais(2, "Colombia", (15,35))
paises.append(pais)
pais = Pais(3, "Peru", (15,20))
paises.append(pais)
pais = Pais(4, "Brasil", (5,25))
paises.append(pais)
pais = Pais(5, "Chile", (10,5))
paises.append(pais)
pais = Pais(6, "Argentina", (25,10))
paises.append(pais)
pais = Pais(7, "Bolivia", (30,20))
paises.append(pais)

def printPaises(paises):
    for pais in paises:
        print(pais.id, " ", pais.name, " ", pais.cord)

printPaises(paises)

#datos
temperatura = 500
speed = 0.045

tour = paises

current = paises
best = paises
new = paises


#c) Elegimos ciudades aleatorias (aca empezaria el for)
# ciudad1 = random.randint(0,6)
# ciudad2 = random.randint(0,6)
ciudad1 = 3
ciudad2 = 5
print(ciudad1, ciudad2)
while(ciudad2 == ciudad1):
    ciudad2 = random.randint(0,6)

newTour = []
for i in range(len(tour)):
    if(i == ciudad1):
        newTour.append(tour[ciudad2])
    elif(i == ciudad2):
        newTour.append(tour[ciudad1])
    else:
        newTour.append(tour[i])

printPaises(newTour)

current = paises
best = paises
new = newTour

def distanceCountries(pais1, pais2):
    return math.sqrt(((pais2.cord[0] - pais1.cord[0])**2) + ((pais2.cord[1] - pais1.cord[1])**2))

def energy(path):
    energy = 0
    for i in range(len(path)):
        if(i == len(path) - 1):
            energy = energy + distanceCountries(path[i], path[0])
        else:
            energy = energy + distanceCountries(path[i], path[i+1])
    return energy

#d) Energia
#Current energy
current_energy = energy(current)

print("Current Energy", current_energy)

#new energy
new_energy = energy(new)

print("New Energy", new_energy)

#e) funcion de aceptacion
prob = 0
if(new_energy < current_energy):
    prob = 1
else:
    prob = math.exp((current_energy - new_energy)/temperatura)
print("Prob", prob)
#if(prob>random.random(0,1)):
if(prob>0.69):
    current = new

#actualizamos temperatura
temperatura = (1-speed) * temperatura
print(temperatura)