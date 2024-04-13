from datetime import timedelta


delta1 = timedelta(days=50, seconds=27, microseconds=10,
                   milliseconds=29000, minutes=5, hours=8, weeks=2)
delta2 = timedelta(weeks=1, hours=23, minutes=61)
delta3 = timedelta(hours=25)
delta4 = timedelta(minutes=300)

print(delta1, delta2, delta3, delta4, sep='\n')
print()


delta1 = timedelta(minutes=-2)
delta2 = timedelta(seconds=-10, weeks=-2)

print(delta1, delta2)
print(delta1, delta1.days, delta1.seconds, delta1.microseconds)
print(delta1.total_seconds())
