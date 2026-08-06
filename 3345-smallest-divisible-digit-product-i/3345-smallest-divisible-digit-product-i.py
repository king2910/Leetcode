class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if n%10==0:
                return n
            l=n
            s=1
            while l>0:
                s*=l%10
                if s%t==0:
                    return n
                l=l//10
            n+=1       