"""
https://contest.yandex.ru/contest/28964/problems/D/

"""

import sys

max_value = int(sys.stdin.readline().strip())

in_set = []
not_int_set = []

possible = set(range(1, max_value+1))
while True:
    guess = sys.stdin.readline().strip()
    if guess == "HELP":
        break

    guesses = list(map(int, guess.split()))
    answer = sys.stdin.readline().strip()

    if answer == "YES":
        possible.intersection_update(guesses)
    elif answer == "NO":
        possible.difference_update(guesses)

print(' '.join(str(i) for i in sorted(possible)))
