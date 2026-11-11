class Solution:
    def isPathCrossing(self, path: str) -> bool:
        yd={"N":1,"S":-1}
        xd={"E":1,"W":-1}
        seen={(0,0)}
        x,y=0,0
        for char in path:
            if char in yd:
                y+=yd[char]
            else:
                x+=xd[char]
            if (x,y) in seen:
                return True
            else:
                seen.add((x,y))
        return False