class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        memo = {}
        l = 0
        res = 0
        maxi = 0
        for i,a in enumerate(s):
            memo[a] = memo.get(a,0) + 1
            maxi = max(maxi,memo[a])
            if i - l - maxi +1 > k:
                memo[s[l]] -= 1
                l += 1
            res = max(res,i - l + 1)
        return res






