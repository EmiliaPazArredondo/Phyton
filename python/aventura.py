#trabajo aplicando conocimientos de phyton

Tareas=["Sacar dinero del banco","Hacer la colada","Dar un paseo","Cortarse el cabello","Preparar un té","Terminar el capítulo de listas","Lllamar a mamá","Ver my hero academia"]
print(Tareas)

#Desbloquear la primera misión: acceder a la primera tarea de la lista

indice = Tareas.index("Sacar dinero del banco")
print("Sacar dinero del banco")

#la tarea oculta: encontrar la 2da tarea de la lista

indice = Tareas.index("Dar un paseo")
print("Dar un paseo")

#Recuperar una sección perdida: obtener un subconjunto de tareas usando slicing

print(Tareas[4:])

#Error detectado: intentar acceder a un índice inexistente y manejar el error

try:
    print(Tareas[100])  # Índice fuera de rango
except IndexError:
    print("Intentaste acceder a una tarea que no existe.")


#Hacker de la lista: modificar la lista para añadir una nueva tarea sin usar append

Tareas += ["Aprender Python"]
print(Tareas)