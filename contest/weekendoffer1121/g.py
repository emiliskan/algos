def min_sum(driver_rate):
    driver_k = {}

    for i in range(len(driver_rate)):
        driver_k[i] = 1

    for i, rate in enumerate(driver_rate):
        recursive(driver_rate, driver_k, i)

    return sum(driver_k.values()) * 500


def recursive(driver_rate, driver_k, i):

    if i < 1:
        return

    if driver_rate[i - 1] > driver_rate[i] and driver_k[i - 1] <= driver_k[i]:
        driver_k[i - 1] += driver_k[i - 1] - driver_k[i] + 1
        recursive(driver_rate, driver_k, i - 1)

    if driver_rate[i - 1] < driver_rate[i] and driver_k[i - 1] >= driver_k[i]:
        driver_k[i] += driver_k[i - 1] - driver_k[i] + 1
        recursive(driver_rate, driver_k, i)


# n = int(input().strip())
#
# driver_rate = []
# for _ in range(n):
#     rate = input().strip()
#     driver_rate.append(rate)
#
# print(min_sum(driver_rate))

cases = [
    ('1', [1, 2, 3, 4], 5000),
    ('2', [5, 5, 5, 5], 2000),
    ('3', [4, 2, 3, 3], 3000),
    ('4', [1, 3, 1, 4], 3000),
    ('5', [], 0),
    ('6', [1, 1, 2, 1], 2500),
    ('7', [2, 3, 2, 1], 3500),
    ('8', [1, 2, 3, 1], 3500),
    ('9', [1, 2, 3, 1, 4], 4500),
    ('10', [0, 0, 0, 1], 2500),
]

for case in cases:
    res = min_sum(case[1])
    assert res == case[2], f'{case[0]}: res {res} != {case[2]}'
