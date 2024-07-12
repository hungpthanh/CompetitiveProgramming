class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = [1] * len(nums)
        multiplication = 1
        for i in range(0, len(nums)):
            answers[i] = multiplication
            multiplication = multiplication * nums[i]
        multiplication = 1
        for i in range(len(nums) - 1, -1, -1):
            answers[i] = answers[i] * multiplication
            multiplication = multiplication * nums[i]
        return answers
        
