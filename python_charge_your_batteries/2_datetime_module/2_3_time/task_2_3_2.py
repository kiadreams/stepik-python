from datetime import time

times = {
    time(h, m, s)
    for h in range(24)
    for m in range(60)
    for s in (00, 15, 30, 45)
}
print(times)