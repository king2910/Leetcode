class Solution:
    def findLucky(self, arr: List[int]) -> int:
        r=0
        f={}
        for x in arr:
            if x in f:
                f[x]+=1
            else:
                f[x]=1
        for key, value in f.items():
            if key==value:
                r=max(r,value)
        return r if r else -1   