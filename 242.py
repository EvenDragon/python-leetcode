from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s)!=len(t): return False
            letters1: Counter[str] = Counter()
            letters2: Counter[str] = Counter()
            for i in range(len(s)):
                letters1[s[i]]+=1
                letters2[t[i]]+=1
            print(letters1)
            print(letters2)
            return letters1==letters2
