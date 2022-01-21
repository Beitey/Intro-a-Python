# Para este desafio usaremos funciones, if/elif/else, for o while, print, input

#Definimos la función:

def palindromo_opcion1(palabra):
    palabra_limpia = palabra.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    palabra1 = ""
    palabra2 = ""
    #recorremos la palabra hasta la mitad y guardamos la ultima y primera letra:
    for i in range( len(palabra_limpia)//2 ):
        palabra1 += palabra_limpia[0]
        palabra2 += palabra_limpia[-1]
        #Luego acortamos la palabra quitandole las letras añadidas a pal1 y pal2
        palabra_limpia = palabra_limpia[1:-1]
    #Comparamos si son iguales
    if palabra1 == palabra2:
        return True
    else:
        return False

def palindromo_opcion2(palabra):
    palabra_limpia = palabra.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    inversa = ""
    for letra in palabra_limpia:
        inversa = letra + inversa

    if palabra_limpia == inversa:
        return True
    else:
        return False
    
def palindromo_opcion3(palabra):
    palabra_limpia = palabra.lower().replace(" ","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    inversa = palabra_limpia[::-1]
    if palabra_limpia == inversa:
        return True
    else:
        return False

#Ana la loca SACÓ la LANA
print(palindromo_opcion1("Ana la loca SACÓ la LANA")) 
print(palindromo_opcion2("Ana la loca SACÓ la LANA")) 
print(palindromo_opcion3("Ana la loca SACÓ la LANA"))
