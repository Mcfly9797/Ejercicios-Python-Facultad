#Se necesita una funcion que reciba un numero entero que devuelva un valor booleano dependiendo si es par o no.

def es_par(num):
    if num%2 == 0:           #Si el resto del la division por dos es 0 entonces el numero es par, en caso de que no impar.
        return True
    else:
        return False

def main():
    num = bool(input("Ingrese un numero entero para validar si es par... "))
     
    if es_par(num):
        print("El numero es par")
    else:
        print("El numero es impar")

    input("Presione cualquier tecla para finalizar")
    
main()