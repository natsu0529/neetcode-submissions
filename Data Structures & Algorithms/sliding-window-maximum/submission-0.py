class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # cur = []
        res = []
        # for i,a in enumerate(k):
        #     cur[i] = a
        for i in range(k - 1,len(nums)):
            res.append(max(nums[i - 2:i + 1])) 
        return res


        