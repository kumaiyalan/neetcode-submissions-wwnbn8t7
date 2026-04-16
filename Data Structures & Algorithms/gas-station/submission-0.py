class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start = 0
        fuel = 0
        
        for i in range(len(cost)):
            fuel += gas[i]
            fuel -= cost[i]

            if fuel < 0:
                start = i + 1
                fuel = 0
        
        return start

        