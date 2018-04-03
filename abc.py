
# Devuelve el abecedario en mayusculas
def letter():
    i = 0
    a = []
    letras = range(ord("A"), ord("Z") + 1)
    for x in letras:
        a.append(chr(x))
        i += 1
    #a.fromlist(chr(letras))
    return a

# Toma un abecedario y una ubicacion, devuelve el abecedario
# comenzando desde la ubicacion dada.
def change(abc, x):
    a = abc[x:]
    b = abc[:x]
    return a + b
