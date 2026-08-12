class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = list(nums)
        subsets = [[]]
        
        for element in s:
            subsets += [current + [element] for current in subsets]
        return subsets