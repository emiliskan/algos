"""
https://contest.yandex.ru/contest/28970/problems/D/
"""

import sys
from collections import defaultdict

parties = defaultdict(int)
all_votes_count = 0
while True:
    entered_data = sys.stdin.readline().split()
    if not len(entered_data):
        break

    party_name = ' '.join(entered_data[:-1])
    party_votes = int(entered_data[-1])

    parties[party_name] += party_votes
    all_votes_count += party_votes

first_choose_chast = all_votes_count / 450
all_parlament_sits = 0
party_in_parlament = {}
for party, votes in parties.items():
    parlament_sits = int(votes // first_choose_chast)
    drob_sits = votes % first_choose_chast
    party_in_parlament[party] = (drob_sits, parlament_sits)

    all_parlament_sits += parlament_sits

while all_parlament_sits < 450:
    for party, count in sorted(party_in_parlament.items(), key=lambda x: (-x[1][0], x[1][1])):
        party_in_parlament[party] = (count[0], count[1] + 1)
        all_parlament_sits += 1

        if all_parlament_sits == 450:
            break

for party in parties.keys():
    print(party, party_in_parlament[party][1])