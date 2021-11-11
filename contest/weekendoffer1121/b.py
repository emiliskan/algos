"""
6 5 10
1 2 3 4 5 6

10
"""


def solved_day(robot_period, critical_day, deadlines):

    if not deadlines:
        return 0

    robot_days = []
    robot_iter = 0
    while True:

        for day in deadlines:
            robot_day = day + (robot_period * robot_iter)
            if robot_day in robot_days:
                continue

            robot_days.append(robot_day)

        if len(robot_days) >= (critical_day + len(deadlines)):
            break

        robot_iter += 1

    return sorted(robot_days)[critical_day - 1]


# first = input().split()
# n = int(first[0])  # количество задач 6
# x = int(first[1])  # периодичность работы робота 5
# k = int(first[2])  # критчиеское количество 10
#
# deadlines = list(map(int, input().split()))
#
# print(solved_day(x, k, deadlines))
#                (id,  r_p, cr_d, deadlines, result)
cases: list[tuple[str, int, int, list, int]] = [
    ('1', 5, 10, [1, 2, 3, 4, 5, 6], 10),
    ('2', 7, 12, [5, 22, 17, 13, 8], 27),
    ('3', 7, 25, [5, 22, 17, 13, 8], 50),
    ('4', 7, 25, [], 0),
    ('5', 7, 25, [], 0),

]
for case in cases:
    res = solved_day(case[1], case[2], case[3])
    assert res == case[4], f'{case[0]}: res {res} != {case[4]}'
