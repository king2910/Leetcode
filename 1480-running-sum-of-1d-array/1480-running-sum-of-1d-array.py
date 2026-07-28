class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        r=[]
        for x in nums:
            s+=x
            r.append(s)
        return r