from typing import Optional


def calculate_average(numbers: list) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)
