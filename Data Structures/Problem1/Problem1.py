def reverseArray(a, b):
    # [1, 2, 3, 4]
    #  0  1  2  3
    
    # Append
    # b += [6] Agregar un valor a un array en lugar de un append
    
    # Insert
    # Agregar un elemento en cualquier posicion [:n] donde n es el lugar donde se quier ingresar 
    # La numeracion es la de 0 a n 
    # b[:1] += [4] 
    
    
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
    del b[-1]
        
    print(b)
    
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr_count, arr)

    # fptr.write(' '.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()
