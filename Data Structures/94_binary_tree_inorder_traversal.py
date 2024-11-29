class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Lista para almacenar el resultado del recorrido in-order
        result = []

        # Pila para mantener el rastro de los nodos a medida que bajamos por el árbol
        stack = []

        # Puntero que nos ayudará a recorrer el árbol. Comienza en la raíz.
        current = root

        # Bucle principal: sigue ejecutándose mientras haya nodos por visitar
        # ya sea en la pila o en el subárbol actual.
        while current or stack:
            # 1. Bajamos todo lo posible por la izquierda, agregando cada nodo a la pila.
            while current:
                # Agregar el nodo actual a la pila antes de movernos a su hijo izquierdo.
                stack.append(current)
                current = current.left  # Moverse al hijo izquierdo

            # 2. Cuando no hay más hijos izquierdos, procesamos el nodo más reciente de la pila.
            current = stack.pop()  # Sacamos el nodo de la cima de la pila

            # Agregamos el valor del nodo actual a la lista `result`.
            result.append(current.val)

            # 3. Ahora que hemos visitado el nodo actual, intentamos movernos a su hijo derecho.
            current = current.right

        # Cuando no quedan nodos por procesar, devolvemos el resultado del recorrido in-order.
        return result
