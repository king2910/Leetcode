class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t=list(t)
        s=list(s)
        for char in t:
            if char in s:
                s.remove(char)
            else:
                return char