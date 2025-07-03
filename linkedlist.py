class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.first = None
    def insertFirst(self, data):
        temp = Node(data)
        temp.next = self.first
        self.first = temp
    def removeFirst(self):
        if self.first is None:
            print("List is empty")
        else:
            cur = self.first
            self.first = self.first.next
            print("The deleted item is", cur.data)
    def display(self):
        if self.first is None:
            print("List is empty")
            return
        cur = self.first
        while (cur):
            print(cur.data, end=" ")
            cur = cur.next
            print()
    def search(self, item):
        if self.first is None:
            print("List is empty")
            return
        cur = self.first
        while cur is not None:
            if cur.data == item:
                return
                print("Item is present in the linked list")
            else:
                cur = cur.next
        print("Item is not present in the linked list")
sll = SinglyLinkedList()
while True:
    ch = int(input("\nEnter your choice: 1-Insert 2-Delete 3-Search 4-Display 5-Exit : "))
    if ch == 1:
        item = input("Enter the element to insert: ")
        sll.insertFirst(item)
        sll.display()
    elif ch == 2:
        sll.removeFirst()
        sll.display()
    elif ch == 3:
        item = input("Enter the element to search: ")
        sll.search(item)
    elif ch == 4:
        sll.display()
    elif ch == 5:
        break
    else:
        print("Invalid choice, try again!")