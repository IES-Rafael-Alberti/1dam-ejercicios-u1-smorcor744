def mayor(n1,n2):
    if n1<n2 :
        return n2
    elif n2<n1 :
        return n1
    else:
        return 0


def main():
    num1 = input("Escribe un número: ")
    num2 = input("Escribe otro número: ")

    resultado = mayor(num1,num2)

    print(resultado)

if __name__ == "__main__":
    main()

