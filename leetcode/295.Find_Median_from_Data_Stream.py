class Heap:
    def __init__(self, sign):
        self.data = []
        self.sign = sign
        heapq.heapify(self.data)
    def add(self, number):
        heapq.heappush(self.data, self.sign * number)
    
    def get(self):
        if len(self.data) == 0:
            return -self.sign * 100005

        return self.sign * self.data[0]

    def pop(self):
        return heapq.heappop(self.data)

    def get_len(self):
        return len(self.data)

class MedianFinder:
    
    def __init__(self):
        self.min_heap = Heap(1)
        self.max_heap = Heap(-1)

    def _balance(self):
        while self.min_heap.get_len() > self.max_heap.get_len():
            top = self.min_heap.pop()
            self.max_heap.add(top)
        while self.max_heap.get_len() - 1 > self.min_heap.get_len():
            top = -self.max_heap.pop()
            self.min_heap.add(top)

    def addNum(self, num: int) -> None:
        if num > self.max_heap.get():
            self.min_heap.add(num)
        else:
            self.max_heap.add(num)
        self._balance()

    def findMedian(self) -> float:
        if self.min_heap.get_len() == self.max_heap.get_len():
            return 1.0 * (self.min_heap.get() + self.max_heap.get()) / 2
        return self.max_heap.get()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
