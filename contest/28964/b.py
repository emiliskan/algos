"""
https://contest.yandex.ru/contest/28964/problems/B/?success=53439349#175943/2016_10_05/UMhQ1iX3LS

"""

import sys


def calc(nums: list[int]):

    same_nums = set()

    for i in nums:
        if i in same_nums:
            print("YES")
            continue

        print("NO")
        same_nums.add(i)


nums = list(map(int, sys.stdin.readline().split()))
calc(nums)