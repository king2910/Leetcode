class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        x=0
        i=0
        while x<=val and i<len(nums):
            x=nums[i]
            if nums[i]==val:
                nums.remove(nums[i])
            else:
                i+=1
        return len(nums)