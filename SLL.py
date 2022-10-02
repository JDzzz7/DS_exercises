class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

def print_list(head: Node):
    if head is None:
        return
    else:
        print(f"{head.data}->", end=" ")
        head = head.next
        print_list(head)

def reverse_list(slist: Linked_list)->Linked_list:
    rev_list = Linked_list()
    recursion(slist.head, rev_list)
    return rev_list

def recursion(head: Node, rev_list: Linked_list)->Linked_list:
    if head is None:
        return
    else:
        node = Node(head.data)
        node.next = rev_list.head
        rev_list.head = node

        head = head.next
        recursion(head, rev_list)

def iter_rev(slist: Linked_list)->Linked_list:
    rev_list = Linked_list()
    while(slist.head):
        node = Node(slist.head.data)
        node.next = rev_list.head
        rev_list.head = node
        slist.head = slist.head.next
        print("Screaming into the void")
    return rev_list
        
if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    mySLL = Linked_list()
    mySLL.head = n1
    n1.next = n2
    n2.next = n3
    rev = reverse_list(mySLL)
    rev2 = iter_rev(mySLL)
    print_list(rev2.head)
    print("\n")
    print_list(rev.head)
