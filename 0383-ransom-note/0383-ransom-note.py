class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        fm={}
        for i in magazine:
            if i in fm:
                fm[i]+=1
            else:
                fm[i]=1
        for i in ransomNote:
            if i in fm and fm[i]>0:
                fm[i]-=1
            else:
                return False
        return True            