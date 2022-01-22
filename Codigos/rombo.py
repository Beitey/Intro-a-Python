def crear_rombo(numero):
    #Parte de arriba
    for i in range(1,numero+1):
        if i%2 != 0:
            print(" "*((numero-i)//2) + i*"*")
    
    #Parte de abajo
    for i in range(1,numero):
        if i%2 == 0:
            print(" "*((i//2)) + (numero-i)*"*")

