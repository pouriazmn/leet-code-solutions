class Solution:
    MOD = 10 ** 9 + 7
    dynamic_table = [[[0, 0] for _ in range(1001)] for x in range(1001)]

    def module_sum(self, iterator_):
        r = 0
        for x in iterator_:
            r = (r + x) % self.MOD
        return r

    def kInversePairs(self, n: int, k: int) -> int:

        if n == 0:
            return 0
        elif k == 0:
            return 1
        elif self.dynamic_table[n][k][0] > 0:
            return self.dynamic_table[n][k][0]
        else:

            if not self.dynamic_table[n - 1][k][1]:
                self.dynamic_table[n - 1][k][1] = self.module_sum(
                    self.kInversePairs(n - 1, k1) for k1 in range(k, -1, -1))
            upper = self.dynamic_table[n - 1][k][1]
            if k >= n:
                if not self.dynamic_table[n - 1][k - n][1]:
                    self.dynamic_table[n - 1][k - n][1] = self.module_sum(
                        self.kInversePairs(n - 1, k1) for k1 in range(k - n, -1, -1))
                lower = self.dynamic_table[n - 1][k - n][1]
            else:
                lower = 0
            self.dynamic_table[n][k][0] = (upper - lower + self.MOD) % self.MOD
            return self.dynamic_table[n][k][0]


if __name__ == '__main__':
    s = Solution()
    s.kInversePairs(4, 0)
    s.kInversePairs(4, 1)
    s.kInversePairs(4, 2)
    s.kInversePairs(4, 3)
    s.kInversePairs(4, 4)