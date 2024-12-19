# Solucion inificiente
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()  # Usamos un conjunto para detectar ciclos

#         while n != 1:
#             # Convertimos el número en una lista de sus dígitos
#             digits = [int(digit) for digit in str(n)]
#             # print(f"Dígitos: {digits}")

#             # Calculamos la suma de los cuadrados de los dígitos
#             n = sum(digit**2 for digit in digits)
#             # print(f"Suma de cuadrados: {n}")

#             # Verificamos si ya hemos visto este número (para evitar ciclos infinitos)
#             if n in seen:
#                 return False  # No es un número feliz
#             seen.add(n)

#         return True


# Solucion mas eficiente
class Solution:
    def isHappy(self, n: int) -> bool:
        # Función auxiliar para calcular la suma de los cuadrados de los dígitos de un número
        def get_next(number):
            total = 0
            while number > 0:
                digit = number % 10  # Obtén el último dígito del número
                total += digit * digit  # Suma el cuadrado del dígito al total
                number //= 10  # Elimina el último dígito del número
            return total  # Devuelve la suma de los cuadrados de los dígitos

        # Inicializamos dos "punteros" para detectar ciclos
        slow = n  # Puntero lento: avanza un paso a la vez
        fast = get_next(n)  # Puntero rápido: avanza dos pasos a la vez

        # Iteramos mientras el puntero rápido no llegue a 1 (número feliz) o detectemos un ciclo
        while fast != 1 and slow != fast:
            slow = get_next(
                slow
            )  # Puntero lento avanza un paso (un cálculo de suma de cuadrados)
            fast = get_next(
                get_next(fast)
            )  # Puntero rápido avanza dos pasos (dos cálculos)

        # Si el puntero rápido llegó a 1, el número es feliz; de lo contrario, hay un ciclo
        return fast == 1
