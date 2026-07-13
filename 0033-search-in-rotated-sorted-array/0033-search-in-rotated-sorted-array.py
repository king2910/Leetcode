class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]-target==0:
                return l
            elif nums[r]-target==0:
                return r
            else:
                if abs(nums[l]-target)<abs(nums[r]-target):
                    l+=1
                else:
                    r-=1
        return -1  