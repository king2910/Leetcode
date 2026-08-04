class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for x in accounts:
            if m<sum(x):
                m=sum(x)
        return m        