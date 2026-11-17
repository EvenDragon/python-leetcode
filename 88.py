class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        j = len(nums1) - 1
        k = m - 1
        for i in range(len(nums2)-1, -1, -1):

            while (j>=0):
                if(k<0 or nums2[i]>=nums1[k]):
                    nums1[j] = nums2[i]
                    j-=1
                    break
                else:
                    nums1[j] = nums1[k]
                    nums1[k] = 0
                    k-=1
                    j-=1