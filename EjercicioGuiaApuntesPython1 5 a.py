'''Programa 1.5 a). Recibe base y altura de un rectangulo e imprime su perimetro.'''


def main():                                                             

    print('Este programa recibe base y altura de un rectangulo e imprime su perimetro.\n')

    base = float (input('Ingrese base de rectangulo...'))               
    altura= float (input('Ingrese la altura del rectangulo...'))       
    perimetro= base*2+altura*2                                          #Calculo area
    
    print('\nEl perimetro es de: '+ str(perimetro))
    input('\nPresione cualquier tecla para finalizar')

main()                                                                  #Comienzo el programa principal.
