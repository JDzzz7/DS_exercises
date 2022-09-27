# Simple singly linked list with insertion and deletion functions, working only with ints atm

# Node class to store data and point to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    # Function initialize the head of LL
    def __init__(self):
        self.head = None
    
    # Function to add a node to the end of the LL
    def append(self, data: int):
        node = Node(data)

        # Make head node the new node if LL is empty
        if self.head is None:
            self.head = node
            return

        # Traverse through LL until the last node
        tail = self.head
        while (tail.next):
            tail = tail.next

        # Add node to the end of the last node which points to NULL
        tail.next = node
    
    # Function to add a node after a specified node
    def insert_after(self, prev: Node, data: int):
        node = Node(data)
        if prev is None:
            return print("no such node found")
        node.next = prev.next
        prev.next = node

    # Function to add a node at the beginning of the LL
    def push(self, data: int):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    # Function to dequeue node from LL
    def dequeue(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            rtn = temp
            temp = None
            return print(f"{rtn.data} dequeued")

    # Function to pop node from LL (*****)
    def pop(self):
        tail = self.head
        prev = None
        if tail is None:
            return
        while (tail.next):
            prev = tail
            tail = tail.next
        rtn = prev.next
        prev.next = None
        return print(f"{rtn.data} popped")

    # Function to remove a specific node (*****)
    def remove(self, val: int):
        temp = self.head
        if temp is None:
            return
        if temp.data == val:
            rtn = temp
            self.head = temp.next
            temp = None
            return print(f"{rtn.data} removed")
        while (temp.next):
            prev = temp
            temp = temp.next
            if temp.data == val:
                rtn = temp
                prev.next = temp.next
                temp = None
                return print(f"{rtn.data} removed")
        if temp is None:
            return print(f"{val} is not in LL")
               
    # Function to print out the linked list
    def printList(self):
        if self.head is not None:
            temp = self.head
            while (temp.next):
                print(f"{temp.data}->", end="")
                temp = temp.next
            print(f"{temp.data}->None")
        else:
            return print("Linked list is empty.")

if __name__ == '__main__':
    myLL = linked_list()
    n1 = Node(5)
    n2 = Node(6)
    n3 = Node(7)
    n4 = Node(8)
    myLL.head = n1
    n1.next = n2
    n2.next = n3
    myLL.append(n4.data)
    myLL.insert_after(n1, 10)
    myLL.push(15)
    myLL.dequeue()
    myLL.pop()
    myLL.remove(10)
    myLL.printList()

