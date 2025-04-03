#Emilia Arredondo
#02-04-2025
# estaba rico el completo, gracias profe

respuesta = input("estás cansado? (si/no):").strip() .lower()

cansado = respuesta == "sí"

if not cansado:
    print("¡Es hora de programar!")

else:
    print("Tómate un descanso, lo necesitas")