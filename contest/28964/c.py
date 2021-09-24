"""
https://contest.yandex.ru/contest/28964/problems/B/?success=53439349#175943/2016_10_05/UMhQ1iX3LS

"""

import sys


def calc(nums: list[int]) -> list:
    same_nums = {}

    for i in nums:

        if i not in same_nums:
            same_nums[i] = 0
        same_nums[i] += 1

    lonely_nums = []
    for k, v in same_nums.items():
        if v == 1:
            lonely_nums.append(k)

    return lonely_nums


nums = list(map(int, sys.stdin.readline().split()))
print(' '.join(str(i) for i in calc(nums)))
