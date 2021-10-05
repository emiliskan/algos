"""
https://contest.yandex.ru/contest/28970/problems/C/
"""

import sys

words = {}
while True:
    entered_words: list = [s.strip() for s in sys.stdin.readline().split()]

    if len(entered_words) == 0:
        break

    for entered_word in entered_words:
        if entered_word not in words:
            words[entered_word] = 0

        words[entered_word] += 1

sorted_words = []
for word in sorted(words.items(), key=lambda x: (-x[1], x[0])):
    print(word[0])

