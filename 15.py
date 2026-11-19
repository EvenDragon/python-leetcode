class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        i,j,k = -1,1,len(nums)-1
        while i<len(nums)-2:
            i+=1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            j = i+1
            k = len(nums)-1
            while j<k:
                x = nums[i] + nums[j] + nums[k]
                if x == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    j+=1
                    k-=1
                elif x < 0:
                    j+=1
                elif x > 0:
                    k -= 1
        return ans
# I Hate this task