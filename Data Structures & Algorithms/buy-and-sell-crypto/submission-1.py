class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr = prices[0]
        pro = 0
        for i in prices:
            if i < min_pr:
                min_pr = i
            else:
                pro = max(pro,i - min_pr)
        return pro
        