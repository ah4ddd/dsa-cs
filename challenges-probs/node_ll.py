class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node # type: ignore

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)

ll.display()
