class TimeMap:

    def __init__(self):
        self.M = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.M:
            self.M[key] = []
        self.M[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.M:
            return ""
        l, r = 0, len(self.M[key]) - 1
        ans = ""
        while l <= r:
            mid = (l + r) // 2
            if self.M[key][mid][1] <= timestamp:
                ans = self.M[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
