class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            c:int =0
            m:int =0
            for x in nums:
                if x:
                    c+=1
                else:
                    c=0
                if c>m:
                    m=c
            return m