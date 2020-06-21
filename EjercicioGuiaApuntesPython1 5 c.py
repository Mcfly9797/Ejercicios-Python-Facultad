'''Programa 1.5 c). Recibe dos numeros y realiza una suma, resta, multiplicacion y division entre ellos.'''
def main():

    print('Este programa recibe dos numeros y realiza una suma, resta, multiplicacion y division entre ellos.\n')
    
    num1 = float(input('Ingrese primer numero... '))
    num2 = float(input('Ingrese segundo numero...'))

    print ("\nLa suma de " + str(num1) +" y "+ str(num2) + " es: "+ str((num1+num2)))           #Suma
    print ("La resta entre " + str(num1) +" y "+ str(num2) + " es: "+ str((num1-num2)))         #Resta
    print ("La multiplicacion de " + str(num1) +" por "+ str(num2) + " es: "+ str((num1*num2))) #Multiplicacion

    if num2 != 0:                                                                               #Valido que no divida por 0
        resultado = num1/num2
    else:
        resultado = 'No se puede dividir por 0.\n'

    print ("La division de " + str(num1) +" por "+ str(num2) + " es: "+ str(resultado))         #Division
    input('\nPresione cualquier tecla para finalizar')

main()                                                                                          #Comienzo programa

