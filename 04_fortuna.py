# Emilia Arredondo
# 14-04-2025

# galleta de la fortuna

import random

opciones = ["no persigas la felicidad, creala",
            "todas las cosas son dificiles antes de ser faciles,"
            "el pajaro madrugador consigue el gusano, pero el segundo raton consigue el queso",
            "alguien en tu vida necesita una carta de tu parte",
            "no solo pienses ¡actua!",
            "tu corazon se acelerara",
            "la fortuna que buscas esta en otra galleta",
            "ayuda! estoy prisionero en una panaderia china!"]

def fortuna():
    fortuna = random.randint(0, len(opciones)-1)
    print(opciones[fortuna])

fortuna()
fortuna()
fortuna()