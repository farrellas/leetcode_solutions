class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumWealth = 0
        for customer in accounts:
            maximumWealth = max(maximumWealth, sum(customer))
        return maximumWealth