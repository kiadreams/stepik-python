from datetime import date


def get_min_max(dates: list[date]) -> tuple:
    result = ()
    if dates:
        result = (min(dates), max(dates))
    return result


dates = []
answer = get_min_max(dates)
print(*answer, type(answer))
