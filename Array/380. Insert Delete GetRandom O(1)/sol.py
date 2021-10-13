from random import choice
class RandomizedSet:

    def __init__(self):
        self.ary = []
        self.hashmap = {}


    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap[val] = len(self.ary)
            self.ary.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        last_element, idx = self.ary[-1], self.hashmap[val]
        self.ary[idx], self.hashmap[last_element] = last_element, idx
        self.ary.pop()
        del self.hashmap[val]
        return True


    def getRandom(self) -> int:
        return choice(self.ary)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
