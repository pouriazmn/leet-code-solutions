"""
link: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
the most important thing about this question was that you can not divide in modular operations
see this geeks-for-geeks: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

for the dividing by 2 of range_sum you should add the modInverse(2, 10^9+7) = 500000004
"""
from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def range_sum(self, upper, num):
        if num == 1:
            return upper

        return (((((upper + upper - num + 1) % self.MOD) * num) % self.MOD) * 500000004) % self.MOD

    def maxProfit(self, inventory: List[int], orders: int) -> int:

        inventory.sort(reverse=True)
        n = len(inventory)
        same_value = 1
        last_ind = 0
        value = 0

        while orders > 0:
            if last_ind < n - 1:
                num = inventory[last_ind] - inventory[last_ind + 1]
            else:
                num = inventory[last_ind]
            if num == 0:
                last_ind += 1
                same_value += 1
                continue
            num_div = orders // num
            if num_div > same_value:
                value_x = self.range_sum(inventory[last_ind], num)
                value = (value + value_x * same_value) % self.MOD

                orders -= same_value * num

            elif num_div < same_value:
                same_value_div = orders // same_value
                value_x = self.range_sum(inventory[last_ind], same_value_div)
                value = (value + value_x * same_value) % self.MOD
                orders -= same_value_div * same_value

                value = (value + orders * (inventory[last_ind] - same_value_div)) % self.MOD
                break
            else:
                value_x = self.range_sum(inventory[last_ind], num)
                value = (value + value_x * num_div) % self.MOD

                orders -= num_div * num
            same_value += 1
            last_ind += 1

        return int(value)


