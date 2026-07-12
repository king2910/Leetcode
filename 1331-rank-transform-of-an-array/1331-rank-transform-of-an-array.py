class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d=list(set(arr))
        d.sort()
        f={}
        for i in range(len(d)):
            f[d[i]]=i+1
        r=[]
        for x in arr:
            r.append(f[x])
        return r        