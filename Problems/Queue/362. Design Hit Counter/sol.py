class HitCounter:

    def __init__(self):
        """
        Initialize the data structure
        """
        self.deque = collections.deque()


    def hit(self, timestamp: int) -> None:
        """
        Add the hit to the deque.
        @param: timestamp - The current timestamp
        :type timestamp: int
        :rtype None
        """
        self.deque.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        """
        Return the number of the hit in the past 300 seconds
        @param: timestamp - The current timestamp
        :type timestamp - int
        :rtype int
        """
        while self.deque and timestamp - self.deque[0] >= 300:
            self.deque.popleft()
        return len(self.deque)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
