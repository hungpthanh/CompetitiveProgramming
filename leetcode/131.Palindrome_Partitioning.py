class Solution:
    def partition(self, s: str) -> List[List[str]]:
        rs = "#" + s[::-1]
        s = "#" + s
        ans = [0]
        results = []
        def check_partition(ans):
            partitions = []
            for i in range(1, len(ans)):
                x, y = ans[i - 1] + 1, ans[i]
                if s[x: y + 1] != rs[len(s) - y: len(s) - x + 1]:
                    return False, []
                partitions.append(s[x: y + 1])
            return True, partitions

        def backtrack(index):
            if index == len(s) - 1:
                is_partition, partitions = check_partition(ans + [index])
                if is_partition:
                    results.append(partitions)
                return
            for i in range(2):
                if i == 1:
                    ans.append(index)
                backtrack(index + 1)
                if i == 1:
                    ans.pop()
        backtrack(1)
        return results

