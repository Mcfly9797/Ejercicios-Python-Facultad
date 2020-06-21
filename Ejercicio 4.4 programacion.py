##El programa dejara ingresar dos numeros naturales. E imprimira la secuencia de enteros comprendida en el primer numero ingresado y el segundo numero ingresado inclusive.
#Tiene las siguientes condiciones: 
# Si el numero es multimo de 3 debe imprimir la palabra "TRES". 
# Si el numero es multimo de 5 debe imprimir la palabra "CINCO". 
# Si el numero es multimo de 5 Y 5 debe imprimir la palabra "TRES Y CINCO"



def secuencia(n1,n2):
    
    if n1<n2:                   #Si el primer numero es menor que el segundo imprimo el ciclo de manera ascendente
        for x in range(n1,n2+1):
            multiplo(x)       
    else:
        for x in range (n1, n2-1, -1): #Si el primer numero es mayor al segundo imprimo el ciclo de manera descendente
            multiplo(x)


def multiplo(num):
    if num%3 == 0 and num%5 ==0:
        print("TRES Y CINCO")
    elif num%3 == 0:
        print("TRES")
    elif num%5 ==0:
        print("CINCO")
    else:
        print (str(num)) 
    

def main():
    print ("Ingrese dos numeros diferentes y el programa mostrara la secuencia de numeros entre ellos")
    n1 = int(input("Ingrese el primer numero... "))
    n2 = int(input("Ingrese el segundo numero... "))


    secuencia(n1,n2)
    input("Ingrese cualquier tecla para finalizar")

main()