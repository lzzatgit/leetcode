class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.v1_idx = 0
        self.v2_idx = 0
        self.next_val = None


    def iterate(self):
        if self.v1_idx < len(self.v1) and self.v2_idx < len(self.v2): # both vectors have elements
            if self.v1_idx <= self.v2_idx:
                self.next_val = self.v1[self.v1_idx]
                self.v1_idx += 1
            else:
                self.next_val = self.v2[self.v2_idx]
                self.v2_idx += 1
        elif self.v1_idx < len(self.v1): # only ele left in v1
            self.next_val = self.v1[self.v1_idx]
            self.v1_idx += 1
        elif self.v2_idx < len(self.v2): # only v2 has ele left
            self.next_val = self.v2[self.v2_idx]
            self.v2_idx += 1
        return self.next_val


    def next(self) -> int:
        if self.hasNext():
            val = self.next_val
            self.next_val = None
            return val

    def hasNext(self) -> bool:
        # 2 cases: if last method called is hasNext: then self.next_val might be not none; if last method called is next: then self.next_val must be none, but does not mean real none
        if self.next_val is not None:
            return True

        self.next_val = self.iterate()
        if self.next_val is None:
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
