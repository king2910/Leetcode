class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l: int =-1
        r: int =-1
        c: int =0
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