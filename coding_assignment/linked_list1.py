class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printit(self):
        current = self.head
        if current is None:
            print("The list is empty.")
            return
        while current:
            print(current.data, end="  ")
            current = current.next
        print()

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, data):
        current = self.head
        if current is None:
            print("The list is empty. No nodes to remove.")
            return

        if current.data == data:
            self.head = current.next
            print(f"Node with value {data} has been removed.")
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print(f"Node with value {data} not found.")
            return
        prev.next = current.next
        print(f"Node with value {data} has been removed.")

    def add_at_pos(self, pos, data):
        new_node = Node(data)
        if pos < 0:
            print("Invalid position.")
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"Node with value {data} added at position {pos}.")
            return
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds.")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"Node with value {data} added at position {pos}.")

    def remove_at_pos(self, pos):
        if pos < 0:
            print("Invalid position.")
            return
        current = self.head
        if current is None:
            print("The list is empty. No nodes to remove.")
            return
        if pos == 0:
            self.head = current.next
            print("Node at position 0 has been removed.")
            return
        count = 0
        prev = None
        while current and count < pos:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("Position out of bounds.")
            return
        prev.next = current.next
        print(f"Node at position {pos} has been removed.")


ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
print("Linked List after adding nodes:")
ll.traverse()

ll.add_at_pos(1, 15)
print("Linked List after adding node with value 15 at position 1:")
ll.traverse()

ll.remove_at_pos(2)
print("Linked List after removing node at position 2:")
ll.traverse()

ll.add(40)
print("Linked List after adding node with value 40:")
ll.traverse()

ll.remove_at_pos(5)
ll.remove_at_pos(0)
print("Linked List after removing node at position 0:")
ll.traverse()


while True:
    print("1.Add node\n2.Remove node\n3.add at position\n4.remove at position\n5.Print linked list\n6.Exit")
    choice=int(input("Enter your choice : "))
    if choice==1:
        ll.add(int(input("Enter the value of the node to be added : ")))
    elif choice==2:
        ll.remove(int(input("Enter the value of Node to be deleted : ")))
    if choice==3:
        val=int(input("Enter the value of the node to be added : "))
        pos=int(input("Enter the position : "))
        ll.add_at_pos(pos,val)
    elif choice==4:
        pos=int(input("Enter the position of the Node to be deleted : "))
        ll.remove_at_pos(pos)
    elif choice==3:
        ll.printit()
    elif choice==4:
        break