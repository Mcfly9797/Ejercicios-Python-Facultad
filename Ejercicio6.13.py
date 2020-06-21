#Crear una funcion que reciba una cadena de caracteres y devuelva la misma sin vocales

def sin_vocales(cad):
    cad_nue=""                                                      #Creo la variable que voy a devolver
    cad_orig = cad.lower()                                          #Paso valores a minusculas para normalizar las comparaciones de vocales
    for c in cad_orig:                                              
        if c!= 'a' and c!='e' and c!='i' and c!='o' and c!='u':     #Si el caracter actual no es vocal la agrego a la cadena que devolvere
            cad_nue += c
    print(cad_nue)
    input('presione cualquier tecla para finalizar')