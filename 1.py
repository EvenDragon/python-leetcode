class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_tuple = list(enumerate(nums, 0))
        nums_tuple.sort(key=lambda x:x[1])
        print(nums_tuple)
        start,end = 0,len(nums)-1
        ans = []
        while start<end:
            x = nums_tuple[start][1]+nums_tuple[end][1]
            if x==target:
                return([nums_tuple[start][0], nums_tuple[end][0]])
            elif x<target:
                start+=1
            else:
                end -=1