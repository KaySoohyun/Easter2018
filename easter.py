
import string

# Crea un criptograma
# Toma un string y lo encripta utilizando el cifrado Cesar. 
# Rota x posiciones y reemplaza el string.
def cesarCipher(pista, x):
    code = ""
    char = 0
    asciiA = ord("a")
    asciiZ = ord("z") + 1
    # Para cada una de las letras del string tomado
    for letra in pista:
        asciiL = ord(letra)
        # Si el caracter es un espacio o signo de puntuacion, no se modifica
        if letra == " " or letra in string.punctuation:
            char = asciiL
        # Si el caracter se ubica despues de la posicion de Z, 
        # se reinicia el conteo desde la A.
        elif (asciiL + x) >= asciiZ:
            resto = (asciiL + x) - asciiZ
            char = asciiA + resto
        # Si el caracter no sobrepasa la posicion de la Z
        else:
            char = asciiL + x
        code = code + chr(char)
    return code

# TODO Crear un main donde se llame a la funcion e interactue con el usuario
# Opciones:
# 1 Cifra una frase, pide el numero de rotacion, la frase e imprime por pantalla
# 2 Da la opcion de ingresar manualmente el texto o tomar uno de un archivo,
#    lo cifra y lo exporta en un documento, se puede elegir el directorio
# 3 Imprime un menu de ayuda

        





