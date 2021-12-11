class MyHashMap:

    def __init__(self):
        self.size = 769
        self.hashmap = [[] for i in range(self.size)]

    def _hash(self, key):
        return key % self.size


    def put(self, key: int, value: int) -> None:
        pos = self._hash(key)
        found = False
        for idx, ele in enumerate(self.hashmap[pos]):
            if key == ele[0]:
                self.hashmap[pos][idx] = (key, value)
                found = True
                break
        if not found:
            self.hashmap[pos].append((key,value))

    def get(self, key: int) -> int:
        pos = self._hash(key)
        for (k, v) in self.hashmap[pos]:
            if key == k:
                return v
        return -1


    def remove(self, key: int) -> None:
        pos = self._hash(key)
        for idx, ele in enumerate(self.hashmap[pos]):
            if key == ele[0]:
                del self.hashmap[pos][idx]

# time: O(K/N): N is the number of all possible keys and K is the number of predefined buckets
# space: O(K + M): M is the number of unique keys that are inserted into the bucket
