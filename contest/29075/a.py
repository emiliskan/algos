"""
https://contest.yandex.ru/contest/29075/problems/


"""
import sys

nq = list(map(int, input().split()))
n = nq[0]
q = nq[1]

nums = list(map(int, sys.stdin.readline().split()))
pr_sums = [0] * (len(nums) + 1)

for i in range(1, len(nums) + 1):
    pr_sums[i] = pr_sums[i - 1] + nums[i - 1]

for i in range(q):

    lr = list(map(int, sys.stdin.readline().split()))
    l = lr[0]
    r = lr[1]

    print(pr_sums[r] - pr_sums[l] + l)
