# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Acarreo que se propaga
        head = ListNode(0)  # Nodo ficticio para simplificar el manejo de la lista
        current = head  # Puntero al nodo actual en la lista resultante

        # Mientras haya nodos en l1 o l2, o exista acarreo
        while l1 or l2 or carry:
            # Obtenemos los valores actuales de l1 y l2, o 0 si no hay más nodos
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Suma de los valores actuales y el acarreo
            total_sum = val1 + val2 + carry
            # Realiza una divivion pero el // funciona como floor redondea para abajo
            carry = total_sum // 10  # Actualizar acarreo
            # Se hace para que valores mayores de 9 no se inserte el carry y el valor que si se inserta
            new_digit = total_sum % 10  # Valor que se inserta en el nodo actual

            # Insertar el nuevo nodo con el dígito resultante
            current.next = ListNode(new_digit)
            current = current.next

            # Avanzar al siguiente nodo en l1 y l2, si existen
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Retornar la lista enlazada resultante, ignorando el nodo ficticio
        return head.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Acarreo que se propaga
        head = ListNode(0)  # Nodo ficticio para simplificar el manejo de la lista
        current = head  # Puntero al nodo actual en la lista resultante

        # Mientras haya nodos en l1 o l2, o exista acarreo
        while l1 or l2 or carry:
            # Obtenemos los valores actuales de l1 y l2, o 0 si no hay más nodos
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Suma de los valores actuales y el acarreo
            total_sum = val1 + val2 + carry
            # Realiza una divivion pero el // funciona como floor redondea para abajo
            carry = total_sum // 10  # Actualizar acarreo
            # Se hace para que valores mayores de 9 no se inserte el carry y el valor que si se inserta
            new_digit = total_sum % 10  # Valor que se inserta en el nodo actual

            # Insertar el nuevo nodo con el dígito resultante
            current.next = ListNode(new_digit)
            current = current.next

            # Avanzar al siguiente nodo en l1 y l2, si existen
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Retornar la lista enlazada resultante, ignorando el nodo ficticio
        return head.next
