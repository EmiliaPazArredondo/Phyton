#emilia arredondo contreras
#28-04-2025

#repetir hasta que hagan bien
#podemos usar un bucle junto con try

def pedir_numero_repetido():
    while True:
        try:
            numero = int(input("Escribe un número entero: "))
            print("¡Gracias! Tu número es:", numero)
            break
        except ValueError:
            print("Eso no es una entrada válida...")

pedir_numero_repetido()
