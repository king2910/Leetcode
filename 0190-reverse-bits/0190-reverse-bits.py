class Solution:
    def reverseBits(self, n: int) -> int:
        x=bin(n)[2:]
        if len(x)<32:
            x='0'*(32-len(x))+x
        x=x[::-1]
        return int(x,2)