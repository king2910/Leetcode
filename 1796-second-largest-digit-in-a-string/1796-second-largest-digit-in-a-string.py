class Solution:
    def secondHighest(self, s: str) -> int:
        r=set()
        for x in s:
            if 48 <= ord(x) <= 57:
                r.add(int(x))
        r=list(r)
        r.sort()
        if len(r)==1 or len(r)==0:
            return -1
        else:
            return r[-2]