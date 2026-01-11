class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end= " -> ")
            current = current.next
        print("None")

    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete_last_element(self):
        end_node = self.head

        if end_node is None:
            return

        if end_node.next is None:
            self.head = None
            return

        while end_node.next.next is not None:
            end_node = end_node.next
        end_node.next = None


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.delete_last_element()
    ll.display()
