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

    def add_first(self, data):
        """
        add item at the head of the linked list
        """
        new_head = Node(data)
        if self.head is None:
            self.head = new_head
            self.tail = new_head
        else:
            temp = self.head
            new_head.next = temp
            self.head = new_head
    
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
    
    def insert(self, data, index):
        """
        insert node in after nth element
        """
        new_node = Node(data)
        count = 0
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None or count < index:
                count += 1
                node = node.next
            temp = node.next
            new_node.next = temp
            node.next = new_node           

    def delete(self, data):
        """ind the previo
        delete node from linkedlist
        """
        if self.head is None:
            print("linked list is empty")
        else:
            node = self.head
            prev_node = None
            flag = True
            while flag:

                if node.data == data:
                    if prev_node is not None:
                        prev_node.next = node.next
                    else:
                        self.head = node.next
                    flag = False
                else:
                    if node.next is None:
                        print("no node find to delete")
                        flag = False
                prev_node = node
                node = node.next
    
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
