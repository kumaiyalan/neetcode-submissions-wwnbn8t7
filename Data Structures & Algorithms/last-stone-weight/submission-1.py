class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minStones = [-stone for stone in stones]
        heapq.heapify(minStones)

        while len(minStones) > 1:
            heaviestStone = -1 * heapq.heappop(minStones)
            secondHeaviest = -1 * heapq.heappop(minStones)

            if heaviestStone != secondHeaviest:
                heapq.heappush(minStones, (heaviestStone - secondHeaviest) * -1)
            
            
        if minStones:
            return minStones[0] * -1
        else:
            return 0

        