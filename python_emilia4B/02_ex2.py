# emilia arredondo
# 29-04-2025
# objetivo dividir entre 2 numeros y evitar o alertar

def division_segura():
    try:
        num1 = int(input("ingresa un número:"))
        num2 = int(input("ingresa otro número:"))
        resultado = num1 / num2
        print("el resultado de la division es:", resultado)
    except ZeroDivisionError:
        print("lo sentimos, no se puede realizar esta división")
    except ValueError:
        print("Error, sólo debes ingresar números enteros")

division_segura()