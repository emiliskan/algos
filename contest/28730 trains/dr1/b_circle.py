
def calc_station_count(n, i, j):
    if abs(i - j) >= n / 2:
        return abs(n - abs(i - j)) - 1
    else:
        return abs(i - j) - 1

a = input()
a = a.split()
n = int(a[0])
i = int(a[1])
j = int(a[2])

print(calc_station_count(n, i, j))

r = calc_station_count(10, 9, 1)
assert r == 1, r

r = calc_station_count(10, 5, 3)
assert r == 1, r

r = calc_station_count(10, 3, 5)
assert r == 1, r

r = calc_station_count(10, 5, 6)
assert r == 0, r

r = calc_station_count(100, 5, 6)
assert r == 0, r

r = calc_station_count(10, 1, 9)
assert r == 1, r

r = calc_station_count(10, 8, 2)
assert r == 3, r

r = calc_station_count(10, 9, 8)
assert r == 0, r
