class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        top = max(piles)
        bot = 1
        while top >= bot:
            mid = (top + bot) >> 1
            time = sum((i + mid- 1) // mid for i in piles)
            if  time <= h:
                res = mid
                top = mid - 1
            else:
                bot = mid + 1
        return res
             
