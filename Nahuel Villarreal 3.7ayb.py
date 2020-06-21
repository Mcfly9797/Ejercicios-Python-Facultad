#Se desea crear un programa con dos funciones. 
#Las mismas deberan ser llamadas por el main y probadas por el usuario
#El programa recibe radio de un circulo y devuelve el area.


#Libreria que contiene la funcion Pi
import math

###Funcion "numero_pi" devuelve como resultado el valor del numero PI con cinco digitos decimales.
def numero_pi():
    pi = round(math.pi,5)
    return pi

###Funcion "radio_circulo" recibe el radio del circulo y devuelve area
def radio_circulo(radio):
    area = numero_pi() * radio**2                                                           #Utiliza funcion "numero_pi" para realizar el calculo del area
    return area

def main():

    print("El siguiente programa devolvera el area de un circulo ingresando su radio")
    radio = float(input('Ingrese radio del circulo... '))
    area = round( radio_circulo(radio), 2 )                                                 #Calculo area
    print("El radio del circulo es de " + str(area))
    input("Ingrese cualquier tecla para finalizar")

main()
