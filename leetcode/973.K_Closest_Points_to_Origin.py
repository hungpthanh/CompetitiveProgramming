class Solution(object):
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = [(p[0] * p[0] + p[1] * p[1], p) for p in points]
        heapq.heapify(heap)
        results = [item[1] for item in heapq.nsmallest(k, heap)]
        return results
        
