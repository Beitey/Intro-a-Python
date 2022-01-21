# Para este desafio usaremos listas, ciclos for

def transpuesta(matriz):
    dimension = len(matriz)
    transpuesta = []

    for columna in range(dimension):
        lista_aux = []
        for fila in range(dimension):
            lista_aux.append(matriz[fila][columna])
        transpuesta.append(lista_aux)

    return transpuesta


A = [[1,23,4],[411,424,6],[897,1324,12]]
print(A)
print("""
***********
""")
print(transpuesta(A))



## Mostrar en formato matriz

def ver_matriz(matriz):
    for fila in matriz:
        print(fila)
        
op = input("Ver en formato matriz? (s/n)\n")

if op == "s":
    ver_matriz(A)
    print("""
**********
""")
    ver_matriz(transpuesta(A))
