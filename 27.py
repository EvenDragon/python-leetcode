class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        ans = 0
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] != val:
                start += 1
                ans += 1
            else:
                if nums[end] == val:
                    end -= 1
                else:
                    nums[start], nums[end] = nums[end], nums[start]
                    ans += 1
                    start += 1
                    end -= 1
        return ans