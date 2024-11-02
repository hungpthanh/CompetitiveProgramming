class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).most_common()
        max_count = counter[0][1]
        res = (max_count - 1) * (n + 1)
        for item in counter:
            if item[1] == max_count:
                res += 1
        return max(len(tasks), res)
