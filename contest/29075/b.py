n: int = int(input().strip())
nums: list[int] = list(map(int, input().split()))

pref_sums = [0] * n
max_pref_sum_i = 0
min_pref_sum_i = 0
max_sum = nums[0]

for i in range(0, n):
    pref_sums[i] = pref_sums[i - 1] + nums[i - 1]

print(max_sum)

"""
5 4 -10 4
5 9 -1  3
i = 1


9

5
-1 -2 4 5 -7
0 0 4 9 0

6
-1 -2 -3 -4 -5 -6
"""
