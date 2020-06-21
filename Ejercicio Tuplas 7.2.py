##Creo una funcion que reciba una tupla que contiene nombres de alumnos, e imprima un saludo por cada item

def saludo_alumnos(tup):            
    for i in tup:                                       #Recorro la tupla, cada item(i) es un elemento de la tupla
        print ("Estimado {} vote por mi".format(i))     #Pido al user que vote por mi con la funcion format
    input('Ingrese cualquier valor para finalizar')
