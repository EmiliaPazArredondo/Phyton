#emilia arredondo contreras
#28-04-2025

#mostrar un elemento de una lista por su posición, manejando si la posición no existe

def mostrar_elemento():
    frutas = ["manzana", "banana", "naranja", "palta"]
    try:
        indice = int(input("elige una posición (0 a 3):"))
        print("fruta elegida:", frutas[indice])

    except IndexError:
        print("estaposición no existe en la lista")
    except ValueError:
        print("debes ingresar numero")

mostrar_elemento()