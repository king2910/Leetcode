class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s=set()
        min=area
        p=[]
        for i in range(1,area+1):
            if i in s:
                continue
            elif area%i==0:
                r=int(area/i)
                if abs(r-i)<min:
                    min=abs(r-i)
                    if i>r:
                        p=[i,r]
                    else:
                        p=[r,i]
        return p        