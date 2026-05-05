class MedianFinder:

    def __init__(self):
        self.numbers = []
        self.length = 0
        

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.length += 1
        

    def findMedian(self) -> float:
        size = self.length
        minHeap = self.numbers[:]
        heapq.heapify(minHeap)
        if size % 2 == 1:
            for i in range(size // 2):
                heapq.heappop(minHeap)
            return float(minHeap[0])
        else:
            for i in range((size // 2) - 1):
                heapq.heappop(minHeap)
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            avg = (x + y) / 2
            return float(avg)