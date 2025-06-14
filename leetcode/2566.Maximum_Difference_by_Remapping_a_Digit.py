class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_value = num
        if num == 0:
            min_value = 1
        else:
            min_value = str(num)
            st = min_value[0]
            min_value = int(min_value.replace(st, '0'))
        max_value = str(num)
        st = 0
        while st < len(max_value) and max_value[st] == '9':
            st += 1
        max_source = '9' if st == len(max_value) else max_value[st]
        max_value = int(max_value.replace(max_source, '9'))
        return max_value - min_value
