#Ejercicio 4.13 modificado. La funcion recibe como parametro fecha (dia mes año) y retorna el signo zodiacal.

def signo_zodiaco(dia, mes, anio):
    if Ejercicio_biblioteca.fecha_valida(dia, mes, anio)
        if((dia >= 21 and mes == 3) or (dia <= 20 and mes == 4)):
            return "Aries"
        elif((dia >= 21 and mes == 4) or (dia <= 20 and mes == 5)):
            return "Tauro"
        elif((dia >= 21 and mes == 5) or (dia <= 20 and mes == 6)):
            return "Geminis"
        elif((dia >= 21 and mes == 6) or (dia <= 21 and mes == 7)):
            return "Cáncer"
        elif((dia >= 22 and mes == 7) or (dia <= 22 and mes == 8)):
            return "Leo"
        elif((dia >= 23 and mes == 8) or (dia <= 22 and mes == 9)):
            return "Virgo"
        elif((dia >= 23 and mes == 9) or (dia <= 21 and mes == 10)):
            return "Libra"
        elif((dia >= 23 and mes == 10) or (dia <= 22 and mes == 11)):
            return "Escorpio"
        elif((dia >= 23 and mes == 11) or (dia <= 21 and mes == 12)):
            return "Sagitario"
        elif((dia >= 22 and mes == 12) or (dia <= 20 and mes == 1)):
            return "Capricornio"
        elif((dia >= 21 and mes == 1) or (dia <= 19 and mes == 2)):
            return "Acuario"
        else:
            return "Piscis"
    else:
        return "FECHA INCORRECTA"    
    else:
        print('La fecha es invalida')
