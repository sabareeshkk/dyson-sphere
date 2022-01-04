class Node:
    """
    nodes for linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    singly linked list
    """
    def __init__(self):
        self.head = None
        self.tail = None

    
    def add(self, data):
        """
        add item at the end of the linked list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node
    
    
    def reverse(self):
        curr_node = self.head
        prev_node = None
        if curr_node is None:
            print("no node find to reverse")
        else:
            while curr_node.next is not None:
                if prev_node is not None:
                    temp =  curr_node.next
                    curr_node.next = prev_node
                    prev_node = curr_node
                    curr_node = temp
                else:
                    temp = curr_node
                    curr_node = temp.next
                    prev_node = temp
                    prev_node.next = None
            curr_node.next = prev_node
            self.head = curr_node









if __name__ == '__main__':
    l = LinkedList()

    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)

    # reverse linked_list
    l.reverse()
    
    while l.head != None:
        print(l.head.data, end=" ")
        l.head = l.head.next
