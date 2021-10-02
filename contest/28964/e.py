"""
https://contest.yandex.ru/contest/28964/problems/E/

"""

import sys

witness_count = int(sys.stdin.readline().strip())
witness_guesses: list[set] = []
for _ in range(witness_count):
    witness_guesses.append(set(sys.stdin.readline().strip()))

numbers_count = int(sys.stdin.readline().strip())
numbers: list[str] = []
for _ in range(numbers_count):
    numbers.append(sys.stdin.readline().strip())

numbers_match_counts = {}
max_count = 0
for i, number in enumerate(numbers):

    numbers_match_counts[i] = 0

    for guess in witness_guesses:
        if guess.issubset(number):
            numbers_match_counts[i] += 1
            if numbers_match_counts[i] > max_count:
                max_count = numbers_match_counts[i]

for k, v in numbers_match_counts.items():
    if v == max_count:
        print(numbers[k])

