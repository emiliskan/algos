"""
Есть массив целых чисел, нужно найти количество последовательностей дающих в сумме k.
Алгоритмическая сложность O(n)
"""


def seq_count(nums: list[int], k: int) -> int:
    """
    [
                                        hmap = {0: 1}
     1, s = 1,  count = 0 sum - k = -9, hmap = {1: 1}
     9, s = 10  count = 1 sum - k = 0 , hmap = {10: 2}
     1, s = 11, count = 2 sum - k = 1 , hmap = {11: 1}
     1, s = 12, count = 2 sum - k = 2 , hmap = {12: 1}
     5, s = 17, count = 2 sum - k = 7 , hmap = {17: 1}
     5, s = 22, count = 3 sum - k = 12, hmap = {22: 1}
     6, s = 28, count = 3 sum - k = 18, hmap = {28: 1}
     4, s = 32, count = 4 sum - k = 22, hmap = {32: 1}
     6, s = 38, count = 5 sum - k = 28, hmap = {38: 1}

     ]
    """
    count = 0
    hmap = {0: 1}
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]

        if sum - k in hmap:
            count += hmap[sum - k]

        hmap[sum] = hmap.get(sum, 0) + 1

    return count


#                (nums, k,   count)
cases: list[tuple[list, int, int]] = [
    ([1, 9, 1], 10, 2),
    ([1, 9, 1, 1, 5, 5, 6, 4, 6], 10, 5),

]
for case in cases:
    res = seq_count(case[0], case[1])
    assert res == case[2]
