class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        remain = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            if gas[i] + remain < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]

        return start
        
