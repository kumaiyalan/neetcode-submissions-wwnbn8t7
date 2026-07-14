class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp = prices[:]

            for s, d, p in flights:
                if prices[s] != float("inf"):
                    tmp[d] = min(tmp[d], prices[s] + p)
            
            prices = tmp

        if prices[dst] != float("inf"):
            return prices[dst]
        else:
            return -1