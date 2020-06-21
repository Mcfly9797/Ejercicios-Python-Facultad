'''Ejercicio 1.8 a). Recibo un numero N e imprimo su tabla de multiplicar hasta N'''

def main():

    print('Este programa recibe un numero N e imprime su tabla de multiplicar hasta N\n')
    num = int(input('Ingrese numero...'))
    for i in range(0, num): 
        print ( 'El numero '+str(num)+ ' multiplicado por '+str(i)+' es de :'+ str(num*i))
    
    input('\nPresione cualquier tecla para finalizar')

main()                                                                                              #Comienzo programa principal