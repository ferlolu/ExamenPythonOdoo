#Ejercicio N° 1

#Realice un programa que simule las operaciones de una calculadora.
#El programa tiene que pedir el ingreso de un número, luego una operación (suma, resta, multiplicación, división)
# y luego un segundo número.
#Seguido, a esto debe mostrar el resultado.

Var_num1 = float(input("Introduzca un numero por favor: "))
Var_num2 = float(input("Introduzca otro numero por favor: "))

var_operacion = input("Introduzca la operacion que desea realizar por favor:\npara sumar: s\npara restar: r\npara multiplicar: m o p\npara dividir: d ").upper()

if var_operacion == "S":
    suma = Var_num1+Var_num2
    print(f"\nLa suma es: {suma}")
elif var_operacion == "R":
    resta = Var_num1-Var_num2
    print(f"\nla resta es:{resta}")
elif var_operacion == "M" or var_operacion == "P":
    mult = Var_num1*Var_num2
    print(f"\nla multiplicación es: {mult}")
elif var_operacion == "D":
    div = Var_num1/Var_num2
    print(f"\nLa división es: {div}")
else:
    print("\nSe equivoco de operación")
