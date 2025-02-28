# 434. Number of Segments in a String

# Dada una cadena s, devuelva el número de segmentos en la cadena.
# Un segmento se define como una secuencia contigua de caracteres no espaciales.


# Ejemplo 1:
# Entrada: s = "Hola, mi nombre es John"
# Salida: 5
# Explicación: Los cinco segmentos son ["Hola", "mi", "nombre", "es", "John"]

# Ejemplo 2:
# Entrada: s = "Hola"
# Salida: 1


class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split()
        return len(s)
