class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            return nums.index(max(nums))
        for i in range(len(nums)):
            if i==0:
                if nums[i]>nums[i+1]:
                    return i
            if i==len(nums)-1:
                if nums[i-1]<nums[i]:
                    return i
            if nums[i-1]<nums[i]>nums[i+1]:
                return i