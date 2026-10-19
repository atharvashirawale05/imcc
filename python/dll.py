class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode
        newnode.prev = temp

    def count_occurrence(self, key):
        count = 0
        temp = self.head

        while temp:
            if temp.data == key:
                count += 1
            temp = temp.next

        return count


# Main program
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(10)
dll.append(30)
dll.append(10)
dll.append(40)

key = int(input("Enter the number to count: "))

print("Occurrence:", dll.count_occurrence(key))