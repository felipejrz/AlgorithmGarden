def lonelyinteger(a):
    # Se crea un diccionario para guardar los numeros
    conteo = {}
    # Se ingresa el numero de veces que se repiden los numeros
    for num in a:
        # Conteo es un diccionario
        # Si el numero no existe en el diccionario, se inicializa en 0
        # Si el numero ya existe, se incrementa en 1
        # Luego se guarda el diccionario con los numeros y su cantidad de repeticiones
        conteo[num] = conteo.get(num, 0) + 1
        
    unicos = [num for num, count in conteo.items() if count == 1]

    return unicos[0]
        

if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    print(lonelyinteger(a))
    
