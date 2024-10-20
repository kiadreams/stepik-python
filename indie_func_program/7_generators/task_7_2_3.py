weekdays = [
    "Saturday",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]
days = ((i + 1, weekdays[i % 7]) for i in range(365))

for _ in range(77):
    print(next(days))
