class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x:int =1
        for i in range(len(nums)):
            if nums[i]>0:
                if i>0 and nums[i]==nums[i-1]:
                    continue
                else:
                    if nums[i]==x:
                        x+=1
                    else:
                        return x
        return x