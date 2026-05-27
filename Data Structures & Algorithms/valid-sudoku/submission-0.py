class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bor = set()
        for n,a in enumerate(board):
            area1 = n // 3
            for m,b in enumerate(a):
                area2 = m // 3
                if b == ".":
                    continue
                if ("r",n, b) in bor or ("c",m, b) in bor or (area1, area2, b) in bor:
                    return False
                bor.add(("r",n,b))
                bor.add(("c",m,b))
                bor.add((area1,area2,b))
        return True
                