from node import Node

#Código para crear un stack o "pila"
class Stack:
    #Se inicia la clase sin valores
    def __init__(self):
        self.top = None
        self.size = 0

    #Este método sirve para agregar valores al stack teniendo como parámetro el dato a agregar
    def push(self, data):
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

        self.size += 1

    #Este método es para eliminar datos del stack, elimina el último en entrar utilizando el principio LIFO (Last in first out)
    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None

            return data
        
        else:
            return "The stcak is empty"

    #Muestra el último valor en el stack, si no hay ninguno muestra el mensaje
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"


    #Método para limpiar todos los valores del stack
    def clear(self):
        while self.top:
            self.pop()