class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1], ]
        for i in range(2, numRows + 1):
            x = ans[-1].copy()
            x.append(0)
            for j in range(1, len(x)):
                x[j] += ans[-1][j - 1]
            ans.append(x)
        return ans