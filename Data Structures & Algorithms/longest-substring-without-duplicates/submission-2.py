class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        l = 0
        res = 0
        for i,cur in enumerate(s):
            if cur in memo and l <= memo[cur]:
                l = memo[cur] + 1
            memo[cur] = i
            res = max(res,i - l + 1)
        return res
        