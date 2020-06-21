#Se desea crear una funcion que reciba horas, minutos y segundos. Y devuelva la cant de segundos 
#Funcion que recibe horas, min, seg y devuelve el total en segundos.
def to_seconds (horas, minutos, segundos):
    total = horas*3600+minutos*60+segundos #Una hora equivale a 3600 segundos, un minuto equivale a 60 segundos.
    return (total)

def main():
    hora = int(input('Ingrese hora... '))
    minutos = int(input('Ingrese minutos... '))
    segundos = int(input('Ingrese segundos... '))
    print("El total de segundos es de "+str(to_seconds(hora, minutos, segundos))) #Llamo a funcion para la impresion del total de segundos

main()