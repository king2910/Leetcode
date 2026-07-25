class Solution:
    def reverseVowels(self, s: str) -> str:
        v='aeiouAEIOU'
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l] in v:
                if s[r] in v:
                    t=s[l]
                    s[l]=s[r]
                    s[r]=t
                    l+=1
                    r-=1
                else:
                    r-=1
            else:
                l+=1
        return ''.join(s)        