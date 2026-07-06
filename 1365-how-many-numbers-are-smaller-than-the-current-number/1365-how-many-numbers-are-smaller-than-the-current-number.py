class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=nums.copy()
        n.sort()
        f={}
        r=[]
        for i in range(len(n)):
            if n[i] not in f:
                f[n[i]]=i
        for x in nums:
            r.append(f[x])
        return r