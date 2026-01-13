class Solution(object):
    def findMaxK(self, nums):
        num_set = set(nums)
        result = -1
        for num in nums:
            if num > 0 and -num in num_set:
                result = max(result, num)
        return result