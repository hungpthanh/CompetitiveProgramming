class Solution:
    def maxRepOpt1(self, text: str) -> int:
        st = 0
        n = len(text)
        text = text + "#"
        st = 0
        spare_array = []
        for i in range(n + 1):
            if text[i] != text[st]:
                spare_array.append((text[st], i - st))
                st = i
        
        counter = Counter(text)
        k = len(spare_array)
        res = 0
        for i in range(1, k - 1):
            if (spare_array[i - 1][0] == spare_array[i + 1][0]) and spare_array[i][1] == 1:
                r = counter[spare_array[i - 1][0]] - spare_array[i - 1][1] - spare_array[i + 1][1]
                if r > 0:
                    res = max(res, spare_array[i - 1][1] + spare_array[i + 1][1] + 1)
                else:
                    res = max(res, spare_array[i - 1][1] + spare_array[i + 1][1])
        
        for i in range(k):
            if counter[spare_array[i][0]] - spare_array[i][1] > 0:
                res = max(res, spare_array[i][1] + 1)
            else:
                res = max(res, spare_array[i][1])
        
        return res
