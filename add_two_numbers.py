# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Node: 
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

def reverse_list(lst: Linked_list)->Linked_list:
    rev_lst = Linked_list()
    recursive(lst.head, rev_lst)
    return rev_lst

def recursive(head: Node, lst: Linked_list):
    if head:
        node = Node(head.val)
        node.next = lst.head
        lst.head = node
        head = head.next
        recursive(head, lst)

def print_lst(head: Node):
    if head:
        print(f"{head.val}->", end=" ")
        print_lst(head.next)

class Solution:
    def pop(self, l1: Node)->Node:        
        tail = l1
        prev = None
        while(tail.next):
            prev = tail
            tail = tail.next
        rtn = prev.next
        prev.next = None
        return rtn.val

    def reg_array(self, l1: Node)->list:
        array = []
        while(l1.next):
            array.append(self.pop(l1))
        array.append(l1.val)
        return array
    
    def convert_to_string(self, array:list)->str:
        string = ""
        for i in range(len(array)):
            array[i] = str(array[i])
        for j in array:
            string += j
        return string

    def addTwoNumbers(self, l1: Node, l2: Node)->Node:
        str1 = self.convert_to_string(self.reg_array(l1))
        str2 = self.convert_to_string(self.reg_array(l2))
        total = int(str1) + int(str2)
        total = list(str(total))
        head = Node(total.pop())
        temp = head
        while (len(total) > 0):
            node = Node(total.pop())
            while temp.next:
                temp = temp.next
            temp.next = node
        return head

if __name__ == '__main__':
    new_list = Linked_list()
    another_list = Linked_list()
    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(3)
    a1 = Node(5)
    a2 = Node(6)
    a3 = Node(4)

    new_list.head = n1
    n1.next = n2
    n2.next = n3

    another_list.head = a1
    a1.next = a2
    a2.next = a3

    # print_lst(new_list.head)
    # rev_lst = reverse_list(new_list)
    # print()
    # print_lst(rev_lst.head)
    answer = Solution()
    print_lst(answer.addTwoNumbers(new_list.head, another_list.head))

