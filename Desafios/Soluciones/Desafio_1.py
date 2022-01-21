# Para este desafío deberemos usar operadores, if/elif/else, print, int e input.


# Primero pedimos los inputs

primer_num = int(input("Ingresa tu primer número:\n"))
operacion = input("""Ingresa la operacion que realizarás
(s) Suma
(r) Resta
(m) Multiplicacion
(d) Division
(p) potencia
(sqrt) Raiz
""")
# Aquí podemos pedir el segundo numero pero si pusimos raiz no será necesario

if operacion == "sqrt":
    output = pow(primer_num, 1/2)

segundo_num = int(input("Ingresa tu segundo número:\n"))

# Ahora comparamos al resto de operaciones

if operacion == "s":
    output = primer_num + segundo_num
    
elif operacion == "r":
    output = primer_num - segundo_num
    
elif operacion == "m":
    output = primer_num * segundo_num

elif operacion == "d":
    if segundo_num != 0:
        output = primer_num / segundo_num
        #Codigo para el extra
        if output % 1 == 0:
            output = int(output)
    else:
        output = "Lo siento, dividir por 0 es malo para la salud"
    
elif operacion == "p":
    output = primer_num ** segundo_num
    #Codigo para el extra
    if output % 1 == 0:
        output = int(output)
    
else:
    output = "Operacion no valida"
    


#Printeamos
    
print(output)
