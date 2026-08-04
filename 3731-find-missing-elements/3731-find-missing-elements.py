class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        r=[]
        i=0
        for x in range(nums[0],nums[-1]):
            if nums[i]!=x:
                r.append(x)
            else:
                i+=1
        return r        