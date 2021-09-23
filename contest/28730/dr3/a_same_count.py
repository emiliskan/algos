"""

 https://contest.yandex.ru/contest/28738/problems/B/

На Новом проспекте построили подряд 10 зданий.
Каждое здание может быть либо жилым домом, либо магазином, либо офисным зданием.

Но оказалось, что жителям некоторых домов на Новом проспекте слишком далеко приходится идти до ближайшего магазина.
Для разработки плана развития общественного транспорта на Новом проспекте мэр города попросил вас выяснить,
какое же наибольшее расстояние приходится преодолевать жителям Нового проспекта,
чтобы дойти от своего дома до ближайшего магазина

1 обозначает жилой дом, число 2 обозначает магазин, число 0 обозначает офисное здание

2 0 1 1 0 1 0 2 1 2
3
"""

import sys


def calc(a):
    max_dist = 0
    for i in range(len(a) - 1):

        if a[i] != "1":
            continue

        dist_fow = 0
        for j in range(i, len(a) - 1):

            if a[j] == "2":
                break

            dist_fow += 1

            if j == len(a) - 1:
                dist_fow = 0

        dist_back = 0
        for j in range(i, -1, -1):

            if a[j] == "2":
                break

            dist_back += 1

            if j == 0:
                dist_back = 0

        dist = min(dist_fow, dist_back)
        if dist > max_dist:
            max_dist = dist

    return max_dist


def assert_res(func, data, right):
    r = func(data)
    assert r == right, f"Expected: {right} got {r}"


assert_res(calc, "2 0 1 1 0 1 0 2 1 2".split(), 3)
assert_res(calc, "1 1 1 1 1 1 1 1 1 2".split(), 1)
assert_res(calc, "2 0 1 1 0 1 0 2 1 2".split(), 3)
assert_res(calc, "2 0 1 1 0 1 0 2 1 2".split(), 3)
assert_res(calc, "2 0 1 1 0 1 0 2 1 2".split(), 3)

# a = sys.stdin.readline().split()
# print(calc(a))
