from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for x , c in cnt.items():
            buckets[c].append(x)
        res = []
        for i in range(len(nums), 0, -1):
            for x in buckets[i]:
                res.append(x)
                if len(res) == k:
                    return res


        
        