class Solution:
    def convertToBase7(self, num: int) -> str:
        r=''
        s=0
        if num<0:
            s=1
            num=num*(-1)
        while num >=7:
            r+=str(num%7)
            num=num//7
        if num<7:
            r+=str(num)
        if s:
            r+="-"
        return r[::-1]