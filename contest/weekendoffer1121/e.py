

def winner():
    ...


cases = [
    ('1', 8, 1, "..-0..-+", [(1, 2), (2, 3), (2, 4), (2, 4), (1, 5), (5, 6), (6, 7)], "First"),
]
for case in cases:
    res = winner()
    assert res == case[4], f'{case[0]}: res {res} != {case[4]}'
