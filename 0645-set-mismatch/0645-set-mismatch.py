class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
            nums.sort()
            for x in range(1,len(nums)):
                if nums[x]==nums[x-1]:
                    d=nums[x]
            nums.remove(d)
            nums.append(0)
            for i in range(len(nums)):
                if nums[i]!=i+1:
                    return [d,i+1]