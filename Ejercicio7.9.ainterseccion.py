#EJercicio 7.9.a
def interseccion(lista1, lista2):
    listaInter = []
    for i in lista1: #recorro primera lista
        for j in lista2: #recorro segunda lista
            if i == j: #comparo si el elemento actual que estoy recorriendo de la lista1 es igual al elemento de la lista 2
                listaInter.append(i) #En caso de igualdad agrego elemento
    return listaInter