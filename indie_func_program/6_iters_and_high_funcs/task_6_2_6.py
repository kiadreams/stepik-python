def from_hex_to_rgb(color: str) -> tuple[int, int, int]:
    return int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)


def convert_to_rgb(values: list[str]) -> list[tuple[int, int, int]]:
    return list(map(from_hex_to_rgb, values))


colors = ['#B22222', '#DC143C', '#FF0000', '#FF6347', '#FF7F50']
print(convert_to_rgb(colors))
