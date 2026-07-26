class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        c=1
        r=set()
        for i in range(0,len(nums)):
            if nums[i-1]==nums[i]:
                c+=1
            else:
                c=1
            if c>len(nums)/3:
                r.add(nums[i])
        return list(r)