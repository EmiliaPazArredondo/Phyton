#ejercicio 1 conversión segura a número

# objetivo: pedir un núkmero al usuario y evitar errores si escribe letras

def pedir_numero ():
    try:
        numero = int(input("escribe un número entero:"))
        print("¡gracias! tu número es:", numero)
    except ValueError:
        print("eso no es un número válido, inténtalo otra vez.")

pedir_numero()