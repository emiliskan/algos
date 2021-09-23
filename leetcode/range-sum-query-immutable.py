# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        sums = []

        sum = 0
        for num in nums:
           sum += num
           sums.append(sum)

        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        return self.sums[right] - self.sums[left-1]


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([-2, 0, 3, -5, 2, -1])

r =  numArray.sumRange(0, 2)
assert r == 1, r # return (-2) + 0 + 3 = 1

r = numArray.sumRange(2, 5) # return 3 + (-5) + 2 + (-1) = -1
assert r == -1, r

r = numArray.sumRange(0, 5) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
assert r == -3, r
