class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=defaultdict(int)
        for x in s:
            c[x]+=1
        for i,x in enumerate(s):
            if c[x]==1:
                return i
        return -1