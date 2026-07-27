class Solution:
    def compress(self, chars: List[str]) -> int:
        r=''
        c=1
        for i in range(1,len(chars)):
            if chars[i-1]==chars[i]:
                c+=1
            else:
                r+=chars[i-1]+(str(c) if c>1 else "")
                c=1
        r+=chars[-1]+(str(c) if c>1 else '')
        chars[:]=list(r)
        return len(r)       