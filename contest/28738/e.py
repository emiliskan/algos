"""
https://contest.yandex.ru/contest/28738/problems/E/

В этом году Иван заканчивает школу и поступает в вуз. За время своей учебы он часто участвовал в олимпиадах по информатике и у него накопилось много дипломов. Иван раскладывал дипломы по папкам совершенно бессистемно, то есть любой диплом мог оказаться в любой из папок. К счастью, Иван помнит, сколько дипломов лежит в каждой из папок.
Иван хочет принести в приемную комиссию выбранного вуза папку, в которой находится диплом Московской олимпиады по программированию (такой диплом у Ивана ровно один). Для того чтобы понять, что в данной папке нужного диплома нет, Ивану нужно просмотреть все дипломы из этой папки. Просмотр одного диплома занимает у него ровно одну секунду и он может мгновенно переходить к просмотру следующей папки после окончания просмотра предыдущей. Порядок просмотра папок Иван может выбирать.
По заданному количеству дипломов в каждой из папок требуется определить, за какое наименьшее время в худшем случае Иван поймет, в какой папке содержится нужный ему диплом.

"""

import sys


def calc(n: int, folders: list):

    max = 0

    for i in range(n):
        if folders[i] > folders[max]:
            max = i

    count = 0
    for i in range(n):
        if i == max:
            continue

        count += folders[i]

    return count



n = int(sys.stdin.readline())
folders = list(map(int, sys.stdin.readline().split()))
print(calc(n, folders))

assert calc(3, [3, 2, 1]) == 3
assert calc(2, [2, 1]) == 1
assert calc(1, [1]) == 0
assert calc(10, [1, 3, 4, 10, 5, 3, 2, 1, 3, 7]) == 29