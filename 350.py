from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        c1,c2 = Counter(), Counter()
        for i in nums1: c1[i]+=1
        for i in nums2: c2[i]+=1
        ans = []
        for i in c1.items():
            ans += [i[0]] * min(c1[i[0]], c2[i[0]])
        return ans