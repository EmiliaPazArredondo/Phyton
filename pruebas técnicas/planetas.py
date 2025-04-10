# Emilia Arredondo Contreras
# 09-04-2025

# Pesos Planetarios 🪐

print("Número Planeta        Gravedad relativa")
print("1   Mercurio                 0.38")
print("2   Venus                    0.91")
print("3   Marte                    0.38")
print("4   Júpiter                  2.53")
print("5   Saturno                  1.07")
print("6   Urano                    0.89")

             
peso = float(input("Ingresa tu peso terrestre 🌍: "))
numero = int(input("Ingresa un número de planeta 🪐 (1-6): "))

gravedad_relativa = {
    1: 0.38,
    2: 0.91,
    3: 0.38,
    4: 2.53,
    5: 1.07,
    6: 0.89
}

gravedad_r = gravedad_relativa.get(numero)

if gravedad_r is not None:
    peso_planeta = peso * gravedad_r
    print(f"Tu peso en el planeta es: {peso_planeta:.2f} kg")
else:
    print("Número no válido")
