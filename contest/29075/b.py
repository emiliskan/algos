n: int = int(input().strip())
nums: list[int] = list(map(int, input().split()))

max_sum = nums[0]
cur_sum = nums[0]

for i in range(len(nums)):
    if cur_sum < 0:
        cur_sum = nums[i]
    else:
        cur_sum += nums[i]

    max_sum = max(cur_sum, max_sum)

print(max_sum)

"""
8
-1 -2 3 4 5 1 -2 -3

3
-1 0 -3

6
-1 -2 -3 -4 -5 -6

4
5 4 -10 4

5
-1 -2 4 5 -7
0 0 4 9 0

"""
