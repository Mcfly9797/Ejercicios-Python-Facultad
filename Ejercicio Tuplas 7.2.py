##Creo una funcion que reciba una tupla que contiene nombres de alumnos, e imprima un saludo por cada item
#7.2a
def saludo_alumnos(tup):            
    for i in tup:                                       #Recorro la tupla, cada item(i) es un elemento de la tupla
        print ("Estimado {} vote por mi".format(i))     #Pido al user que vote por mi con la funcion format
    input('Ingrese cualquier valor para finalizar')


##Creo una funcion que reciba una tupla que contiene nombres de alumnos, e imprima un saludo por cada item
#Modificacion agrego generos
#7.2b
def saludo_alumnos(tup):            
    for i in tup:                                       #Recorro la tupla, cada item(i) es un elemento de la tupla de dos dimensiones
        if i[1]=='M':                                       #Verifico si es masculino
            print ("Estimado {} vote por mi".format(i))     
        elif i[1]=='F':                                     #Verifico si es femenino
            print ("Estimada {} vote por mi".format(i))     
        else:                                               #el user es de genero no definido
            print ("Estimade {} vote por mi".format(i))    

    input('Ingrese cualquier valor para finalizar')
