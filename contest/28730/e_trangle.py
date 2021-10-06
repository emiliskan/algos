import sys


def is_in_triangle(x, y, d):

    if x >= 0 and y >= 0 and x + y <= d:
        return 0

    x_diff = x - d
    y_diff = y - d

    if x_diff < 0 and y_diff < 0:
        return 1

    if x_diff <= y_diff:
        return 2

    if y_diff <= x_diff:
        return 3


d = int(sys.stdin.readline())
x1, x2 = map(int, sys.stdin.readline().split())

print(is_in_triangle(x1, x2, d))
