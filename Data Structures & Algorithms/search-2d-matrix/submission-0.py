class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1]:
            return False
        n = 0
        while matrix[n][-1] < target:
            n += 1
        row = matrix[n]
        l = 0
        r = len(row) - 1
        while l <= r:
            mid = (l + r) >> 1
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        

