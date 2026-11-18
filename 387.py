from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter: Counter[str] = Counter()
        for i in s:
            counter[i]+=1
        for i,item in enumerate(s,0):
            if counter[item]==1: return i
        return -1