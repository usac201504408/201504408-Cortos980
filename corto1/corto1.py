



#variables 






#for i in range(2, 10): #numero de carnet 201504408 -> ultimos 3 digios son 408 - se coloca hasta 409 en el rango
    #se valida si el numero que toca es par o impar
termino = False
siguienteNumero = 18
resultadoDivision = 0

#metodo para escribir en archivo
def EscribirArchivo(listaEscribir):
    f = open('collatz.txt', 'w')
    try:
       f.write(str(listaEscribir))
    finally:
        f.close()

numero = 20
listaCompleta = list()

for i in range(2,21):
    listaActual = list()
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            listaActual.append(str(i))
        else:
            i = (i * 3) + 1
            listaActual.append(str(i))

        if i == 1:
            listaActual.append("termino")
    print(listaActual)
    listaCompleta.append(listaActual)

EscribirArchivo(str(listaCompleta) + "\n")

        


 
        
