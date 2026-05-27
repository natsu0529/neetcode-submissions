class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a : dict = {}
        for i in nums:
            a[i] = a.get(i, 0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        for num, fre in a.items():
            bucket[fre].append(num)
        res = []
        for i in range(len(bucket) - 1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        
        