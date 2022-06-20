#Ejercicio N°3

#Implemente el programa de la calculadora mediante una clase en python
#que tenga un método para cada operación.

class Calculadora:
    def __init__(self):
        self.res = 0

    def mostrar_resultado(self):
        print("el resultado es:", self.res)


    def sumar(self, x, y):
        self.res = x+y
        #print("el resultado de la suma es: ", suma)

    def restar(self, x, y):
        self.res = x-y
        #print("el resultado de la resta es: ", resta)

    def multiplicar(self,x, y):
        self.res = x*y
        #print("el resultado de la multiplicación es: ", multiplicacion)

    def dividir(self, x, y):
        if y != 0:
            self.res = x/y
            #print("el resultado de la división es: ", division)
        else:
            print("No se puede realizar una división sobre 0")



# c1 = Calculadora()
# c1.sumar(0,2)
# c1.mostrar_resultado()
# c1.multiplicar(0,2)
# c1.mostrar_resultado()
# c1.restar(0,2)
# c1.mostrar_resultado()
# c1.dividir(0,2)
# c1.mostrar_resultado()




