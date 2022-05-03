import pandas

def main():
    archivo = pandas.read_excel('ejemplo.xls')

    archivo.to_csv("ejemplo.csv")

if __name__ == "__main__":
    main()