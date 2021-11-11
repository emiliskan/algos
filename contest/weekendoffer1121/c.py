def count_steps(field):
    count = 0
    for n_i in range(len(field)):
        for n_j in range(len(field[n_i])):
            if field[n_i][n_j]:
                continue

            queue = [(n_i, n_j)]
            while queue:

                i, j = queue.pop()
                field[i][j] = True

                indexes = [
                    (i + 1, j),
                    (i, j + 1),
                    (i - 1, j),
                    (i, j - 1)
                ]

                for index in indexes:
                    if (
                            index[0] < 0 or index[1] < 0
                    ) or (
                            index[0] > len(field) - 1 or index[1] > len(field[0]) - 1
                    ):
                        continue

                    if not field[index[0]][index[1]]:
                        queue.append((index[0], index[1]))

            count += 1

    return count

# sizes = list(map(int, input().split()))
#
# k = int(input().strip())
# mines = []
# for _ in range(k):
#     cords = tuple(map(int, input().split()))
#     mines.append(cords)
#
#
# field = [[False for i in range(sizes[0])] for j in range(sizes[1])]
#
# for mine in mines:
#     field[mine[0] - 1][mine[1] - 1] = True
#
# print(count_steps(field))

"""
1: 1
0 0 0
1 1 1
0 0 0
2: 2
0 0 0
1 1 0
0 0 0
3: 2
0 1 0
0 1 0
0 1 0
4: 2
1 0 0
0 1 0
0 0 1

"""
cases = [
    ('1', 3, 3, [(2, 1), (2, 2), (2, 3)], 2),
    ('2', 3, 3, [(2, 1), (2, 2)], 1),
    ('3', 3, 3, [(1, 2), (2, 2), (3, 2)], 2),
    ('4', 3, 3, [(1, 1), (2, 2), (3, 3)], 2),
    ('5', 15, 15, [(1, 1), (2, 2), (3, 3)], 1),
    ('5', 100, 100, [(1, 1), (2, 2), (3, 3)], 1),
]
for case in cases:
    field = [[False for i in range(case[1])] for j in range(case[2])]

    for mine in case[3]:
        field[mine[0] - 1][mine[1] - 1] = True

    res = count_steps(field)
    assert res == case[4], f'{case[0]}: res {res} != {case[4]}'
