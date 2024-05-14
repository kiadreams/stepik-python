import re

pattern = re.compile(r"^@[a-z\d]{4,14}$")
nickname = input()
print("Correct" if pattern.findall(nickname) else "Incorrect")
