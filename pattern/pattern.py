# --------------------
# Print a pyramid
# --------------------
import sys

WIDTH = 60
STAR, SPACE, LF, NONE = "*", " ", "\n", ""
START, REPEAT, FINISH = STAR, STAR + STAR, NONE
#START, REPEAT, FINISH = "#", "__", "\b#"


def make_pattern(size: int) -> list[str]:
    return [line(line_num) for line_num in range(size)]


def line(n: int) -> str:
    return start(n) + middle(n) + end(n)


def start(n: int) -> str:
    return START


def middle(n: int) -> str:
    return n * REPEAT


def end(n: int) -> str:
    return FINISH


def format_pyramid(pattern: list[str]) -> list[str]:
    return LF.join(line.center(WIDTH) for line in pattern)


def format_left_triangle(pattern: list[str]) -> list[str]:
    return LF.join([line for line in pattern])


def format_right_triangle(pattern: list[str]) -> list[str]:
    return LF.join([line.rjust(WIDTH) for line in pattern])


def format_diamond(pattern: list[str]) -> list[str]:
    pattern = pattern + pattern[::-1][1:]
    return LF.join(line.center(WIDTH) for line in pattern)


def format_arrow(pattern: list[str]) -> list[str]:
    pattern = pattern + pattern[::-1][1:]
    return LF.join(line for line in pattern)


argc = len(sys.argv)
if argc not in {2, 3}:
    print("Usage: python3 pyramid.py rows [screen width]")
else:
    size = int(sys.argv[1])
    if argc == 3:
        WIDTH = int(sys.argv[2])
    print(format_pyramid(make_pattern(size)))
    print(format_arrow(make_pattern(size)))
    #print(format_diamond(make_pattern(size)))
