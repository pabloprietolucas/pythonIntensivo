import pickle




def mostrarAgenda(agenda):
    for contacto in agenda:
        print(f"{contacto['nombre']}: {contacto['numero']}")
    espera = input("Presione enter para volver al menú...")


def buscarContacto(agenda):
    termino = input("Escriba su término de búsqueda: ")
    encontrado = False
    for contacto in agenda:
        if termino.lower() in contacto['nombre'].lower() or termino in str(contacto['numero']):
            print(f"{contacto['nombre']}: {contacto['numero']}")
            encontrado = True
    if not encontrado:
        print("La búsqueda no obtuvo resultados")
    espera = input("Presione enter para volver al menú...")


def addContacto(agenda):
    nombre = input("Escriba el nombre: ")
    numero = int(input("Teclee el número: "))
    agenda.append({'nombre':nombre, 'numero': numero})
    espera = input("Presione enter para volver al menú...")
    return agenda


def main():
    f = open('agenda.bin', 'rb')
    agenda = pickle.load(f)
    f.close()
    opcion = None
    while opcion != 4:
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Ver agenda")
        print("4. Cerrar")
        opcion = int(input("Elija una opción: "))
        if opcion == 1:
            agenda = addContacto(agenda)
            f = open('agenda.bin', 'wb')
            pickle.dump(agenda, f)
            f.close
        elif opcion == 2:
            buscarContacto(agenda)

        elif opcion == 3:
            mostrarAgenda(agenda)
        elif opcion == 4:
            pass
        else:
            print("Inserte una opción válida")
    f = open('agenda.bin', 'wb')
    pickle.dump(agenda, f)
    f.close
    


if __name__ == "__main__":
    main()