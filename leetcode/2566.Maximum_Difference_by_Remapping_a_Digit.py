class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_value = num
        if num == 0:
            min_value = 1
        else:
            min_value = str(num)
            st = min_value[0]
            min_value = min_value.replace(st, '0')
            min_value = int(min_value)
        max_value = str(num)
        st = 0
        while st < len(max_value) and max_value[st] == '9':
            st += 1
        if st == len(max_value):
            max_source = '9'
            max_target = '9'
        else:
            max_source = max_value[st]
            max_target = '9'
        max_value = max_value.replace(max_source, max_target)
        max_value = int(max_value)
        return max_value - min_value

        
