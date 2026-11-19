class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = 0
        for i in nums:
            s ^= i
        for i in range(len(nums)+1):
            s ^= i
        return s