class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_car = self.head

        while current_car.next is not None:
            current_car = current_car.next

        current_car.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self,value):
        if self.head.value ==value:
            self.head = self.head.next

    def delete_middle_node(self,node):
        if self.head is None:
            return

        if self.head.value == node:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == node:
                current.next = current.next.next
                return
            current = current.next

ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.delete_middle_node(20)
print("--My List--")
ll.display()
