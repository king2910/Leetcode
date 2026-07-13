class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f={}
        for x in nums:
            if x in f:
                f[x]+=1
            else:
                f[x]=1
        return min(f,key=f.get)