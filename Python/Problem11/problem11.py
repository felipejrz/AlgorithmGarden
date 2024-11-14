def print_formatted(number):
    ancho = len(bin(number)) - 2  # La longitud de la representación binaria, excluyendo el prefijo '0b' se elimina con [2:]

    for i in range(1, number + 1):
        print(f"{i:>{ancho}} {oct(i)[2:]:>{ancho}} {hex(i)[2:].upper():>{ancho}} {bin(i)[2:]:>{ancho}}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)