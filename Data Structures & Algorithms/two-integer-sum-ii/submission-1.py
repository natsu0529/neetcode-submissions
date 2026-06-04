class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}
        for i, n in enumerate(numbers):
            if n in a:
                continue
            b = target - n
            if b in a:
                if i > a[b]:
                    return [a[b]+1, i+1]
                else:
                    return [i+1, a[b]+1]
            else:
                a[n] = i