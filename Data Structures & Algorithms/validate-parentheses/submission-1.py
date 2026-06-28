class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{",  "]": "["}
        stack = []
        for a in s:
            if a in dic:
                last = stack.pop() if stack else "#"
                if last !=  dic[a]:
                    return False
            else:
                stack.append(a)
        return not stack