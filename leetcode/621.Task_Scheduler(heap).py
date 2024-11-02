class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        start = {}
        counter = Counter(tasks).most_common()
        counter = [(-item[1], item[0]) for item in counter]
        heapq.heapify(counter)
        last = {}
        index = 0
        temp = deque()
        while len(counter) > 0 or len(temp) > 0:
            index += 1
            value, character = heapq.heappop(counter)
            last[character] = index
            if value + 1 < 0:
                temp.append((value + 1, character))
            if len(counter) == 0 and len(temp) > 0:
                index = last[temp[0][1]] + n
            while len(temp) > 0:
                value, c = temp[0]
                if index - last[c] < n:
                    break
                temp.popleft()
                heapq.heappush(counter, (value, c))
            

        return index
