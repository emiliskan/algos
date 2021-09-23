"""
https://contest.yandex.ru/contest/28738/problems/C/

В строкоремонтную мастерскую принесли строку, состоящую из строчных латинских букв.
Заказчик хочет сделать из неё палиндром. В мастерской могут за 1 байтландский тугрик заменить произвольную букву
в строке любой выбранной заказчиком буквой.
Какую минимальную сумму придётся заплатить заказчику за ремонт строки?
Напомним, что палиндромом называется строка, которая равна самой себе, прочитанной в обратном направлении

cognitive: 4

"""

import sys


def calc(string):

    count = 0
    str_len = len(string) - 1
    half = len(string) // 2

    for i in range(half):
        if string[i] != string[str_len - i]:
            count += 1

    return count


# string = sys.stdin.readline().strip()
# print(calc(string))

assert calc("cognitive") == 4
assert calc("a") == 0
assert calc("ab") == 1
assert calc("aaaaaaaaaa") == 0
assert calc("aaaaiaaaa") == 0
assert calc("aaaabaaaaa") == 1
