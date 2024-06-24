DIGITS = "123456789"


def is_ascending(n: int) -> bool:
    if n < 10:
        return True
    if (n // 10) % 10 >= n % 10:
        return False
    return is_ascending(n // 10)


def get_limits(n: int) -> tuple[int, int]:
    size = len(str(n))
    return int(DIGITS[:size]), int(DIGITS[-size:])


def forward(reading: int, steps: int = 1) -> int:
    start, limit = get_limits(reading)
    for _ in range(steps):
        if reading == limit:
            reading = start
        else:
            reading += 1
            while not is_ascending(reading):
                reading += 1
    return reading


def backward(reading: int, steps: int = 1) -> int:
    start, limit = get_limits(reading)
    for _ in range(steps):
        if reading == start:
            reading = limit
        else:
            reading -= 1
            while not is_ascending(reading):
                reading -= 1
    return reading


def distance(a_reading: int, b_reading: int) -> int:
    if len(str(a_reading)) != len(str(b_reading)):
        return -1
    diff = 0
    while a_reading != b_reading:
        a_reading = forward(a_reading)
        diff += 1
    return diff

print(backward(456))
print(not(is_ascending(3451)))
