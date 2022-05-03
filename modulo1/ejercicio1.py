import os, math

def recorrerLista(path):
    
    lista = os.scandir(path)
    for archivo in lista:

        if archivo.is_file():
            unidad = "B"
            tamaño = archivo.stat().st_size

            if tamaño > (10**9):
                tamaño /= (1073741824)
                unidad= "GB"
            elif tamaño > (10**6):
                tamaño /= 1048576
                unidad = "MB"
            elif tamaño > 1000:
                tamaño /= (1024)
                unidad = "KB"

            archivoruta = archivo.path
            if ruta in archivoruta:
                archivoruta = archivoruta.replace(ruta, "")
            if archivo.name in archivoruta:
                archivoruta = archivoruta.replace(archivo.name, "")
            archivoruta = archivoruta[1:]
            

            print(f"{archivoruta}{archivo.name}: {round(tamaño,2)} {unidad}" )

        elif archivo.is_dir():
            recorrerLista(archivo)

def main():

    global ruta 
    ruta = "C:/Users/Pablo"
    recorrerLista(ruta)
    
    
    


 
if __name__ == "__main__":
    main()