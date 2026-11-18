class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        summ = 0
        d = dict()
        d[0] = 1
        for i in nums:
            summ+=i
            ans+= d.get(summ-k,0)
            d[summ] = d.get(summ,0)+1
        return(ans)