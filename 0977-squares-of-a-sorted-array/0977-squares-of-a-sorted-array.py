class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        r=[]
        for x in nums:
            r.append(x**2)
        r.sort()
        return r 