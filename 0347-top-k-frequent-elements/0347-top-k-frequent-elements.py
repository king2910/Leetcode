class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for x in nums:
            if x in f:
                f[x]+=1
            else:
                f[x]=1
        f=sorted(f, key=f.get,reverse=True)
        return f[:k]       