class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Inicializamos los conjuntos y la lista del resultado
        listA = set()
        listB = set()
        C = []

        # Iteramos a través de los índices de A y B
        for i in range(len(A)):
            # Agregamos los elementos actuales a los conjuntos
            listA.add(A[i])
            listB.add(B[i])

            # Calculamos los comunes y agregamos su tamaño al resultado
            comunes = listA & listB  # Intersección
            C.append(len(comunes))

        return C
