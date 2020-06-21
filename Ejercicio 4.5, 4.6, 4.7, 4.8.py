#Ejercicio 4.5 Funcion que recibe un año y devuelve si es bisiesto o no.
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


##Ejercicio 4.6 se solicita una funcion que reciba dos parametros(numeros) que representan mes y año y devuelven la cant de dias, utiliza la funcion anterior.
def cant_dias_mes(mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes==10 or mes == 12: ##valido que sean los meses de 31
        return 31
    if mes == 2:
        if es_bisiesto(anio):   #Valido si es bisiesto
            return 29
        else:
            return 28
    else:
        return 30


#Ejercicio 4.7 recibo dia mes y año y devuelvo con un booleano si es una fecha valida
def fecha_valida (dias, mes, anio):
    return (mes>0 and mes<=12 and dias>=1 and cant_dias_mes(mes, anio)>=dias) #El mes esta dentro de los parametros validos. y si los dias ingresados por el usuario coinciden con los devueltos por la funcion llamada.
   
    
#Ejercicio 4.8 Recibo una fecha y devuelvo la fecha del dia siguiente.
def fecha_siguiente(dia, mes, anio):
    if fecha_valida(dia,mes,anio):    
        if fecha_valida(dia+1,mes,anio): #Si la fecha ingresada es correcta, pruebo si la fecha ingresada sumada un dia es valida
            return (dia+1,mes,anio)
        elif fecha_valida(1,mes+1,anio): #SI la fecha ingresada mas un dia no es correcta, pruebo con el dia 1 del mes siguiente
            return (1,mes+1,anio)   
        else:
            return(1,1,anio+1)          #Si el mes siguiente no es correcto, pruebo con el año siguiente
    else:
        print('Ingreso una fecha invalida se devolvera la misma fecha ingresada')
        return(dia,mes,anio)

