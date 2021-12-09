class MyHashSet:

    def __init__(self):
        self.size = 769
        self.bucketArray = [Bucket() for i in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        pos = self._hash(key)
        self.bucketArray[pos].insert(key)

    def remove(self, key: int) -> None:
        pos = self._hash(key)
        self.bucketArray[pos].delete(key)

    def contains(self, key: int) -> bool:
        pos = self._hash(key)
        return self.bucketArray[pos].exists(key)

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Bucket:
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

# leetcode sol1

# time O(N/K) where K is the size and N is the total number of elements, N/K means the average length of each linked list,
# insert O(1), delete & exists O(N/K)

# space O(K + M) where K is the number of predefined buckets, and MM is the number of unique values that have been inserted into the HashSet.
