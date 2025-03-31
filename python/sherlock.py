#Trabajo utilizando lo que aprendí en phyton

pistas = ("puerta roja",221, "londres", 3.14, "watson", 7,"moriarty")

print("¡Bienvenido, detective holmes!")
print("Se ha encontrado una serie de pistas misteriosas...")
print("pistas encontradas:", pistas)

# Análisis de pistas
print("\n Analizando las pistas...")

#Aquí va tu código de respuestas

#cúal es la primera pista?

print(pistas[0])

# cúal es la última pista?

print(pistas[6])

# cúantas pistas hay en total?

print(len(pistas))

# está la palabra "londres" en las pistas?

print("londres" in pistas)

# desempaqueta las primeras 3 pistas

pistas=("puerta roja","221","londres",)

a, b, c, = pistas

print(a, b, c)

# crea una nueva tupla con pistas adicionales

nuevas_pistas=("asesino","víctima","cuchillo")

print(nuevas_pistas)

# encuentra la posición de "watson"

pistas = ("puerta roja", 221, "londres", 3.14, "watson", 7, "moriarty")
posicion = pistas.index("watson")
print(posicion)


# cúantas veces aparece el número 7 en las pistas?

pistas = ("puerta roja", 221, "londres", 3.14, "watson", 7, "moriarty")
apariciones = pistas.count(7)
print(apariciones)


print("\n felicitaciones, detective. ¡has resuelto el análisis inicial de las pistas!")
print("Ahora, sigue con las deducciones para resolver el misterio.")