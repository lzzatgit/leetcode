class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0) # pseudo head

    def insert(self, value):
        if not self.exists(value): # since hashset, we insert only when not exist
            new_node = Node(value, self.head.next)
            self.head.next = new_node

    def delete(self, value):
        prev = self.head # remember head here is a pseudo head
        curr = self.head.next # so this is the start of real values
        while curr:
            if curr.val == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr:
            if curr.val == value:
                return True
            curr = curr.next
        return False
