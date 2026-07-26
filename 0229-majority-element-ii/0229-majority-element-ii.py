class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        f={}
        r=[]
        for x in nums:
            if x in f:
                f[x]+=1
            else:
                f[x]=1
        for key,val in f.items():
            if val>len(nums)/3:
                r.append(key)
        return r