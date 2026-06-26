class MedianFinder:

    def __init__(self):
        # maxheap
        self.left = [] 
        # minheap
        self.right = []

        heapq.heapify(self.left)
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if not self.left and not self.right:
            heapq.heappush(self.left, -num)
            return

        if num >= -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
        if len(self.right) - len(self.left) > 1:
            i = heapq.heappop(self.right)
            heapq.heappush(self.left, -i)
        elif len(self.left) - len(self.right) > 1:
            i = heapq.heappop(self.left)
            heapq.heappush(self.right, -i)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
        
        