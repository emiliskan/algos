# https://contest.yandex.ru/contest/28738/problems/B/
# 1 обозначает жилой дом, число 2 обозначает магазин, число 0 обозначает офисное здание
# Выведите одно целое число: наибольшее расстояние от дома до ближайшего к нему магазина.
# Расстояние между двумя соседними домами считается равным 1
#
# 2 0 1 1 0 1 0 2 1 2
# 3

import sys


def calc(a):
    store = -20
    dists = [0] * len(a)
    for i in range(len(a)):
        if a[i] == "2":
            store = i

        elif a[i] == "1":
            dists[i] = i - store

    store = 30
    for i in reversed(range(len(a))):
        if a[i] == "2":
            store = i

        elif a[i] == "1":
            dists[i] = min(dists[i], store - i)

    return max(dists)


a = sys.stdin.readline().split()
print(calc("2 0 1 1 0 1 0 2 1 2".split()))
