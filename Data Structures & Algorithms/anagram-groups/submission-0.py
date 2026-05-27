class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        for n in strs:
            chan = tuple(sorted(n))
            if chan not in a:
                a[chan] = []
            a[chan].append(n)
        return list(a.values())


        
        