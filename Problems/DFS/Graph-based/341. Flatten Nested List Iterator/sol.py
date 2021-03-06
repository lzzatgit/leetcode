# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat_lst = []
        def flatten_lst(nested_list):
            for nested_int in nested_list:
                if nested_int.isInteger():
                    self.flat_lst.append(nested_int.getInteger())
                else:
                    flatten_lst(nested_int.getList())
        self.next_pointer = 0
        flatten_lst(nestedList)

    def next(self) -> int:
        val = self.flat_lst[self.next_pointer]
        self.next_pointer += 1
        return val

    def hasNext(self) -> bool:
         return self.next_pointer < len(self.flat_lst)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
