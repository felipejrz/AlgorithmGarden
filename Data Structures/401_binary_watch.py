# 401. Binary Watch

# Un reloj binario tiene 4 LED en la parte superior para representar las horas (0-11) y 6
# LED en la parte inferior para representar las actas (0-59). Cada LED representa un cero o uno,
# con la broca menos significativa a la derecha.

# Por ejemplo, el siguiente reloj binario dice "4:51".
# Dado un entero Turnon que representa el número de LED que están actualmente (ignorando el PM),
# devuelve todas las veces posibles que el reloj podría representar. Puede devolver la respuesta en cualquier orden.

# La hora no debe contener un cero líder.

# Por ejemplo, "01:00" no es válido. Debería ser "1:00".
# El minuto debe consistir en dos dígitos y puede contener un cero líder.

# Por ejemplo, "10: 2" no es válido. Debería ser "10:02".

# Ejemplo 1:

# Entrada: Turnon = 1
# Salida: ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00" , "4:00", "8:00"]
# Ejemplo 2:

# Entrada: Turnon = 9
# Producción: []


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        resultados = []

        # Recorrer todas las combinaciones de horas (0-11) y minutos (0-59)
        for h in range(12):  # 4 bits (0-11)
            for m in range(60):  # 6 bits (0-59)
                # Contamos los bits en 1 de h y m
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    # Formateamos el resultado asegurando que los minutos tengan dos dígitos
                    resultados.append(f"{h}:{m:02d}")

        return resultados
