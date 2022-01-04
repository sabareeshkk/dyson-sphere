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
            while node.next is not self.head:
                node = node.next
            node.next = new_node
        new_node.next = self.head

    def splitLinkedList(self, lk_list_one, lk_list_sec):
        temp = self.head
        tortoise = self.head # slow i
        rabbit = self.head # fast 2i

        while (rabbit is not None and rabbit.next is not self.head and  rabbit.next.next is not self.head):
            tortoise = tortoise.next
            rabbit = rabbit.next.next

        if (rabbit.next.next is self.head):
            rabbit = rabbit.next
        
        lk_list_sec.head = tortoise.next
        rabbit.next = lk_list_sec.head   
        tortoise.next = temp
        lk_list_one.head = temp
        
    
    def printList(self):
        temp = self.head
        print("head data------", temp.data)
        if self.head is not None:
            while(True):
                print("%d" %(temp.data))
                temp = temp.next
                if (temp == self.head):
                    break








if __name__ == '__main__':
    l = LinkedList()

    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    
    l.printList()
    print("--------initial LinkedList-----")
    lk_list_one = LinkedList()
    lk_list_sec = LinkedList()
    lk_list = l.splitLinkedList(lk_list_one, lk_list_sec)

    lk_list_one.printList()
    print("----- second linked list-----")
    lk_list_sec.printList()