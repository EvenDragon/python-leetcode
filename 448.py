class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        all = set([x for x in range(1,len(nums)+1)])
        return list(all-set(nums))