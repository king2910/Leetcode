class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            r=[0]*len(nums)
            if nums.count(0)==1:
                i=nums.index(0)
                nums.remove(0)
                r[i]=math.prod(nums)
            return r
        p=math.prod(nums)
        return [p//i for i in nums]