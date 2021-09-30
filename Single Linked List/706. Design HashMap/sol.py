class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2046
        self.hash_map = [[] for i in range(self.key_space)]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.key_space
        found = False
        for k, v in enumerate(self.hash_map[hash_key]):
            if key == v[0]:
                self.hash_map[hash_key][k] = (key,value)
                found = True
        if not found:
            self.hash_map[hash_key].append((key,value))


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.key_space
        for (k,v) in self.hash_map[hash_key]:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.key_space
        for k, v in enumerate(self.hash_map[hash_key]):
            if key == v[0]:
                del self.hash_map[hash_key][k]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
