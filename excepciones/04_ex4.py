#emilia arredondo
#28-04-2025

#acceder a un valor en un diccionario
#sin que se rompa el programa si la clave no existe

def buscar_cantante():
    cantante = {
        "nombre": "Luis Miguel",
        "pais": "Puerto Rico"
    }

    try:
        clave = input("¿Qué quieres saber? (nombre o país): ")
        print("Resultado:", cantante[clave])
    except KeyError:
        print("Esa clave no existe")

buscar_cantante()
