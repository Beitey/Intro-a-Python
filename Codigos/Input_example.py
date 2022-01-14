# La funcion input recibe un texto ingresado por el usuario y lo retorna en formato
## string, esto lo podemos guardar en una variable

usuario = input("Ingrese su nombre:\n")
comida = input("Ingrese la comida que desea:\n")

# Si queremos recibir un numero debemos transformarlo en integer con la función int()
cantidad = int(input("Ingrese la cantidad que quiere comer:\n"))

print(f"Hola {usuario}, hoy te daremos {cantidad} de {comida}")


# También podemos detener el final del programa pidiendo un input, ya que python esperará a que
## se ingrese algo para continuar.
input("Introdusca cualquier cosa para salir\n")
