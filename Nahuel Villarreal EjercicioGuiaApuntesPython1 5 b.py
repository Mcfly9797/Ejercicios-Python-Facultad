'''Programa 1.5 b). Recibe base y altura de un rectangulo e imprime su area.'''

def main():

    print('Este programa recibe base y altura de un rectangulo e imprime su area.\n')
    base= float(input('Ingrese base de rectangulo...'))                                     
    altura= float(input('Ingrese la altura del rectangulo...'))
    area = base*altura                                                  #Calculo area 
    print('\nEl area es de: '+ str(area))
    input('\nPresione cualquier tecla para finalizar')

main()                                                                  #Comienzo programa principal.

