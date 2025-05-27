# Emilia Arredondo 
# 30-04-2025

import random 

total = random.randint(1,6) + random.randint(1,6)

adivinanza = int(input("¿cúal es el total? 2-12:"))

while adivinanza != total:
    adivinanza = int(input("¿cúal es el total? 2-12:"))

print("Yupii, ¡¡lo adivinaste!!")