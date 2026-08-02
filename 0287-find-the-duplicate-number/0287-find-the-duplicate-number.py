class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set(nums)
        for x in nums:
            if x not in s:
                return x
            else:
                s.remove(x)        