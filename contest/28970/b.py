"""
https://contest.yandex.ru/contest/28970/problems/B/
"""

import sys

candidates_count = {}
while True:
    candidate_choices: list = sys.stdin.readline().split()

    if len(candidate_choices) == 0:
        break

    candidate, choices = candidate_choices[0], int(candidate_choices[1])
    if candidate not in candidates_count:
        candidates_count[candidate] = 0

    candidates_count[candidate] += choices

sorted_cands = sorted(candidates_count.keys())
for candidate in sorted_cands:
    print(f"{candidate} {candidates_count[candidate]}")
