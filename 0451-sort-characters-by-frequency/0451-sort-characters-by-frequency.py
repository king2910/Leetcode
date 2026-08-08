class Solution:
    def frequencySort(self, s: str) -> str:
        r=""
        f={}
        for char in s:
            if char in f:
                f[char]+=1
            else:
                f[char]=1
        f=dict(sorted(f.items(), key=lambda item: item[1],reverse=True))
        for k,v in f.items():
            r+=str(k)*v
        return r    