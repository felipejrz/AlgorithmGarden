class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lista_nodo = head
        # Los sets en Python son una estructura de datos usada para almacenar elementos 
        # de una manera similar a las listas, pero con ciertas diferencias.
        # Los elementos de un set son único, lo que significa que no puede haber elementos duplicados.
        seen = set()  # Usamos un set para hacer un seguimiento de los valores vistos
        prev = None  # 'prev' es el nodo anterior al nodo actual
        
        while lista_nodo:
            if lista_nodo.val in seen:
                # Si el valor ya ha sido visto, eliminamos el nodo
                prev.next = lista_nodo.next
            else:
                # Si el valor no ha sido visto, lo agregamos al set y avanzamos
                seen.add(lista_nodo.val)
                prev = lista_nodo  # Actualizamos 'prev' al nodo actual
            
            lista_nodo = lista_nodo.next  # Avanzamos al siguiente nodo
        
        return head  # Devolvemos la cabeza de la lista modificada
