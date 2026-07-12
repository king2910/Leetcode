class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        elif len(height)==2:
            return min(height)
        l=0
        r=len(height)-1
        m=0
        while l<r:
            m=max(m,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m        