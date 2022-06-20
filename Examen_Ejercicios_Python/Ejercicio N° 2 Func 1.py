#Ejercicio N°2

#La calculadora debe pedir al usuario un número y una operación de forma repetida.
#Tiene que ir guardando el valor del resultado acumulado.
#Cuando el usuario ingresa la palabra "salir" cuando pide la operación, tiene que mostrar el resultado del acumulado y salir del programa.


lista = []
res = 0
numero = 0
operacion = ""
valida = True
while operacion != "salir":
    operacion = input("Por favor ingrese una operacion: +,-,*,/ ").lower()
    if operacion != "salir":

        if operacion in ["+", "-", "*", "/"]:
            valida = True
            numero = int(input("Por favor ingrese un numero: "))
            if operacion == "+":

                res += numero
            elif operacion == "-":

                res -= numero
            elif operacion == "*":

                res *= numero
            elif operacion == "/":

                if numero != 0:
                    res /= numero
                else:
                    print("No se puede dividir sobre cero")

        else:
            valida = False
            print("Operacion no válida")

        if valida:
            lista.append((operacion, numero))
            print(lista)
        else:
            lista.append(("Operacion no valida", numero))
    else:
        print("el resultado final es: ", res)











