class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # map(str, digits): Convierte cada número del array en una cadena.
        # ''.join(...): Une las cadenas resultantes en una sola cadena sin separadores.
        # int(...): Convierte la cadena final en un número entero.
        num = int(''.join(map(str, digits)))
        num += 1 
        # str(num): Convierte el número resultante de vuelta a una cadena.
        # map(int, ...): Convierte cada carácter de la cadena en un entero.
        # list(...): Convierte el resultado del map() en una lista de enteros.
        return list(map(int, str(num)))