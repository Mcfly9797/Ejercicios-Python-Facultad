#Se desea crear una funcion que reciba un numero y devuelva su factorial

def factorial(num):
    resultado = 1
    for num in range(1,num+1):
        resultado *=num
               
    return resultado

#Main para probar la funcion
def main():
    fact = int(input('Ingrese numero que quiere su factorial'))
    print(str(factorial(fact)))
    input('\nPresione cualquier tecla para finalizar')
main()