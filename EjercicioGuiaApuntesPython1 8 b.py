'''Ejercicio 1.8 b). Recibo un numero N sumo la secuencia de numeros hasta llegar a N '''
def main():

    print('Este programa recibe un numero N suma la secuencia de numeros siguientes hasta llegar al mismo\n')
    num = int(input('Ingrese numero N...'))
    total = 0
    for i in range(1, num):                                                             #Repito bucle para recorrer la secuencias de numeros
        total = total + i
    print ('La suma de los totales es: '+ str(total))
    input('\nPresione cualquier tecla para finalizar')

main()