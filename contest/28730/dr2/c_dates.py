import sys


def is_right_date(m, d, y):
    if m == d:
        return True

    if m <= 12 and d <= 12:
        return False

    return True


a = sys.stdin.readline().split()
m = int(a[0])
d = int(a[1])
y = int(a[2])

print(int(is_right_date(m, d, y)))

r = is_right_date(1, 12, 2000)
assert r == 0, r

r = is_right_date(1, 24, 2000)
assert r == 1, r

r = is_right_date(1, 30, 2000)
assert r == 1, r

r = is_right_date(19, 2, 2000)
assert r == 1, r

r = is_right_date(2, 3, 2008)
assert r == 0, r

r = is_right_date(15, 12, 2008)
assert r == 1, r

r = is_right_date(2, 29, 2008)
assert r == 1, r

r = is_right_date(3, 3, 2067)
assert r == 1, r