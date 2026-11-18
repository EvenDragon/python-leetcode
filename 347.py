from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter()
        for i in nums:
            c[i] += 1
        return [x[0] for x in c.most_common(k)]