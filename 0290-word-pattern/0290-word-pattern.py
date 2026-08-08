class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        f={}
        s=s.split()
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in f:
                if f[pattern[i]]==s[i]:
                    continue
                else:
                    return False
            else:
                f[pattern[i]]=s[i]
        return len(f) == len(set(f.values()))