class Solution:
    def maxProduct(self, n: int) -> int:
        n=str(n)
        n=[int(x) for x in n]
        n.sort()
        return n[-1]*n[-2]