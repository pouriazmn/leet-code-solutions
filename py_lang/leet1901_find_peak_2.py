from typing import List


class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            max_mid, ind = -1, -1
            for i in range(len(mat[mid])):
                if mat[mid][i] > max_mid:
                    max_mid, ind = mat[mid][i], i
            asc = mid > 0 and max_mid > max(mat[mid - 1])
            dsc = mid < n - 1 and max(mat[mid + 1]) < max_mid
            if (asc and dsc) or (asc and mid == n - 1) or (dsc and mid == 0):
                return [mid, ind]
            elif asc:
                l = mid + 1
            else:
                r = mid

        return [l, mat[l].index(max(mat[l]))]