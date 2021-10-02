"""
https://contest.yandex.ru/contest/28970/problems/
"""

import sys

color_count: int = int(sys.stdin.readline().strip())
colors: dict[int, int] = {}
for _ in range(color_count):
   boxes: list = sys.stdin.readline().split()
   box: tuple[int, int] = int(boxes[0]), int(boxes[1])

   if not box[0] in colors:
      colors[box[0]] = 0

   colors[box[0]] += box[1]

sorted_colors: list[int] = sorted(colors.keys())
for k in sorted_colors:
   print(f'{k} {colors[k]}')