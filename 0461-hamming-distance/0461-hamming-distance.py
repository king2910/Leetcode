class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=0
        x=bin(x)[2:][::-1]
        y=bin(y)[2:][::-1]
        if len(x)<len(y):
            x+='0'*abs(len(x)-len(y))
        else:
            y+='0'*abs(len(x)-len(y))
        for i in range(len(x)):
            if x[i]!=y[i]:
                c+=1
        return c       