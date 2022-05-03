def aumentarTamaño(contraseña, clave):
    clavefinal=""
    for letra in contraseña:
        num = ord(letra)
        num *= 5
        clavefinal += str(num)
    clavefinal = cambiarPorLetras(clavefinal)
    clavefinal += clave
    return clavefinal
    
def disminuirTamaño(clave):
    clavefinal =""
    i=len(clave)-1
    while i > 32:
        clavefinal += clave[i]
        i -= 1
    return clavefinal

        
def convertirNumeritos(contraseña):
    clave =""
    for letra in contraseña:
        clave += str(ord(letra))
    return clave

def cambiarPorLetras(clave):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    i=0
    clavefinal=""
    while i<len(clave):
        aux = ""
        if i == (len(clave)-1):
            aux += clave[i]
        else:   
            aux += clave[i] + clave[i+1]
        
        clavefinal += abecedario[int(aux)%len(abecedario)]
        clavefinal = clavefinal[::-1]
        i += 2
    return clavefinal

def crearClave(contraseña):
    clave = convertirNumeritos(contraseña)
    clave = cambiarPorLetras(clave)
    while len(clave) != 32:
        if len(clave)<32:
            clave = aumentarTamaño(contraseña, clave)
        if len(clave)>32:
            clave = disminuirTamaño(clave)

    print(clave)

def main():
    contraseña = input("Escriba una contraseña de entre 6 y 12 caracteres: ")
    while len(contraseña)<6 or len(contraseña)>12:
        contraseña = input("Debe tener entre 6 y 12 caracteres: ")
    crearClave(contraseña)
    


if __name__ == "__main__":
    main()