def reverseArray(b):
    # [1, 2, 3, 4]
    #  0  1  2  3
    
    # Append
    # b += [6] Agregar un valor a un array en lugar de un append
    # b += [6]  # Equivalente a b.extend([4]) Esta lo inserta al final de la cadena
    
    # Insert
    # Agregar un elemento en cualquier posicion [:n] donde n es el lugar donde se quier ingresar 
    # La numeracion es la de 0 a n 
    # b[:1] += [4] Esta es para insertar en un lugar en espesifico si es lo que queremos 
    
    
    # Remove
    # Con esta funcion for busca al valor que se quiere eliminar en este caso
    # la numeracion va de 1 a n donde 1 es el primer valor
    # re = 2
    # for i in range(len(b)):
    #     if b[i] == re:
    #         del b[i]  del eliminar al valor que se menciona
    #         break
        
    # Pop
    # Con el mismo del de remove con -1 ingreso al ultimo valor del array para eliminarlo con del
    # del b[-1] Elimina rl ultimo valor pero tener cuidado si el array solo contiene 1 valor
    
    # Corte
    # Con invertida = b[::-1] puedes invertir una cadena de numero en vez de usar un for
    
    
    li2 = []
    li2 = b[::-1]

    for i in li2:
        print(i, end=" ")

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    reverseArray(arr)