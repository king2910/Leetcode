class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums)==1:
            return nums
        l=0
        r=1
        while r<len(nums):
            if nums[l]==0:
                if nums[r]!=0:
                    t=nums[l]
                    nums[l]=nums[r]
                    nums[r]=t
                    l+=1
                    r+=1
                else:
                    r+=1
            else:
                l+=1
                r+=1