class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=-1
        r=-1
        c=0
        for i in range(len(nums)):
            if nums[i]==target:
                if c==0:
                    l=i
                    r=i
                    c+=1
                else:
                    r=l+c
                    c+=1
        return [l,r]        