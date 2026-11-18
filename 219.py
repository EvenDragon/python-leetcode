from collections import Counter
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window: Counter[int] = Counter()
        els = 0
        for i in range(len(nums)):
            if window[nums[i]]>0:
                return True
            window[nums[i]]+=1
            els+=1
            if els > k:
                window[nums[i-k]] -=1
                els-=1
        return False