# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Para recorrer una lista de nodo se puede hacer 
        # Se puede con un variable o con la misma lista
        # lista1 = list1
        # while lista1:
        #     # Para imprimir el valor es con .val y para movernos con .next
        #     print(lista1.val, end=" -> ")
        #     lista1 = lista1.next

        # Insertar nuevo nodo a un lista de nodos 
        # new_node = Node(4) # Cremos el nodo con el valor que querremos
        # if not head: # Si no existe el nodo se crea
        #     return new_node
        # current = head
        # while current.next:
        #     current = current.next
        # current.next = new_node
        # return head

        new_list = ListNode(0)
        current = new_list

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # Es mejor apuntar el nodo completo en vez del valor como list.val 
                list1 = list1.next # Movemos de nodo de la lista 
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        # Añade los nodos sobrantes 
        # Aqui verifica si list es None si no es agrega los sobrante de list 1 si si agrega list2
        current.next = list1 if list1 else list2
        # Asi se regresa la lista como si fuera un array
        return new_list.next        