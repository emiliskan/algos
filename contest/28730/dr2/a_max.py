import sys

def calc(nums):

    if not nums:
        return 0

    max = nums[0]
    for i in nums:
        if i > max:
            max = i

    max_count = 0
    for i in nums:
        if i == max:
            max_count += 1
    return max_count


nums = []
while True:
    a = int(sys.stdin.readline())
    if a == 0:
        break

    nums.append(a)

print(calc(nums))

# r = calc([1, 1, 2, 2, 3, 3, 3, 4, 0])
# assert r == 3, r
