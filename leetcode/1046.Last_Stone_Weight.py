class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-item for item in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, - abs(first - second))
        if len(stones) == 0:
            return 0
        return -stones[0]
