#Ejercicio N°4

#Utilizando herencia de clase crear una clase llamada Calculadorax2 con el propósito de que los servicios aplique dos veces cada uno de los operadores.
#Por ejemplo:
#- Calculadorax2.sumar(x,y) devuelve el valor de x + y + y
#- Ejemplo:
    #- Calculadorax2.sumar(2,3) devuelva el valor 8. Porque hace la cuenta 2 **+ 3 + 3**

from Ejercicio3Classpython import Calculadora

class Calculadora2(Calculadora):


    def sumar(self, x,y):
        self.res = x + y + y

    def restar(self, x,y):
        self.res = x - y- y

    def multiplicar(self, x,y):
        self.res = x * y * y

    def dividir(self, x,y):
        if y != 0:
            self.res = x / y / y
        else:
            print("No se puede dividir sobre cero")


c4 = Calculadora2()
c4.mostrar_resultado()
c4.sumar(25,30)
c4.mostrar_resultado()
c4.restar(115,110)
c4.mostrar_resultado()
c4.multiplicar(5,8)
c4.mostrar_resultado()
c4.dividir(60,2)
c4.mostrar_resultado()




