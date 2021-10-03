class DLinkedList:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}

        self.head, self.tail = DLinkedList(), DLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.next.prev = node

    def _pop_tail(self):
        lru = self.tail.prev
        self._remove_node(lru)
        return lru

    def _remove_node(self, node):
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)

        if not node:
            return -1

        self._remove_node(node)
        self._add_node(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)

        if not node:
            newNode = DLinkedList()
            newNode.key = key
            newNode.value = value
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                self.size -= 1
                lru_key = tail.key
                del self.cache[lru_key]

        else:
            node.value = value
            self._remove_node(node)
            self._add_node(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
