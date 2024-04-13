from datetime import date


dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
for dt in dates:
    print(dt.strftime('%d/%m/%Y'))
