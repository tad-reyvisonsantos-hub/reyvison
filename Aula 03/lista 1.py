# Aula 03 - Listas encadeadas

class Node:
      def __init__(self, data):
            self.data = data
            self.next = None

            def _repr_(self):
                  return f"Node list({self.data!r})"
            
class Linkedlist:
      def __init__(self):
            self.head = None

      def append(self, data):
            novo = Node(data)  
            if self.head is None:  #Lista vazia
                  self.head = novo    
                  return
            atual = self.head
            while atual.next is not None:  #vai andar até o último
                  atual = atual.next
            atual.next = novo              #encadeamento

      def __iter__(self):
            atual = self.head
            while atual is not None:
                  yield atual.data
                  atual = atual.next 

lista = Linkedlist()
lista.append("ab")
lista.append("ac")
lista.append("ad")

for item in lista:
      print(item)
    