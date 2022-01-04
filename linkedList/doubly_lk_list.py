class Node:

    def __init__(self, next=None, prev=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLkList:

    def __init__(self):
        self.head = None

    def add(self, data):

        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next

            new_node.prev = curr_node
            curr_node.next = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':

    l = DoublyLkList()

    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)

    l.printList()
