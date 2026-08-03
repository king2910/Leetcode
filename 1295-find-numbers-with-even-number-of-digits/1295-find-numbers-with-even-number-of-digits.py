class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        a=0
        for x in nums:
            if len(str(x))%2==0:
                a+=1
        return a        