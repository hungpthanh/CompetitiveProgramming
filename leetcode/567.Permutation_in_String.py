class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        if len(s1) == len(s2):
            return count_s1 == count_s2
        index = len(s1)
        while True:
            if count_s1 == count_s2:
                return True
            if index >= len(s2):
                break
            if s2[index] not in count_s2:
                count_s2[s2[index]] = 0
            count_s2[s2[index]] += 1
            count_s2[s2[index - len(s1)]] -= 1
            if count_s2[s2[index - len(s1)]] == 0:
                count_s2.pop(s2[index - len(s1)])
            index += 1
        return False
