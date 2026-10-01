class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        items = {}
        if len(s) != len(t):
            return False
        for i in s:
            items[i] = items.get(i,0) + 1
        for i in t:
            if  i not in items or items[i] == 0:
                return False
            items[i] -= 1
        return True
