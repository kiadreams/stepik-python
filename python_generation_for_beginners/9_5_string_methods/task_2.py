import re

pattern = re.compile(r"^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}_\d{2,3}$")
number = input()
print("YES" if pattern.findall(number) else "NO")