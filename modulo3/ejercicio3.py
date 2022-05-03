def mostrarPrimos(N):
    listaPrimos = []
    for n2 in range(N+1):
        if n2 < 2:
            continue
        for i in range((n2//2)+1):
            if i < 2:
                continue
            if n2 % i == 0:
                break
        else:
            listaPrimos.append(n2)
    return listaPrimos

def main():
    N = int(input("EScriba un número para N: "))
    array = mostrarPrimos(N)
    print(array)





if __name__ == "__main__":
    main()