from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for i in strs:
            c = ''.join(sorted(i))
            d[c].append(i)
        return list(d.values())