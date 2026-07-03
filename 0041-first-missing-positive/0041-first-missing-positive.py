class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums=[x for x in nums if x>0]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1