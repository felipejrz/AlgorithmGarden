# 412. Fizz Buzz

# Dado un número entero n, devuelve una respuesta de matriz de cadenas (1 indexada) donde:

# Respuesta [i] == "FizzBuzz" si es divisible por 3 y 5.
# Respuesta [i] == "Fizz" si yo es divisible por 3.
# Respuesta [i] == "Buzz" si es divisible por 5.
# Respuesta [i] == I (como una cadena) Si ninguna de las condiciones anteriores es verdadera.


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizzbuzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizzbuzz.append("Fizz")
            elif i % 5 == 0:
                fizzbuzz.append("Buzz")
            else:
                fizzbuzz += [str(i)]
        return fizzbuzz
