"""
Перевод введенных чисел в 16-и ричной значение цвета
"""

rgb = [hex(int(input())).lstrip("0x").rjust(2, "0") for _ in range(3)]
print("#", "".join(rgb).upper(), sep="")
